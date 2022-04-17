import requests


def inform_me(price):
    API_Key = '4D596448442B5242327971633873314C6B6F6F2F34413D3D'
    url = 'https://api.kavenegar.com/v1/%s/sms/send.json' % API_Key
    payload = {'reseptor': '09121234567',
               'message': 'Bitcoin Price is Low! Bitcoin Price is as low as %i' % price}
    response = requests.post(url, data=payload)
    print response   #for test
    
    
my_good_price = 6500

response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD',
           proxies={'https': 'socks5://127.0.0.1:1080'})


price = float(response.json()['data']['amount'])

if (price < my_good_price):
    inform_me(price)
