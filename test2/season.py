import datetime

# https://ja.wikipedia.org/wiki/%E5%AD%A3%E7%AF%80#:~:text=%E6%97%A5%E6%9C%AC%E3%81%AE%E6%B0%97%E8%B1%A1%E5%BA%81%E3%81%AF%E3%80%81%E5%AD%A3%E7%AF%80,%E5%85%AC%E5%BC%8F%E3%81%AB%E5%AE%9A%E3%82%81%E3%81%A6%E3%81%84%E3%82%8B%E3%80%82
# 気象庁による月ごとの季節を参照
season = {'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11], 'winter': [1, 2, 12]}

today = datetime.date.today()
print('Content-Type: text/plain')
print()
if today.month in season['spring']:
    print('Are you enjoying the spring?')
elif today.month in season['summer']:
    print('Are you enjoying the summer?')
elif today.month in season['autumn']:
    print('Are you enjoying the autumn?')
else:
    print('Are you enjoying the winter?')