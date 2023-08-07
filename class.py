#学习类
class Dog():

	def __init__(self,name,age):
#创造新实例时，Python会自动调用)_init_()，其中self必不可少
#它是指向实例本身的引用
		self.name=name
		self.age=age
	def sit(self):
		print(self.name.title()+" is now sitting")
	def roll_over(self):
		print(self.name.title()+" rolled over!")

my_dog= Dog('james',6)

my_dog.sit()

my_dog.roll_over()

print(my_dog.name)
