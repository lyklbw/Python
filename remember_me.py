import json
filename="username.json"

try:
    with open(filename) as f_obj:
        username=json.load(f_obj)
except FileNotFoundError:
    username=input("What is your name?\n")
    with open(filename,'a') as f_obj:    
        json.dump(username,f_obj)
        print("We'll remember you when you come back, "+username+"!")
else:
    print("Welcome back, "+username+"!")
#先try 如果没有问题就是进入else 如果有问题就是进入except