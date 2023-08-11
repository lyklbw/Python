filename="programming.txt"
with open (filename ,"a") as file_object:
	file_object.write("I love programming")
#注意："w"写入是要小心，如果指定文件存在，pyhton会清空文件内容 "r" only read "a" add
#如果没有指定文件，python会自己创建，不用担心丢失数据

#write不会在文本末尾自动加换行符



