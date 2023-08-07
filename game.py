point=0
alien_color=['yellow','red','blue','black']
if 'red' in alien_color:
	point=point+5
	
if 'yellow' in alien_color:
	point=point+10
if 'black' in alien_color:
	point=point-1

print(point)
