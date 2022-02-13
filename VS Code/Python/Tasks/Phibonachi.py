first_value = 0
second_value = 1
third_value = 0
sum_value = 0
# Надо создать функцию, которая при передаче значений будет считать число Фибоначи в трейтьей переменой. Потом проверять её на чётность и суммировать в четвёртую переменную все значения, которые прошли проверку на чётность, через def туда функцию бахнуть какую-нибудь и while для проверки на чётность и записи новых чисел в 4 переменную и задачи границы
# либо можно в одно while вписасть, увеличение значений на один шаг и всё и что б в этой функции всё делалось

while third_value <= 4000000:
    third_value = first_value + second_value
    if third_value % 2 == 0: 
        sum_value += third_value
    first_value = second_value
    second_value = third_value

print(sum_value)


second_value = first_value + second_value