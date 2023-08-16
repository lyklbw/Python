def word_Count(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        return int(num_words)

all=0
file_list=["Alice.txt","pi_digits.txt","programming.txt"]
for file in file_list:
    all+=word_Count(file)
print(all)