import requests
import time
import random

# url = "https://www.b17.ru/media_load.php?id=2327"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
}

urls = ["https://www.b17.ru/media_load.php?id=2327", "https://www.b17.ru/media_load.php?id=2328", "https://www.b17.ru/media_load.php?id=2329", "https://www.b17.ru/media_load.php?id=2330", "https://www.b17.ru/media_load.php?id=2332"]

# Работает
for url in urls:
    responce = requests.get(url, headers=headers)
    with open(f"E:/Work/Podcasts/For mind/Tests/m/{url.split('=')[-1]}.mp3", "wb") as file:
        file.write(responce.content)
    print(f"{url.split('=')[-1]} Downloaded...")
    time.sleep(random.uniform(2, 4))