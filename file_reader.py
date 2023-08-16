#写一个open就可以了，python会自己判断close的时机
#文件读取
with open('.\\pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
#逐行读取
filename='pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
#删除空白行，rstrip删除tab space etc
print("创建一个包含文件各行内容的列表")
with open(filename) as file_object:
	lines=file_object.readlines()#从文件中读取一行,在with代码块之外 依旧就可以使用
for line in lines:
	print(line.rstrip())
