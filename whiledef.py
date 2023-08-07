
def function(city_name,city_time):
	print("I wanna go to "+city_name+city_time)

Flag=True
while Flag:
	name=input("where to go\n")
	time=input("when to go\n")
	function(name,time)
	response=input("if continue\n")
	if response=='no' :
		Flag=False

