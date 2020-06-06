from OSRS_Hiscores import Hiscores
import re

def getSkillInfo(bot, update):
    #print level and XP and Xp till next..why not
    #stats = "Could not find info on that player"
    msg = update.message.text
    skill = msg.rsplit(' ', 1)[1]
    username = str(msg[7:len(msg)-len(skill)])
    user = Hiscores(username, 'N')

    if(skill == "total"):
        stats = getTotalLevel(user)
    else: 
        stats = str(user.stats[skill]['level'])
        stats += "\nXP to next level: "
        stats += str(user.stats[skill]['exp_to_next_level'])
        
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=stats)

def getTotalLevel(user):
    return user.skill('total')

