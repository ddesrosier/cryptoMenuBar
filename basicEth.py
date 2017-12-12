import rumps
import time
from coinmarketcap import Market

market = Market()

def update():
    price = market.ticker('ethereum')[0]['price_usd']
    print("%s %f" % (time.strftime("%H:%M:%S", time.localtime()), price))
    return price


@rumps.timer(300)
def a(sender):
    app.title = update()


global_namespace_timer = rumps.Timer(a, 300)
app = rumps.App(market.ticker('ethereum')[0]['price_usd'], menu=())
app.run()
