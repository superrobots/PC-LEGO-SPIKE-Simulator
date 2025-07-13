import time

class wait_for_seconds:
	
	def __init__(self,second):
		time.sleep(second)

def wait_until(condition, timeout=10):
	"""Wait until a condition is met or timeout is reached."""
	start_time = time.time()
	while not condition():
		if time.time() - start_time > timeout:
			raise TimeoutError("Condition not met within timeout period.")
		time.sleep(0.1)  # Sleep for a short duration to avoid busy waiting

class Timer:
	
	def __init__(self):
		self.start = time.time()
	
	def now(self):
		dif = time.time()- self.start
		print("time.now", dif) 
		return dif

	def reset(self):
		self.start = time.time()
		print("time.reset", self.start) 
		return self.start