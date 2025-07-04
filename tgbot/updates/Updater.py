import requests

class Updater:
    def __init__(self, TOKEN: str):
        self.last_update_id = None
        self.TOKEN = TOKEN

    def getUpdates(self) -> tuple:
        url = f"https://api.telegram.org/bot{self.TOKEN}/getUpdates"
        params = {
            "offset": self.last_update_id,
            "limit": 50,
            "timeout": 30
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        response = requests.post(url, json=params, headers=headers).json()
        ok = True
        if response['ok']:
            count = len(response['result'])
            if result := response['result']:
                self.last_update_id = result[0]['update_id']+1
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


