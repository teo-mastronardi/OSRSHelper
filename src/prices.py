import requests

def getPrice(bot, update):
    price =  "Did not find such item"
    item = update.message.text[7:]
    item = item.capitalize()
    r = requests.get('https://rsbuddy.com/exchange/summary.json')
    jsonData = r.json()

    for majorkey, subdict in jsonData.items():
        for subkey, value in subdict.items():
            if(value == item):
                itemId = subdict.get("id")
                price = format(subdict.get("overall_average"), ",") +"gp"

    chat_id = update.message.chat_id
    changes = getPriceChanges(itemId)
    price += "\n" + changes
    bot.send_message(chat_id=chat_id, text=price)
    #bot.send_message(chat_id=chat_id, text=changes)

def getPriceChanges(itemId):
    r=requests.get('http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='+str(itemId))
    jsonData = r.json()
    for majorkey, subdict in jsonData.items():
        changes = "Today's price change: " + subdict.get("today").get("price")
        changes +="\nThis months's change: " + subdict.get("day30").get("change")
        changes +="\nThree months change: " + subdict.get("day90").get("change")
        changes += "\nSix months change: " + subdict.get("day180").get("change")
        break
    return changes