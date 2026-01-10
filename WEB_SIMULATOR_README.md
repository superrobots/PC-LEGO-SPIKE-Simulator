# LEGO SPIKE Web Simulator - POC

A proof-of-concept web-based interface for the LEGO SPIKE simulator that allows you to test LEGO SPIKE Python code directly in your web browser without any hardware.

## Features

- **Web-based Code Editor**: Write and edit LEGO SPIKE Python code in the browser
- **Real-time Execution**: Run code and see console output immediately
- **Visual Feedback**: 5x5 LED matrix visualization (simulated SPIKE Hub display)
- **Example Programs**: Pre-loaded examples for quick testing
- **No Installation Required**: Run the simulator from any browser

## Requirements

- Python 3.12+
- Flask web framework

## Installation

1. Install Flask dependencies:
```bash
pip install -r requirements-web.txt
```

## Usage

1. Start the web simulator:
```bash
python web_simulator.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. You'll see the web interface with:
   - **Left panel**: Code editor and console output
   - **Right panel**: Simulated SPIKE Hub with LED matrix and example programs

4. Write or load example LEGO SPIKE Python code and click **Run Code** to execute it.

## Features Overview

### Code Editor
- Full Python syntax support
- Pre-populated with a simple example
- Keyboard shortcut: `Ctrl+Enter` or `Cmd+Enter` to run code

### Console Output
- Shows all print statements and debug output
- Displays errors with detailed messages
- Clear button to reset console

### LED Matrix Visualization
- 5x5 LED grid representing the SPIKE Hub display
- LEDs light up when showing images
- Visual feedback for light matrix operations

### Example Programs
Three built-in examples to get started:
1. **Simple Output**: Display images on the LED matrix
2. **Motor Control**: Control motors on different ports
3. **Distance Sensor**: Read from distance sensor

### API Endpoints

The web simulator exposes these REST API endpoints:

- `GET /` - Main web interface
- `POST /api/run` - Execute Python code
  - Request: `{"code": "python code here"}`
  - Response: `{"success": true/false, "output": [...], "error": null}`
- `GET /api/status` - Get current simulator state
- `POST /api/reset` - Reset the simulator

## How It Works

The web simulator:
1. Provides a Flask web server that serves an HTML/CSS/JavaScript interface
2. Accepts Python code through a REST API
3. Executes the code in a sandboxed environment with access to the spike module
4. Captures console output and returns it to the browser
5. Updates the visual display based on simulator state

## Limitations (POC)

This is a proof-of-concept and has some limitations:
- LED matrix visualization is basic (shows lit/unlit states)
- Sensor values are simulated (Random, Circular, or Console modes)
- No real-time motor visualization
- Execution is synchronous (one program at a time)
- Basic security sandbox (not production-ready)

## Security Note

⚠️ This POC runs user-provided Python code on the server. It is intended for local development and testing only. Do NOT expose this to the internet without proper security measures.

## Future Enhancements

Potential improvements for a production version:
- Better code editor with syntax highlighting (CodeMirror/Monaco)
- Enhanced LED matrix animations
- Motor and sensor visualizations
- Multi-user support with session isolation
- Improved code execution sandbox
- Save/load programs functionality
- Share code snippets feature

## Testing

To test the web simulator:

1. Run the default example (already loaded in the editor)
2. Try the Distance Sensor example:
   - Click "Distance Sensor" in the examples panel
   - Click "Run Code"
   - See simulated sensor readings in the console

3. Try creating your own program:
```python
from spike import PrimeHub

hub = PrimeHub()
print("Hello from LEGO SPIKE!")
hub.light_matrix.show_image('HAPPY')
```

## Troubleshooting

**Module not found errors:**
- Make sure you're running the script from the repository root directory
- The spike module should be in the same directory as web_simulator.py

**Port already in use:**
- Change the port in web_simulator.py (last line) to a different number
- Or kill the process using port 5000

**Visualization not working:**
- The web interface works without tkinter (unlike the desktop visualization)
- LED matrix updates are basic in this POC version

## License

Same as the main PC-LEGO-SPIKE-Simulator project.
