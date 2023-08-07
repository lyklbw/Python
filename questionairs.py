message={

}

Flag=True

while Flag :
	name=input("where u wanna go ?\n")
	when=input("when to go ?\n")
	
	message[name]=when

	response=input("again?\n")
	if response == 'no':
		Flag=False

print(message)
