import time
def print_machine(unprinted_designs,completed_models):
	"""检验"""

	while unprinted_designs:
		current_designs=unprinted_designs.pop();
		print("printing"+current_designs+ " waiting waiting...\n")
		time.sleep(1)
		print(current_designs+"has been printed")
		completed_models.append(current_designs)

a=['LBJ','KD',"Jordan"]
b=[]
print_machine(a,b)
print('a:')
print(a)
print('\nb:') 
print(b)	
