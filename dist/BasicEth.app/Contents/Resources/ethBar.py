from rumps import *
import time
import requests

def update():
    try:
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
        data = r.json()
    except Exception as e:
        print("Error: {}".format(e))
        # console.log(e)

    # print("%s | %s" % (data[0]['price_usd'],time.strftime("%H:%M:%S")))
    # print(data)
    package = {
        # 'title': " " + data[0]['price_usd'],
        'title': "ETH " + data[0]['price_usd'],
        'hour': "1h " + data[0]['percent_change_1h'],
        'day': "24h " + data[0]['percent_change_24h'],
        'week': "7d " + data[0]['percent_change_7d']
    }
    return package


@rumps.timer(10)
def a(sender):
    package = update()
    # print(package['title'])
    # print(app.menu)
    app.title = package['title']

######## Main Function

global_namespace_timer = rumps.Timer(a, 300)
app = rumps.App('cmc', menu=())
app.menu = [
    '1h',
    '24h',
    '7d',
    None
]
app.run()
