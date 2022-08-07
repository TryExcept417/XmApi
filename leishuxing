class Game(object):
	top_score=0
	def __init__(self,name):
		self.name=name
	@staticmethod
	def show_help():
		print("这个是帮助信息")
	@classmethod
	def show_top_score(cls):
		print("历史最高分是%s" %cls.top_score)
	def start_game(self):
		print("{}开始玩游戏".format(self.name))

Game.show_help()
Game.show_top_score()
liaolei=Game("liaolei")
liaolei.start_game()