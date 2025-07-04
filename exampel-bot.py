from tgbot import App

TOKEN = "BOT_TOKEN"

app = App(TOKEN)

app.start_pulling(logging = True)
