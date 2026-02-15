class Status_light:
	ISDEBUG = True
	#max LED number
	MAXLEDNUMBER = 8
	#actual LED ID
	LEDID = 0
	

	def __init__(self, visualizer=None):
		self.visualizer = visualizer
		if(self.ISDEBUG):print("Status light is initialised in debug mode. Simulation Maximum LED:",self.MAXLEDNUMBER ," change at spike.status_light.py ")
		print("Simulated status light ")

	def on(self,color='white'):
		if(self.ISDEBUG):print("Sets the color of the light to: ",color)
		print("Simulated status light is turned on with this color:",color)
		if self.visualizer:
			self.visualizer.update_status_light(color, True)

	def off(self):
		if(self.ISDEBUG):print("Turns off the light.")
		print("Simulated status light is turned off")
		if self.visualizer:
			self.visualizer.update_status_light(None, False)
		