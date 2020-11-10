from .api import TraderApi as Trader
from .cookie import get_cookie

cookies = get_cookie()

cookies_str = ''

for item in cookies:
    cookies_str += item['name'] + '=' + item['value'] + '; '

cookies_str = cookies_str.rstrip('; ')
client = Trader(cookies_str)
ret = client.entrust(
"宁波银行",
'002142',
'SZ',
4,
35.5,
100,
2
)

print(ret)
print(ret.text)
