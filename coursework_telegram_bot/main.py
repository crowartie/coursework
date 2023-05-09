from threading import Thread
from web_app import app
from bot import bot

def start_bot():
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print("Bot polling section error: " + str(e))
def start_web_app():
    app.run()

if __name__=="__main__":
    Thread(target=start_bot).start()
    Thread(target=start_web_app).start()