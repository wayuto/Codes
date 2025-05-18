import requests
import json

print('你好,我是PyAI')
while True:
    u = input('我: ')
    text = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg='+u+'').text.encode()
    rew = json.loads(text)
    print('PyAI: '+rew['content'])
    print('http://api.qingyunke.com/')