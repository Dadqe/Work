from bs4 import BeautifulSoup

received = 0
spent = 0

with open(r"E:/Work/VS Code/Python/Some about parse/Steam/Аккаунт elianorchick.html", "r", encoding='utf-8') as file:
    source = file.read()
# print(source)

soup = BeautifulSoup(source, 'lxml')
count_minus = 0
all_change = soup.find_all('td', class_='wht_wallet_change wallet_column')
for num in all_change:
    
    numeric = num.text.split(' ')[0]
    print(numeric)
    if '+' in numeric:
        received += float(numeric.split("+")[1].replace(',', '.'))
    elif '-' in numeric:
        count_minus += 1
        spent += float(numeric.split("-")[1].replace(',', '.'))
print(f"Received = {received} and Spent = {spent}", count_minus)
    



# <td class="wht_wallet_change wallet_column" data-tooltip-html="<div class='wallet_tip'>
#     <table>
#         <tr>
#             <td>Предыдущий баланс кошелька:</td>
#             <td style='text-align: right'>2693,50 pуб.</td>
#         <tr>
#         <td>Изменить:</td>
#         <td style='text-align: right'>+21,64 pуб.</td>
#         <tr>
#             <td>Новый баланс кошелька:</td>
#             <td style='text-align: right'>2715,14 pуб.</td>
#     </table></div>">
#     +21,64 pуб.
# </td>