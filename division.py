#try:
#	print(5/0)
#	except ZeroDivisionError:
#	print("you can not divide by 0")
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
	first=input("\nFirst number: ")
	if first=='q':
		break
	second=input("Second number: ")
	if second=='q':
		break
	try:
		answer=int(first)/int(second)	
	except ZeroDivisionError:
		print("you can not divide by 0")
	else:
		print(answer)

