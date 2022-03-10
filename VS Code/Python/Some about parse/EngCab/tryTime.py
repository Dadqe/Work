import datetime
import time

#  У меня есть время заявки. Я отнимаю 5 минут от текущего времени и надо просто математически сравнить через два оператора, входит ли в этот промежуток времени данные о datetime заявки и получить на выходе True or False


# now = datetime.datetime(2022, 3, 10, 9, 31, 0)
# z = datetime.datetime(2022, 3, 10, 9, 28, 0)
# delta = now - datetime.timedelta(minutes=5)
# check = delta < z < now

# now = datetime.datetime.now().replace(microsecond=0) #test
print(now)
# print(z)
# print(delta)
# print(check)






# a = datetime.datetime.now()
# time.sleep(5)
# b = datetime.datetime.now()

# print(a)
# print(b)
# print((b-a).seconds)



# today = datetime.datetime.today()
# delta_days = datetime.timedelta(days=14)
# past_date = today - delta_days

# # past_date = datetime.datetime.today() - datetime.timedelta(days=14)
# print(past_date)
# print(type(today))
# print(type(delta_days))
# print(type(past_date))