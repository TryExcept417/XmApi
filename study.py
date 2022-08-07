	
# for  i in range(1,10):
# 	j=int((str(i)*6))
# 	for n in range(1,10):
# 		for m in range(10000,99999):
# 			if j/n==m and str(m)[:2]==str(m)[-2:]:
# 				print(j,n,m)


# for i in range(1, 10, +1):
#     for j in range(999999, 100000, -1):
#         strs = str(j)
#         if strs[0] == strs[1] and strs[2] == strs[3] and strs[3] == strs[4] and strs[4] == strs[5]:
#             if len(str(int(j/i))) == 5:
#                 strs = str(int(j / i))
#                 if strs[0] == strs[3] and strs[1] == strs[4] and strs[2] != strs[0] and strs[2] !=strs[1]:
#                     if int(str(j / i).split(".")[1]) <= 0:
#                         print(str(j)+ "/" + str(i) + "=" +str(int(j/i)))

# class Dog(object):
# 	"""docstring for Dog"""
# 	def __init__(self, name):
# 		self.name = name
# 	def game(self):
# 		print("{0}在快乐的玩耍".format(self.name))
		
# class XiaoTianDog(Dog):
# 	"""docstring for XiaoTianDog"""
	
		
# 	def game(self):
# 		print("{0}在天上快乐的玩耍".format(self.name))

# class Person(object):
# 	"""docstring for Person"""
# 	def __init__(self, name):
		
# 		self.name = name
# 	def playwithdog(self,dog):
# 		print("{}与{}一起快乐的玩耍".format(self.name,dog.name))
# 		dog.game()
		
# xiaotian=XiaoTianDog("xiaotianquan")
# xiaoming=Person("xiaoming")
# xiaoming.playwithdog(xiaotian)

# class  Dog(object):
# 	COUNT=0
# 	def __init__(self,name):
# 		self.name=name
# 		Dog.COUNT+=1
# 		print(Dog.COUNT)

# a0=Dog("XIAOPANG")
# a1=Dog("XIAOANG")
# a2=Dog("XIAOPAN")
# print(a0.COUNT,a1.COUNT,a2.COUNT,Dog.C)


# class Game(object):
# 	"""docstring for Game"""
# 	top_score=100
# 	def __init__(self, name):
# 		self.name = name
# 	"""静态方法"""
# 	@staticmethod
# 	def show_help():
# 		print("这个是帮助信息")
# 	"""类属性，类方法"""
# 	@classmethod
# 	def show_top_score(cls):
# 		print(cls.top_score)
# 		print(Game.top_score)
# 	def wan_jia(self):
# 		print("%s玩游戏" %self.name)
# """静态方法调用不需要实例化"""
# Game.show_help()
# a=Game("liaolei")
# a.show_top_score()
# a.wan_jia()
		

"""单例设计模式"""
# class DanLi(object):
# 	"""单例设计模式，new方法负责创建空间"""
# 	instance=None
# 	init_flag=False
# 	def __init__(self,name):
# 		if DanLi.init_flag:
# 			return
# 		self.name=name
# 		DanLi.init_flag=True
# 		print("%s" % self.name)
# 	def __new__(cls,*a,**b):
# 		if cls.instance is None:
# 			cls.instance=super().__new__(cls)
# 		return cls.instance


# a=DanLi("liaolei")
# b=DanLi("liaoxiping")
# print(a)
# print(b)

print(12*16)

