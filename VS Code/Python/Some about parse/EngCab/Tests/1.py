data = []
service = "Услуга"
date_of_creation = "Тут Дата" # Дата создания заявки
description = "Описание" # Описание
completion_deadline = "Крайний срок" # Крайний срок завершения
sono = "СОНО" # СОНО

data.extend(["[+]", f"{date_of_creation} - {completion_deadline}", service, description, sono, "-----"])

with open('data4.txt', "w", encoding='utf-8') as file:
    file.writelines([f"{line}\n" for line in data])