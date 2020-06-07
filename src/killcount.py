import requests
import const

def getKillCount(bot, update):
    msg = update.message.text
    boss = msg.rsplit(' ', 1)[1].title()
    username = str(msg[4:len(msg)-len(boss)])
    
    if(boss not in const.BOSSES):
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id, text="Boss does not exist")
        return

    r = requests.get('https://secure.runescape.com/m=hiscore_oldschool/a=12/index_lite.ws?player='+username)
    data = r.text
    numOfJunk = 35 
    idx = const.BOSSES.index(boss)
    counter = 0
    for line in data.splitlines():
        if(numOfJunk <= 0):
            if(counter == idx):
                killcount = line
            counter += 1
        numOfJunk -= 1

    killcount = killcount.rsplit(',', 1)[1]
    if(killcount == '-1'):
        killcount = "No killcount recorded"
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=killcount)