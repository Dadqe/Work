import requests
from bs4 import BeautifulSoup
import sys
sys.path.insert(0, 'C:/Tokens/KinoPoisk/')
from Token import token

month = 12
url = f"https://www.kinopoisk.ru/premiere/ru/2021/month/{month}/"

# path = r"E:\Work\VS Code\Python\Some about parse\KinoPoisk\Data\\" # PC
path = r"C:\Work\VS Code\Python\Some about parse\KinoPoisk\Data\\" # Laptop


# headers = {
#     'authority': 'www.kinopoisk.ru',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Yandex";v="22"',
#     'accept': '*/*',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'x-requested-with': 'XMLHttpRequest',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36',
#     'sec-ch-ua-platform': '"Windows"',
#     'origin': 'https://www.kinopoisk.ru',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.kinopoisk.ru/premiere/ru/2021/month/4/',
#     'accept-language': 'ru,en;q=0.9',
#     'cookie': 'yuidss=4627193721567002613; mda_exp_enabled=1; yp=1583927268.oyu.4627193721567002613#1589631473.yu.4627193721567002613; yandexuid=4627193721567002613; _ym_d=1620049704; yandex_login=ru89514120022; PHPSESSID=fa9ea80188acf5780c415dfa86fa915a; yandex_gid=66; tc=462; uid=19866162; _csrf_csrf_token=NzbBa6JqNKG9MC5b8yIOkcpkFpP9rdbT2Dj7eMsmzzI; mobile=no; desktop_session_key=3af6a05294b7702318effa87c1c45aae719fc713dd02b884f14c034920b84cd8b90578cda886af6499be3833ae526efb9e3e30155468d60f2a3fcfc78847d96121a87f59cd0fc69eaca30525d848ba6c3d3a2140129840630f6c9ad47a2448e8; desktop_session_key.sig=Ot5JvVJarwIoHSUX0IXPpYEmrdA; crookie=inTnkE1jga4+JJ5F3JLW+T9uGr9mZIYoUa4bBtULUZWRASgbdyWCv9r/7M/rYH4mu1SqZ2asW83mA3SDsW2vLfvlXc0=; cmtchd=MTY0NTUyMDkzMjgyNg==; ys=udn.cDrQlNCw0L3QuNC7INCU0LXQvNC40L0%3D#c_chck.1056569115; i=0coswPKN/jjVy0aThZBtjl3GWkidCgRwhplBenWVgxE3Iw2NydCxhnSqfYnLc99j6Gy44WgEIxpNuIJjgbmqw8x5ko4=; _csrf=Bc2V1k8ITzpdb0e-GVi0LFB6; location=1; undefinedClosed=1; user_country=ru; yandex_plus_metrika_cookie=true; ya_sess_id=3:1645635598.5.1.1567002641398:iCz7Xg:50.1.2:1|406046668.33956442.2.2:33956442|516613772.68677907.2.2:76821356|30:205304.1688.Ui7FTRBasDWCmpiVb7S0Kd-2kU0; mda2_beacon=1645635598345; sso_status=sso.passport.yandex.ru:blocked',
# } # PC
headers = {
    'authority': 'www.kinopoisk.ru',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Yandex";v="22"',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.850 Yowser/2.5 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.kinopoisk.ru',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.kinopoisk.ru/premiere/ru/2021/month/4/',
    'accept-language': 'ru,en;q=0.9',
    'cookie': 'gdpr=0; _ym_uid=1625650459749674570; yandexuid=2023660621620469477; yandex_login=ru89514120022; mda_exp_enabled=1; PHPSESSID=b8ff1520be1b9a27b4f6ce43db460a0e; user_country=ru; yandex_gid=65; tc=452; _csrf_csrf_token=Mhm6ydHShJOsJijMCcGOo_-DKDbST9_S2wNVO4HuDsg; mobile=no; desktop_session_key=65ade09596f568260f2e611e34940fcb092b96fad7995641a99bdc621d9c097df4a48997b33aa2baf80ec52def52eebba675976d8d8b4f16dec0370cde663c34385d269e1c163b6790f6337e844de645340f63527e6dcaae419fea6e151ba459; desktop_session_key.sig=rcj7fYuAD2OWiA4WyV4SVadaYPE; _ym_isad=1; yuidss=2023660621620469477; yp=1645758898.yu.2023660621620469477; ymex=1648264498.oyu.2023660621620469477; yandex_plus_metrika_cookie=true; _ym_visorc=b; ya_sess_id=3:1645672499.5.1.1624601833099:3G07sA:48.1.2:1|406046668.11.2.2:11|516613772.11078760.2.2:15379303|30:205315.614465.M3qdaYoiS2vrWxMi0uTInZaRmGQ; ys=udn.cDrQlNCw0L3QuNC7INCU0LXQvNC40L0%3D#c_chck.2552914671; i=0tjJ3zZcZtYNBKV3XpV4vtaeI/m99qOlBfHPTPOKAGmnghBqol86+/BNdlWLouyvF0LiRzPq3oL9DXRmBOpxbqOCGaY=; mda2_beacon=1645672499023; cmtchd=MTY0NTY3MjUwNjU5Nw==; crookie=/vr1iEVA2ew1TY/s9IUgaXo+MbaV5uv+npV6BwWBydFMPdAiOgtcGMUZ6J+1LMTRMSZZcoTLwgHe1+VFKV1tv96LhB8=; sso_status=sso.passport.yandex.ru:synchronized; mda_reloaded_page=1; location=1; uid=19866162; _ym_d=1645672508',
} # Laptop

page = 0
html = True

# Запись всех копий страниц с нужного месяца (со всеми фильмами)
while html:
    data = {
        'token': 'token',
        'page': page,
        'ajax': 'true'
    }
    
    page += 1
    response = requests.post(url, headers=headers, data=data)
    html = response.text
    if bool(html) == True:
        with open(path + f"KinoPoisk2021_month{month}#{data.get('page')}.html", "w", encoding="utf-8") as file:
            file.write(html)
        print(f"Код с {data['page']}-й части страницы {month} сохранён")
    else:
        print(f"Нет {data['page']}-й части на странице {month}")
        html = False


