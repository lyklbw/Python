filename="Alice.txt"
try:
    with open(filename) as f_obj:
        content=f_obj.read()
except FileNotFoundError:
    msg="Sorry,the file "+filename+" does not exist."
    print(msg)
else:
    words=content.split()
    num_words=len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")