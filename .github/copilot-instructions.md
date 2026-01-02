# GitHub Copilot Instructions for PC-LEGO-SPIKE-Simulator

## Project Overview

This is an unofficial PC-based LEGO SPIKE simulator written in Python. It allows users to test LEGO SPIKE Python code without physical hardware by simulating sensors, motors, and other peripherals.

## Key Technologies

- **Python**: Requires Python 3.12+
- **Package Manager**: Uses `uv` for dependency management
- **Testing Framework**: pytest for unit tests

## Project Structure

```
spike/                  # Core simulator modules (sensors, motors, controls)
├── simulator.py        # Base simulator logic with three modes: Random, Circular, Console
├── motor.py           # Motor simulation
├── distance_sensor.py # Distance sensor simulation
├── color_sensor.py    # Color sensor simulation
└── ...                # Other sensor/actuator modules

tests/                 # Test files organized by component
example/               # Example programs demonstrating simulator usage
main_ui.py            # UI entry point for visualization
visualization.py      # 2D visualization
visualization_3d.py   # 3D visualization
```

## Coding Conventions

### General Python Style

- Use **tabs for indentation** (not spaces) - this project uses tabs throughout
- Class names use PascalCase (e.g., `DistanceSensor`, `Motor`)
- Variable names use snake_case (e.g., `distance_cm`, `default_speed`)
- Module-level constants use SCREAMING_SNAKE_CASE (e.g., `ISDEBUG`, `SIMULATORTYPE`)

### Simulator-Specific Conventions

#### Debug Mode

Every simulator module has an `ISDEBUG` class variable:
- Set to `True` by default to print debug information to console
- Debug prints should use format: `if(self.ISDEBUG):print("description. Variable:", str(value))`
- Always include descriptive context in debug messages

#### Simulator Configuration

Each sensor/actuator module should include these configuration constants:
- `SIMULATORTYPE`: Defines simulation mode - "Random", "Circular", or "Consol"
- `SIMULATORTIME`: Time between changes (for Circular mode)
- `SIMULATORCHANGE`: Amount of value change per period (for Circular mode)
- `SIMULATORSWITCHMAX`: Maximum threshold value
- `SIMULATORSWITCHMIN`: Minimum threshold value

#### Simulation Modes

The simulator supports three modes:
1. **Random**: Returns random values within the valid range
2. **Circular**: Values increase/decrease cyclically between min and max
3. **Consol**: Prompts user for input via console

### Code Patterns

#### Module Initialization

```python
class SensorName:
    ISDEBUG = True
    SIMULATORTYPE = "Random"  # or "Circular" or "Consol"
    SIMULATORTIME = 3
    SIMULATORCHANGE = 10
    SIMULATORSWITCHMAX = 80
    SIMULATORSWITCHMIN = 0
    
    def __init__(self, port):
        self.port = port
        self.simulator = simulator.Simulator()
        if(self.ISDEBUG):print("Sensor initialized in debug mode...")
```

#### Using the Simulator

Always use `simulator.get_new_value()` for simulated readings:

```python
self.value, self.direction = self.simulator.get_new_value(
    issimulation=True,
    simulationtype=self.SIMULATORTYPE,
    isdebug=self.ISDEBUG,
    actualvalue=self.value,
    newreading=None,
    minvalue=0,
    maxvalue=100,
    name="descriptive name",
    direction=self.direction,
    change=self.SIMULATORCHANGE,
    iswait=False,
    switch_min=self.SIMULATORSWITCHMIN,
    switch_max=self.SIMULATORSWITCHMAX,
    isextern=False,
    minreading=0,
    maxreading=100
)
```

### Import Statements

- Use comma-separated imports for standard library: `import random,time`
- Import from spike package: `from spike import DistanceSensor`
- Import simulator: `from spike import simulator`

### Documentation

- Use docstrings for complex methods, especially those matching LEGO SPIKE API
- Include parameter types, values, and defaults in docstrings
- Document return types and possible errors
- See existing modules for examples (e.g., `distance_sensor.py`)

## Testing Guidelines

### Test Organization

- Tests are organized in directories matching example structure (e.g., `tests/05.Distance_sensor/`)
- Each test file focuses on a single method or feature
- Test file naming: `test_<module>_<method>.py`

### Test Structure

```python
'''<Method signature and documentation>
Parameters
<parameter descriptions>
Returns
<return value description>
Errors
<possible errors>
Example'''
from spike import ModuleName

def test_module_method():
    # Initialize the component
    component = ModuleName('E')
    
    # Test the functionality
    result = component.method()
    
    # Print results (tests often print for manual verification)
    print('Result:', result)
```

### Running Tests

- Use pytest: `pytest` or `pytest tests/`
- Tests may rely on manual verification of console output
- Not all tests use assertions - some are demonstration/example tests

## Building and Running

### Setup with uv

```bash
uv sync                 # Install dependencies
uv run pytest          # Run tests
```

### Running Examples

```bash
python example/01.Getting_started/getting_started.part1_simple_output.py
```

### Running with Visualization

```bash
python main_ui.py      # 2D visualization
python visualization_3d.py  # 3D visualization
```

## Development Workflow

1. **Adding New Sensors/Actuators**:
   - Create new module in `spike/` directory
   - Follow existing patterns for ISDEBUG, SIMULATORTYPE, etc.
   - Use the `Simulator` class for value generation
   - Add corresponding tests in `tests/` directory

2. **Modifying Existing Modules**:
   - Maintain backward compatibility with LEGO SPIKE API
   - Keep simulator configuration constants accessible
   - Update debug messages to reflect changes
   - Test with different SIMULATORTYPE values

3. **Adding Tests**:
   - Create test directory matching the component number/name
   - One test file per method
   - Include docstring documentation from LEGO SPIKE API
   - Tests should be runnable and produce console output

## Important Notes

- This is a **simulator**, not the actual LEGO SPIKE implementation
- Some functionality is not fully implemented - this is expected
- The goal is API compatibility, not perfect hardware emulation
- Debug output is important for understanding simulator behavior
- Users can modify simulator behavior by editing module files directly

## Common Pitfalls

- Don't use spaces for indentation - this project consistently uses tabs
- Don't remove or modify ISDEBUG, SIMULATORTYPE, and other configuration constants
- Don't assume all LEGO SPIKE features are fully implemented
- Don't forget to import the simulator class when needed
- Don't change the API surface to maintain compatibility with real LEGO SPIKE code

## Dependencies

- Minimize external dependencies - the core simulator should work with Python standard library
- visualization features may use additional libraries
- Use `uv` for dependency management (not pip directly)
- All dependencies must be compatible with Python 3.12+
