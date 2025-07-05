class Updater:
    def __init__(self, TOKEN: str):
        self.TOKEN = TOKEN

    async def getUpdates(self, session, offset) -> tuple:
        url = f"https://api.telegram.org/bot{self.TOKEN}/getUpdates"
        params = {
            "limit": 50,
            "timeout": 30
        }
        if offset is not None:
            params['offset'] = offset
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        async with session.get(url, params=params, headers=headers) as response:
            try:
                response = await response.json()
            except Exception as e:
                print("ERROR: JSON decode xatolik:", e)
                return (False, 0, [])

            ok = True
            if response['ok']:
                count = len(response['result'])
            else:
                ok = False
                print("ERROR: Updatelarni olishda xatolik.")
            return (ok, count, response['result'])
    
    def short_result(self, response):
        result = {
            "from_id" : response['message']['from']['id'],
            "chat_id" : response['message']['chat']['id'],
            "chat_type" : response['message']['chat']['type'],
            "text" : response['message'].get("text", "")
        }
        return result


