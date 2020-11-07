from .api import TraderApi as Trader


client = Trader('_b_=; _e_="{\\\\"id\\\\":\\\\"8B6E72EB4E1FDDDD\\\\",\\\\"_e_\\\\":\\\\"653732DF6C3858D7ABF14C86E611846D\\\\",\\\\"_sign_\\\\":\\\\"27630C84\\\\"}"; ssid="5S3ASI2n5Hk="; _s_="{\\\\"id\\\\":\\\\"8B6E72EB4E1FDDDD\\\\",\\\\"_e_\\\\":\\\\"653732DF6C3858D7ABF14C86E611846D\\\\",\\\\"_sign_\\\\":\\\\"14D8CA0A\\\\"}"; deviceInfo=%7B%22macAddress%22%3A%22%22%2C%22systemName%22%3A%22IOS%22%2C%22model%22%3A%22%22%2C%22appVerion%22%3A%22%22%2C%22localizedModel%22%3A%22%22%2C%22uuid%22%3A%22%22%2C%22systemVersion%22%3A%226.0%22%2C%22phoneNum%22%3A15001332302%2C%22ipAdress%22%3A%22%22%2C%22idfa%22%3A%22%22%2C%22imsi%22%3A%22%22%2C%22iccid%22%3A%22%22%2C%22rmpn%22%3A%22%22%2C%22dev%22%3A%22HB-H5%22%7D')
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
