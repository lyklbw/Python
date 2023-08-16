filename="alice.txt"
try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    message="Sorry,the file is not exist."
    print(message)
else:
    words=contents.split()
    num_words=len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")
