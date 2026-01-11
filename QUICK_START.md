# Quick Start Guide - LEGO SPIKE Web Simulator

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/superrobots/PC-LEGO-SPIKE-Simulator.git
   cd PC-LEGO-SPIKE-Simulator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements-web.txt
   ```
   
   This will install Flask and Werkzeug.

3. **Run the test** (optional but recommended):
   ```bash
   python test_web_simulator.py
   ```
   
   You should see:
   ```
   ✓ All tests passed! Web simulator is ready to use.
   ```

## Starting the Simulator

Run the web simulator:
```bash
python web_simulator.py
```

You should see:
```
Starting LEGO SPIKE Web Simulator...
Open your browser to: http://localhost:5000
 * Running on http://127.0.0.1:5000
```

## Using the Web Interface

1. **Open your browser** and navigate to: `http://localhost:5000`

2. **Code Editor** (left panel):
   - Write or edit your LEGO SPIKE Python code
   - Default example is already loaded
   - Use `Ctrl+Enter` (or `Cmd+Enter` on Mac) to run code quickly

3. **Run Your Code**:
   - Click the green **"▶ RUN CODE"** button
   - Watch the console output below the editor
   - See the status bar at the bottom turn green for success

4. **Try Example Programs** (right panel):
   - Click "Simple Output" to load a basic example
   - Click "Motor Control" to test motor functions
   - Click "Distance Sensor" to try sensor reading

5. **Clear Console**:
   - Click the red **"CLEAR"** button to clear console output

6. **Reset Simulator**:
   - Click the blue **"RESET SIMULATOR"** button to reset state

## Example Code

### Hello World
```python
from spike import PrimeHub

hub = PrimeHub()
print("Hello from LEGO SPIKE!")
```

### LED Matrix
```python
from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()
hub.light_matrix.show_image('HAPPY')
wait_for_seconds(2)
hub.light_matrix.show_image('HEART')
```

### Distance Sensor
```python
from spike import DistanceSensor

sensor = DistanceSensor('E')
distance = sensor.get_distance_cm()
print("Distance:", distance, "cm")
```

### Motor Control
```python
from spike import Motor

motor = Motor('A')
motor.run_for_degrees(360, speed=50)
print("Motor position:", motor.get_position())
```

## Troubleshooting

### "Module not found" errors
- Make sure you're in the repository directory
- The `spike` folder should be in the same directory as `web_simulator.py`

### "Port already in use"
- Another program is using port 5000
- Edit `web_simulator.py` and change the port number in the last line:
  ```python
  app.run(debug=True, host='0.0.0.0', port=5001)  # Changed to 5001
  ```

### Page won't load
- Check that the server is running (you should see Flask output)
- Try http://127.0.0.1:5000 instead of localhost
- Check your firewall settings

### Code execution hangs
- The simulator uses debug mode by default (verbose output)
- Wait for execution to complete
- Check the console for prompts (in "Consol" simulator mode)

## Understanding Console Output

The simulator runs in **debug mode** by default, showing detailed information:

```
Distance sensor is initialised in debug mode. Button type:Random
Retrieves the measured distance in centimeters.
distance sensor distance_cm simulated random number:153
Distance: 153 cm
```

This helps you understand what the simulator is doing. To reduce output, you can modify the `ISDEBUG` variable in the spike module files.

## Simulator Modes

Each sensor/actuator can operate in three modes:

1. **Random**: Returns random values (default)
2. **Circular**: Values cycle between min and max
3. **Consol**: Prompts you to enter values

To change modes, edit the corresponding file in the `spike/` directory and change the `SIMULATORTYPE` variable.

## Next Steps

- Explore the example programs in the `example/` directory
- Modify the simulator settings in `spike/` module files
- Read the full documentation in `WEB_SIMULATOR_README.md`
- Try writing your own LEGO SPIKE programs!

## Getting Help

- Check `WEB_SIMULATOR_README.md` for detailed documentation
- Review example programs in the `example/` directory
- Check the original README.md for simulator concepts
- Open an issue on GitHub if you find bugs

## Security Warning

⚠️ The web simulator executes Python code on your computer. Only use it locally and don't expose it to the internet without proper security measures.

---

**Enjoy coding with the LEGO SPIKE Web Simulator!** 🤖
