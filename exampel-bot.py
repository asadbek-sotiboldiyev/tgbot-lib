from tgbot import App
from tgbot.models import Message

TOKEN = "BOT_TOKEN"

app = App(TOKEN)

async def start(message: Message):
	""" /start xabari kelganda """
	await message.reply("Salom, botga xush kelibsiz")
	await message.reply("text1")
	await message.reply("tex2")
	await message.reply("tex3")
	await message.reply("tex4")
	# message.send_message("Salom user", chat_id=message.chat_id)

async def echo_for_other(message: Message):
	await message.reply(message.text)

# Handler qo'shish
app.add_handler("/start", start)

app.start_pulling(logging = True)
