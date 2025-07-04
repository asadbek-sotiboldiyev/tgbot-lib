import requests
from .updates import *

class App:
	"""
	Asosiy app klassi.
	"""
	def __init__(self, TOKEN):
		"""
		TOKEN (str): @botfather dan olgan tokeningiz 
		"""
		self.TOKEN = TOKEN
		self.url = f"https://api.telegram.org/bot{TOKEN}"
		self.ok = self.getMe()

	def getMe(self):
		print("STARTING: Bot tekshirilyapti...")
		bot = requests.get(self.url + "/getMe")
		return bot.json()['ok']

	def start_pulling(self, logging=False):
		if self.ok:
			updater = Updater(self.TOKEN)
			running = True
			while running:
				if logging:
					print("INFO: Update lar olinmoqda...")
				running, count, updates = updater.getUpdates()
				if logging:
					if count == 0:
						print("UPDATE: Yangi updatelar yo'q")
					else:
						print(f"UPDATE: {count} ta yangi updatelar olindi.")
					for update in updates:
						print("NEW UPDATE:", updater.short_result(update))
		else:
			print("ERROR: TOKEN noto'g'ri. Qayta tekshiring.")

