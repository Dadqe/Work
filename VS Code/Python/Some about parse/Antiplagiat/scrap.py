import requests

# cookies = {
#     'current-lang': 'ru-RU',
#     'domain-lang': 'ru-RU',
#     'cc.granted': '1',
#     '.AspNetCore.Culture.EP': 'c=ru|uic=ru',
#     'ASP.NET_SessionId': 'bbh00woqijyxkog4c1jje5tm',
#     '__RequestVerificationToken': '',
# }

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Language': 'ru,en;q=0.9',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     # Requests sorts cookies= alphabetically
#     # 'Cookie': 'current-lang=ru-RU; domain-lang=ru-RU; cc.granted=1; .AspNetCore.Culture.EP=c=ru|uic=ru; ASP.NET_SessionId=bbh00woqijyxkog4c1jje5tm; __RequestVerificationToken='',
#     'Pragma': 'no-cache',
#     'Referer': 'https://users.antiplagiat.ru/tariffs',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Yandex";v="22"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }, cookies=cookies, headers=headers

response = requests.get('https://users.antiplagiat.ru/tariffs')
# print(requests.utils.dict_from_cookiejar(response.cookies))
print(requests.utils.default_user_agent(response.headers))

# url = 'http://example.com/some/cookie/setting/url'
# resp = requests.get(url)
# # получение cookie, установленные сервером
# resp.cookies['example_cookie_name']
# # 'example_cookie_value'