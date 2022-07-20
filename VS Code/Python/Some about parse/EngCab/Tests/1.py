import time

def gathering_new_bid(source):
    print(source)

def main():
    while True:
        gathering_new_bid(source=Login)
        time.sleep(10)

if __name__ == "__main__":
    try:
        Login = input('Введи логин: ')
        # Password = getpass.getpass('Введи пароль: ')
        # s = requests.Session()
        # s.post(url, data=auth, headers=headers, timeout=(5))
    except Exception as e:
        print("Something gone wrong...")
        print(e)
        print("Ты где-то накосячил с логином или паролем\nStart the program again")
        
    while True:
        try:
            main()
        except Exception as e:
            print("Something gone wrong...")
            print(e)
            print("The program will start in 1 minute")
            time.sleep(60)
