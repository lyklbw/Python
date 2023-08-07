storage=[]

help="input whatever city you wanna go input quit to out"
flag=True
while flag==True:
	message=input(help+"\n")
	if(message=="quit"):
		flag=False
	else:
		storage.append(message)
	if not flag :
		break;
for tmp in storage:
	print(tmp)
