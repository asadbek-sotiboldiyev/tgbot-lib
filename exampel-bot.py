from tgbot import App

TOKEN = "BOT_TOKEN"

app = App(TOKEN)

def start(message: Message):
	""" /start xabari kelganda """
	message.reply("Salom user")
	# message.send_message("Salom user", chat_id=message.chat_id)

def echo_for_other(message: Message):
	message.reply(message.text)

# Handler qo'shish
app.add_handler("/start", start)
# Hech bir handlerga mos tushmasa. TODO: Filter qo'shi kerak
app.handle_other(echo_for_other)

app.start_pulling(logging = True)
