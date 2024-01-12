class Nissan_m: 
	def __init__(self): 
		self.models = ['altima', '370z', 'cube', 'rogue'] 

	def Models(self): 
		print('These are the available models for Nissan') 
		for model in self.models: 
			print('NISSAN',model,"\n") 
