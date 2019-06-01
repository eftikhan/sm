import requests
from beem.steem import Steem
from beem.blockchain import Blockchain
from beem.account import Account
import ast
from datetime import datetime
from discord_webhook import DiscordWebhook
import os

"""
alric = 16
infarno = 5
zinter = 49
lyanna = 27
tyrus = 38
talia = 70
jarlax = 74
seachan = 71
foxwood = 72
kiara = 73
plado = 110
Valnamor = 111
Rennyn = 112
Peakrider = 113
Mancer = 109
Selenia = 56
62: Elven Cutthroat
64: Cocatrice
66: Enchanted Pixie
68: Magi Sphinx
9: Fire Demon
10: Serpent of the Flame
11: Elemental Phoenix
20: Mischievous Mermaid
21: Naga Warrior
22: Frost Giant
32: Swamp Thing
33: Spirit of the Forest
42: Defender of Truth
43: Air Elemental
44: Angel of Light
53: Dark Enchantress
54: Screaming Banshee
55: Lord of Darkness
57: Lightning Dragon
58: Chromatic Dragon
59: Gold Dragon
"""


di = {'16': .55,
       '5': .42,
      '49': .45,
      '27': .42,
      '38': .42,
      '70': .50,
      '71': .45,
      '72': .55,
      '73': .45,
      '74': .4,
      '62': .09,
      '64': .10,
      '66': .1,
      '68': 1,
      '9': .3,
      '10': .3,
      '11': 1.5,
      '20': .50,
      '21': .25,
      '22': 1.2,
      '32': .35,
      '33': 2.5,
      '42': .3,
      '43': .5,
      '44': 1.2,
      '53': .25,
      '54': .25,
      '55': 1.5,
      '57': 1.5,
      '58': 1.5,
      '59': 1.5}


dic = {'16': .7,
        '5': .50,
        '49': .7,
        '27': .56,
        '38': .68}

EF = os.environ.get('EF')

stm = Steem(node="https://api.steemitdev.com/", keys=EF)
acc = Account('eftikhan', steem_instance=stm)
bo = Blockchain(stm,'head')


print("started")
for detail in bo.stream(['custom_json']):
    try:
        if detail['id'] == 'sm_sell_cards':
            for i in ast.literal_eval(detail['json']):
                lin = requests.get("https://steemmonsters.com/cards/find?ids=" + i['cards'][0]).json()
                for ii in lin:
                    id = ii['market_id']
                    idd = str(ii['card_detail_id'])
                    price = float(ii['buy_price'])
                    if int(ii['edition']) == 1 and price <= di[idd]:
                        acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":eftikhan")
                        time = datetime.now()
                        webhook = DiscordWebhook(
                            url='https://discordapp.com/api/webhooks/582590527103434765/sAT1ZNhY8ZfmzN0uqnzCMMTfJghjH4y1DAatfIEXo4NrOj8zbFQ0XhXOlNTiR_B6Hc-x',
                            content='<@397972596207124480> dev time: {}'.format(time))
                        webhook.execute()

                    elif int(ii['edition']) == 0 and price <= dic[idd]:
                        acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":eftikhan")
                        time = datetime.now()
                        webhook = DiscordWebhook(
                            url='https://discordapp.com/api/webhooks/582590527103434765/sAT1ZNhY8ZfmzN0uqnzCMMTfJghjH4y1DAatfIEXo4NrOj8zbFQ0XhXOlNTiR_B6Hc-x',
                            content='<@397972596207124480> Dev time: {}'.format(time))
                        webhook.execute()
    except Exception as e:
        print("Error found: {}".format(e))
