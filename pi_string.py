#我们将创建一个字符串，它包含文件中存储的所有数字，且没有任何空格
filename="pi_digits.txt"
with open(filename) as file_object:
#lines是一个列表 每行的字符都构成列表中的一个元素
	lines = file_object.readlines()

pi_string=''
for line in lines:
	pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))
