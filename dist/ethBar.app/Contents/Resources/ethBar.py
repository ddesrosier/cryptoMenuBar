from rumps import *
import time
import requests
import pprint as pp

@clicked('Update')
def update():
    try:
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
        data = r.json()
    except Exception as e:
        print('Error: {}'.format(e))
        # console.log(e)

    # print("%s | %s" % (data[0]['price_usd'],time.strftime("%H:%M:%S")))

    package = {
        # 'title': " " + data[0]['price_usd'],
        'title': 'ETH ' + data[0]['price_usd'],
        'hour': '1h ' + data[0]['percent_change_1h'],
        'day': '24h ' + data[0]['percent_change_24h'],
        'week': '7d ' + data[0]['percent_change_7d']
    }

    # Make these menu items with keys [1h, 24h, 7d] and just update them... dumbass

    # del app.menu['Changes']
    # app.menu['Changes'].clear()
    # app.menu['Changes'].update([package['hour'], package['day'], package['week']])
    app.title = package['title']

    # pp.pprint(app.menu['Changes'].items())
    return package


@rumps.timer(10)
def a(sender):
    temp = update()


######## Main Function

global_namespace_timer = rumps.Timer(a, 300)
app = rumps.App('cmc', menu=([
    'Changes',
    'Update',
    None
]))
app.run()
