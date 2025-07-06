import aiohttp

class Message:
	def __init__(self, TOKEN, msg, session = None):
		self.url = f"https://api.telegram.org/bot{TOKEN}/"
		self.message_id = msg['message_id']
		self.chat_id = msg['chat']['id']
		self.text = msg.get('text', '')
		self.session = session

	async def send_message(self, text, chat_id, parse_mode=None, reply_to=None):
		payload = {
			"chat_id" : chat_id,
			"text": text,
			"disable_web_page_preview": False,
			"disable_notification": False,
		}
		if parse_mode:
			payload["parse_mode"] = parse_mode
		if parse_mode:
			payload["reply_to_message_id"] = reply_to
		headers = {
			"accept": "application/json",
			"content-type": "application/json"
		}

		async with self.session.post(self.url + "sendMessage", json=payload, headers=headers) as resp:
			response = await resp.json()
		if response['ok']:
			# message yuborildi
			pass
		else:
			print("xatooooooo")
			print(response)
			# message yuborishda xatolik yuz berdi
			pass

	async def reply(self, text, parse_mode=None, reply_to=None):
		await self.send_message(text, chat_id=self.chat_id, parse_mode=parse_mode, reply_to=reply_to)


