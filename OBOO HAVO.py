



import requests
from aiogram import Bot, Dispatcher,executor,types
url="https://goweather.herokuapp.com/weather/Tashkent"

response=requests.get(url)




API_TOKEN="5174843753:AAEhrQ9y8m4lzGr7OJ_bEF6Ak30O5NkurbI"
bot=Bot(API_TOKEN)
db=Dispatcher(bot)

@db.message_handler(commands=["start"])
async def start(message: types.Message):
        response=requests.get(url)
        obhavo = response.json()["temperature"]
        natija=response.json()['temperature']
        natija2=response.json()['wind']
        await message.answer("Bugun Toshkentda temprature{}.Shamol Tezligi{}".format(natija,natija2))
    
   
        
if __name__== "__main__":
    executor.start_polling(db)


