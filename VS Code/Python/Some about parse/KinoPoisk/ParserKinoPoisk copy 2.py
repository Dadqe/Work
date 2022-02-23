import requests
from bs4 import BeautifulSoup
# импортировать рандом, оттуда randint(2, 6) или ещё там как-то, можно посмотреть в видосе предпоследнем

page = 4

url = "https://www.kinopoisk.ru/premiere/ru/2021/month/4/"

path = r"E:\Work\VS Code\Python\Some about parse\KinoPoisk\Data\\"
# Сайт оказался динамическим. Он подгружает фильмы по мере пролистывания страницы, сейчас на стадии поиска того, как эту задачу пройти...

# То, как получить всевсе фильмы с нужного месяца, через посыл метода post там по по 1-3 итерации (добавлении фильмов)....Нооо надо как-то пройти это, посмотреть, что будет происходить после post на несуществующую итерацию(там где пусто во вкладке preview, например, там вроде никакого когда не должно быть внутри) и обработать это в try&except что б он просто пропускал и переходил на следующий месяц...

# Нужно написать функцию по получению страниц в файлы в Data, мб можно как-то попробовать по относительному пути (надо изучить этот момент)

headers = {
    'authority': 'www.kinopoisk.ru',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Yandex";v="22"',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.kinopoisk.ru',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.kinopoisk.ru/premiere/ru/2021/month/4/',
    'accept-language': 'ru,en;q=0.9',
    'cookie': 'yuidss=4627193721567002613; mda_exp_enabled=1; yp=1583927268.oyu.4627193721567002613#1589631473.yu.4627193721567002613; yandexuid=4627193721567002613; _ym_d=1620049704; yandex_login=ru89514120022; PHPSESSID=fa9ea80188acf5780c415dfa86fa915a; yandex_gid=66; tc=462; uid=19866162; _csrf_csrf_token=NzbBa6JqNKG9MC5b8yIOkcpkFpP9rdbT2Dj7eMsmzzI; mobile=no; desktop_session_key=3af6a05294b7702318effa87c1c45aae719fc713dd02b884f14c034920b84cd8b90578cda886af6499be3833ae526efb9e3e30155468d60f2a3fcfc78847d96121a87f59cd0fc69eaca30525d848ba6c3d3a2140129840630f6c9ad47a2448e8; desktop_session_key.sig=Ot5JvVJarwIoHSUX0IXPpYEmrdA; crookie=inTnkE1jga4+JJ5F3JLW+T9uGr9mZIYoUa4bBtULUZWRASgbdyWCv9r/7M/rYH4mu1SqZ2asW83mA3SDsW2vLfvlXc0=; cmtchd=MTY0NTUyMDkzMjgyNg==; ys=udn.cDrQlNCw0L3QuNC7INCU0LXQvNC40L0%3D#c_chck.1056569115; i=0coswPKN/jjVy0aThZBtjl3GWkidCgRwhplBenWVgxE3Iw2NydCxhnSqfYnLc99j6Gy44WgEIxpNuIJjgbmqw8x5ko4=; _csrf=Bc2V1k8ITzpdb0e-GVi0LFB6; location=1; undefinedClosed=1; user_country=ru; yandex_plus_metrika_cookie=true; ya_sess_id=3:1645635598.5.1.1567002641398:iCz7Xg:50.1.2:1|406046668.33956442.2.2:33956442|516613772.68677907.2.2:76821356|30:205304.1688.Ui7FTRBasDWCmpiVb7S0Kd-2kU0; mda2_beacon=1645635598345; sso_status=sso.passport.yandex.ru:blocked',
}
data = {
    'token': 'NzbBa6JqNKG9MC5b8yIOkcpkFpP9rdbT2Dj7eMsmzzI',
    'page': '0',
    'ajax': 'true'
}
response = requests.post(url, headers=headers, data=data)
html = response.text

# Записываем полученную страницу в файл
with open(path + f"KinoPoiskKK{page}.html", "w", encoding="utf-8") as file:
    file.write(html)





