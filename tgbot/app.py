import requests
import aiohttp
import asyncio
from .updates import *
from .models import Message

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

		self.handles = dict()

	def getMe(self):
		print("STARTING: Bot tekshirilyapti...")
		bot = requests.get(self.url + "/getMe")
		return bot.json()['ok']
	
	def start_pulling(self, logging=False):
		asyncio.run(self.pulling(logging=logging))

	async def pulling(self, logging=False):
		"""
		Updatelarni olishni boshlash.
		logging (bool): default=False
		"""
		last_update_id = None
		async with aiohttp.ClientSession() as session:
			if self.ok:
				updater = Updater(self.TOKEN)
				running = True
				while running:
					if logging:
						print("INFO: Update lar olinmoqda...")

					running, count, updates = await updater.getUpdates(session, offset=last_update_id)

					if logging:
						if count == 0:
							print("UPDATE: Yangi updatelar yo'q")
						else:
							print(f"UPDATE: {count} ta yangi updatelar olindi.")

					for update in updates:
						if logging:
							print("NEW UPDATE:", updater.short_result(update))
						message = Message(self.TOKEN, update['message'])
						if msg_fn := self.handles.get(message.text, False):
							await msg_fn(message)
						else:
							# Handlelarga to'g'ri kelmagan xabar e'tiborsiz qoladi
							pass
						last_update_id = update['update_id'] + 1
			else:
				print("ERROR: TOKEN noto'g'ri. Qayta tekshiring.")

	def add_handler(self, msg, fn):
		self.handles[msg] = fn

