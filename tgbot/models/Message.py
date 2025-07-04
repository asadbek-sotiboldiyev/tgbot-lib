import requests

class Message:
	def __init__(self, TOKEN, msg):
		self.url = f"https://api.telegram.org/bot{TOKEN}/"
		self.message_id = msg['message_id']
		self.chat_id = msg['chat']['id']
		self.text = msg.get('text', '')

	def send_message(self, text, chat_id, parse_mode=None, reply_to=None):
		payload = {
			"chat_id" : chat_id,
			"text": text,
			"disable_web_page_preview": False,
			"disable_notification": False,
			"reply_to_message_id": reply_to
		}
		if parse_mode:
			payload["parse_mode"] = parse_mode,
		headers = {
			"accept": "application/json",
			"content-type": "application/json"
		}

		response = requests.post(self.url + "sendMessage", json=payload, headers=headers).json()
		if response['ok']:
			# message yuborild
			print(response['result'])
		else:
			print("xatooooooo")
			print(response)
			# message yuborishda xatolik yuz berdi
			pass

	def reply(self, text, parse_mode=None, reply_to=None):
		self.send_message(text, chat_id=self.chat_id, parse_mode=parse_mode, reply_to=reply_to)


