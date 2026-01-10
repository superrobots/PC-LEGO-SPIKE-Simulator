"""
Test script to verify the web simulator works correctly
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_spike_import():
	"""Test that spike module can be imported"""
	try:
		import spike
		print("✓ Spike module imported successfully")
		return True
	except Exception as e:
		print(f"✗ Failed to import spike module: {e}")
		return False

def test_web_simulator_import():
	"""Test that web_simulator can be imported"""
	try:
		import web_simulator
		print("✓ Web simulator module imported successfully")
		return True
	except Exception as e:
		print(f"✗ Failed to import web_simulator: {e}")
		return False

def test_flask_import():
	"""Test that Flask is available"""
	try:
		import flask
		print("✓ Flask imported successfully")
		return True
	except Exception as e:
		print(f"✗ Failed to import Flask: {e}")
		print("  Install with: pip install -r requirements-web.txt")
		return False

def test_basic_execution():
	"""Test that basic LEGO SPIKE code can be executed"""
	try:
		from spike import PrimeHub
		hub = PrimeHub()
		print("✓ PrimeHub instantiated successfully")
		return True
	except Exception as e:
		print(f"✗ Failed to instantiate PrimeHub: {e}")
		return False

if __name__ == "__main__":
	print("Testing Web Simulator Components...\n")
	
	results = []
	results.append(test_spike_import())
	results.append(test_flask_import())
	results.append(test_web_simulator_import())
	results.append(test_basic_execution())
	
	print(f"\n{'='*50}")
	passed = sum(results)
	total = len(results)
	print(f"Tests passed: {passed}/{total}")
	
	if passed == total:
		print("✓ All tests passed! Web simulator is ready to use.")
		print("\nTo start the web simulator, run:")
		print("  python web_simulator.py")
		sys.exit(0)
	else:
		print("✗ Some tests failed. Please check the errors above.")
		sys.exit(1)
