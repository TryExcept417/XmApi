"""单例设计模式"""
 class DanLi(object):
 	"""单例设计模式，new方法负责创建空间"""
 	instance=None
 	init_flag=False
 	def __init__(self,name):
 		if DanLi.init_flag:
 			return
 		self.name=name
 		DanLi.init_flag=True
 		print("%s" % self.name)
 	def __new__(cls,*a,**b):
 		if cls.instance is None:
 			cls.instance=super().__new__(cls)
 		return cls.instance


 a=DanLi("liaolei")
 b=DanLi("liaoxiping")
 print(a)
 print(b)
