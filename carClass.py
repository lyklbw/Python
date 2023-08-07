class Car():
	def __init__(self,name,age,nation):
		self.name=name
		self.age=age
		self.nation=nation
		self.odometer=0;
	def print_function(self):
		long_name=(self.name + " driven for "+self.age + " years"+" from "+ self.nation)
		print(long_name)
	def updata_odometer(self,addition):
		if self.odometer<=addition:
			self.odometer=addition
		else:
			print("You can not roll back an odometer")
	def increment_odometer(self,add):
		self.odometer+=add
	def show_odometer(self):
		print(self.odometer)
#python不能整型数连接字符串要用 str()转换
#将属性和方法整合成一个类 再将这个类变成呢个一个属性
class Battery():
		def __init__(self,battery_size=100):
			self.battery_size=battery_size
			self.range=2*self.battery_size+30
		def describe_battery(self):
			print("battery left: "+str(self.battery_size))
		def change_batterysize(self,value):
			self.battery_size+=value
		def get_range(self):
			self.range=self.battery_size*2+30
		def describe_range(self):
			print("剩余公里数： "+str(self.range))
#继承
class electricCar(Car):
	"""电动汽车的特别之处"""
	def __init__(self,name,age,nation):
		#super代表父类
		super().__init__(name,age,nation)
		self.battery=Battery()
mytesla=electricCar("tesla","3","the US")
mytesla.battery.describe_battery()
mile=input("输入电池电量变化值(正为充电，负为放电)\n")
mytesla.battery.change_batterysize(int(mile))
mytesla.battery.describe_battery()
mytesla.battery.get_range()
mytesla.battery.describe_range()




