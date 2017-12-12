import rumps
import time
from coinmarketcap import Market

market = Market()

def update():
    price = market.ticker('ethereum')[0]['price_usd']
    print("%s | %s" % (price,time.strftime("%H:%M:%S")))

    return "Ξ " + price


@rumps.timer(10)
def a(sender):
    app.title = update()


global_namespace_timer = rumps.Timer(a, 10)
app = rumps.App('cmc', menu=())
app.run()
