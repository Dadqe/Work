# import requests

# url = "https://browser-info.ru/"
# responce = requests.get(url)

# with open("test.html", "w", encoding="utf-8") as file:
#     file.write(responce.text)

with open("test.html", "r", encoding="utf-8") as file:
    
    first_string = file.readline()
    print(first_string)

# print(responce.text)
