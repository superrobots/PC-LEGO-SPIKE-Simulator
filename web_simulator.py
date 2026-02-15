"""
Web-based LEGO SPIKE Simulator POC
A Flask web server that provides a browser-based interface to the LEGO SPIKE simulator.
"""
import sys
import os
import io
import json
from contextlib import redirect_stdout, redirect_stderr
from flask import Flask, render_template, request, jsonify
from threading import Lock

# Add the current directory to the Python path so we can import spike modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
execution_lock = Lock()

# Global state to track simulator outputs
simulator_state = {
	'console_output': [],
	'light_matrix': [[0]*5 for _ in range(5)],
	'status_light': {'color': None, 'is_on': False},
	'last_error': None
}

class WebVisualizer:
	"""Simple visualizer for web simulator that updates global state"""
	def update_light_matrix(self, matrix):
		simulator_state['light_matrix'] = matrix
	
	def update_status_light(self, color, is_on):
		simulator_state['status_light'] = {'color': color, 'is_on': is_on}


class OutputCapture:
	"""Captures stdout and stderr during code execution"""
	def __init__(self):
		self.outputs = []
	
	def write(self, text):
		if text.strip():
			self.outputs.append(text)
	
	def flush(self):
		pass
	
	def get_output(self):
		return ''.join(self.outputs)

@app.route('/')
def index():
	"""Serve the main web interface"""
	return render_template('index.html')

@app.route('/api/run', methods=['POST'])
def run_code():
	"""Execute Python code in the simulator"""
	with execution_lock:
		try:
			# Get the code from request
			data = request.get_json()
			code = data.get('code', '')
			
			# Clear previous state
			simulator_state['console_output'] = []
			simulator_state['last_error'] = None
			
			# Capture output
			output_capture = OutputCapture()
			
			# Create a visualizer for this execution
			visualizer = WebVisualizer()
			
			# Inject visualizer into builtins so spike modules can access it
			import builtins
			old_visualizer = getattr(builtins, '__web_visualizer__', None)
			builtins.__web_visualizer__ = visualizer
			
			# Create a safe execution environment
			exec_globals = {
				'__builtins__': __builtins__,
				'print': lambda *args, **kwargs: output_capture.write(' '.join(map(str, args)) + '\n'),
				'__web_visualizer__': visualizer  # Make visualizer available
			}
			
			# Redirect stdout and stderr
			old_stdout = sys.stdout
			old_stderr = sys.stderr
			
			try:
				sys.stdout = output_capture
				sys.stderr = output_capture
				
				# Execute the code
				exec(code, exec_globals)
				
			finally:
				sys.stdout = old_stdout
				sys.stderr = old_stderr
				# Restore old visualizer in builtins
				if old_visualizer is None:
					if hasattr(builtins, '__web_visualizer__'):
						delattr(builtins, '__web_visualizer__')
				else:
					builtins.__web_visualizer__ = old_visualizer
			
			# Get the captured output
			output = output_capture.get_output()
			simulator_state['console_output'] = output.split('\n') if output else []
			
			return jsonify({
				'success': True,
				'output': simulator_state['console_output'],
				'error': None
			})
			
		except Exception as e:
			error_msg = f"{type(e).__name__}: {str(e)}"
			simulator_state['last_error'] = error_msg
			return jsonify({
				'success': False,
				'output': simulator_state['console_output'],
				'error': error_msg
			}), 400

@app.route('/api/status', methods=['GET'])
def get_status():
	"""Get current simulator state"""
	return jsonify({
		'console_output': simulator_state['console_output'],
		'light_matrix': simulator_state['light_matrix'],
		'status_light': simulator_state['status_light'],
		'last_error': simulator_state['last_error']
	})

@app.route('/api/reset', methods=['POST'])
def reset_simulator():
	"""Reset the simulator state"""
	with execution_lock:
		simulator_state['console_output'] = []
		simulator_state['light_matrix'] = [[0]*5 for _ in range(5)]
		simulator_state['status_light'] = {'color': None, 'is_on': False}
		simulator_state['last_error'] = None
		
		return jsonify({
			'success': True,
			'message': 'Simulator reset successfully'
		})

if __name__ == '__main__':
	print("Starting LEGO SPIKE Web Simulator...")
	print("Open your browser to: http://localhost:5000")
	app.run(debug=True, host='0.0.0.0', port=5000)
