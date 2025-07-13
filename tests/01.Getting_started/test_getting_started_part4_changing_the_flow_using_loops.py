from spike import ForceSensor, Motor

def test_getting_started_part4_changing_the_flow_using_loops():
	# This program uses a loop to control the motor with the Force Sensor.
	# The motor will start when the Force Sensor is pressed and stop when it is released.
	# The loop will repeat this process 5 times.
	# The program also measures the force in newtons or as a percentage and uses it to control the motor speed.
	# Initialize the Force Sensor, a motor, and a variable
	force_sensor = ForceSensor('B')
	motor = Motor('C')
	count = 0
	# You can press the Force Sensor 5 times 
	motor.set_default_speed(25)
	while count < 5:
		force_sensor.wait_until_pressed()
		motor.start()
		force_sensor.wait_until_released()
		motor.stop()
		count = count + 1


	count = 0
	while count < 5:
		# Measure the force in newtons or as a percentage
		percentage = force_sensor.get_force_percentage()
		# Use the measured force to start the motor
		motor.start(percentage)
		count = count + 1
