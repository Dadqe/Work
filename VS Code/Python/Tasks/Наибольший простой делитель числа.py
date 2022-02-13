# finish_sum = 0
import math

list = []
n = 600851475143
for numbers in range (2, int(math.sqrt(n))):
    if n % numbers == 0:
        check_number = numbers
        complited = 0
        for numbers in range (2, check_number):
            if check_number % numbers == 0:
                complited += 1
        if complited == 0:
            list += [check_number]
        # if check_number % 2 != 0 or check_number % 3 != 0:
        #     list += [check_number]
print(max(list))



























# От Сани на JS
# function simpleDel() {
#   let startChislo = 600851475143;
#   Logger.log("Простые делители числа " + startChislo + ": ");
#   for (let iskomoe = 2; iskomoe < Math.sqrt(startChislo); iskomoe++) {
#     if (startChislo % iskomoe == 0) {
#       let sum = 0;
#       for (let neDel = 2; neDel < iskomoe; neDel++) {
#         if (iskomoe % neDel == 0) {
#           sum = sum + 1;
#         }
#       }
#       if (sum == 0) {
#         Logger.log(iskomoe + " ");
#       }
#     }
#   }
# }


# def delit(a) :
#     res = []
#     i = 2
# # цикл до квадратного корня из "а"
# # больше этого без остатка не делится, если только ...
# # (об этом ниже)
#     while i * i < a + 1 :
# # если при делении остаток = 0, то добавляем "i" в список
#         if a % i == 0 :
#             res.append(i)
# # теперь делим исходное число на "i", пока не появится остаток
#             while a % i == 0 :
#                 a //= i
# # берем следующее "i"
#         i += 1
# # если в конце "а" не равно единице, то значит остался один(!)
# # делитель, больший кв. корня из исходного "а"
# # добавляем в список
#     if a != 1 :
#         res.append(a)
#     return res 
    
# print(delit(int(input())))