import requests
from beem.steem import Steem
from beem.blockchain import Blockchain
from beem.account import Account
import ast
import os
from threading import Thread

SV = os.environ.get('SV')

def anyx():
    di = {'16': .55,
          '15': .03,
          '5': .42,
          '49': .45,
          '27': .42,
          '38': .42,
          '70': .50,
          '71': .45,
          '72': .55,
          '73': .45,
          '74': .4, }

    dic = {'16': .7,
           '5': .50,
           '49': .7,
           '27': .56,
           '38': .68}

    stm = Steem(node="https://anyx.io", keys=SV)
    acc = Account('sourovafrin', steem_instance=stm)
    bo = Blockchain(stm, 'head')

    print("started anyx")
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
                            acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":sourovafrin")

                        elif int(ii['edition']) == 0 and price <= dic[idd]:
                            acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":sourovafrin")
        except Exception as e:
            print("Error found anyx: {}".format(e))


def minnow():
    di = {'16': .55,
          '15': .03,
          '5': .42,
          '49': .45,
          '27': .42,
          '38': .42,
          '70': .50,
          '71': .45,
          '72': .55,
          '73': .45,
          '74': .4, }

    dic = {'16': .7,
           '5': .50,
           '49': .7,
           '27': .56,
           '38': .68}

    stm = Steem(node="https://steemd.minnowsupportproject.org/", keys=SV)
    acc = Account('sourovafrin', steem_instance=stm)
    bo = Blockchain(stm, 'head')

    print("started minnow")
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
                            acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":sourovafrin")

                        elif int(ii['edition']) == 0 and price <= dic[idd]:
                            acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":sourovafrin")
        except Exception as e:
            print("Error found minnow: {}".format(e))


def stee():
    di = {'16': .55,
          '15': .03,
          '5': .42,
          '49': .45,
          '27': .42,
          '38': .42,
          '70': .50,
          '71': .45,
          '72': .55,
          '73': .45,
          '74': .4, }

    dic = {'16': .7,
           '5': .50,
           '49': .7,
           '27': .56,
           '38': .68}

    stm = Steem(node="https://api.steemit.com", keys=SV)
    acc = Account('sourovafrin', steem_instance=stm)
    bo = Blockchain(stm, 'head')

    print("started steem")
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
                            acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":sourovafrin")

                        elif int(ii['edition']) == 0 and price <= dic[idd]:
                            acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":sourovafrin")
        except Exception as e:
            print("Error found stee: {}".format(e))


def use():
    di = di = {'16': .55,
          '15': .03,
          '5': .42,
          '49': .45,
          '27': .42,
          '38': .42,
          '70': .50,
          '71': .45,
          '72': .55,
          '73': .45,
          '74': .4, }

    dic = {'16': .7,
           '5': .50,
           '49': .7,
           '27': .56,
           '38': .68}

    stm = Steem(node="https://api.steemit.com", keys=SV)
    acc = Account('sourovafrin', steem_instance=stm)
    bo = Blockchain(stm, 'head')

    print("started use")
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
                            acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":sourovafrin")

                        elif int(ii['edition']) == 0 and price <= dic[idd]:
                            acc.transfer('svirus', 2, 'SBD', "sm_market_purchase:" + id + ":sourovafrin")
        except Exception as e:
            print("Error found use: {}".format(e))


if __name__ == '__main__':
    Thread(target=anyx, args=()).start()
    Thread(target=minnow, args=()).start()
    Thread(target=stee, args=()).start()
    Thread(target=use, args=()).start()
