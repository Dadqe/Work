from plyer import notification
import time

print("До активации уведомления")

notification.notify( message='Первое сообщение',
    app_name='Название твоего приложения',
    # app_icon='sample.jpg',
    title='Заголовок', )

print("После активации уведомления")
time.sleep(3)
print("Поспал 3 секундочки")
notification.notify( message='Второе сообщение',
    app_name='Название твоего приложения',
    # app_icon='sample.jpg',
    title='Заголовок', )
print("Второй прошёл")