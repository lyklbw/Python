import json
filename="username1.json"
with open(filename,"w") as f_obj:
    for x in range(1,9):
        usename="lyklbw"+str(x)
        json.dump(usename,f_obj,indent=4)
        
with open(filename) as f_obj:
    for line in f_obj:
        print(line,end='\n')
        