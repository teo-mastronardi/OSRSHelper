from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from prices import *
from diaries import *
from stats import *
from killcount import *
import config

def main():
    updater = Updater(config.token_secret)
    dp = updater.dispatcher
    print("Launching...")
    dp.add_handler(CommandHandler('price',getPrice))
    dp.add_handler(CommandHandler('diary',getDiary))
    #dp.add_handler(CommandHandler('herb',setHerbTimer))
    dp.add_handler(CommandHandler('level',getSkillInfo))
    dp.add_handler(CommandHandler('kc',getKillCount))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()