

def count_letter(example_list, letter):
    count = 0
    for words in example_list:
        if letter in words:
            count += 1
    return count

test_list = []
run = True
while run:
    slovo = input('Введите слово: ')
    test_list.append(slovo)
    question = input('Хотите добавить ещё слово? ').lower()
    while question == 'да' or question == 'y' or question == 'yes':
        slovo = input('Введите слово: ')
        test_list.append(slovo)
        question = input('Хотите добавить ещё слово? ').lower()
    else:
        run = False
        

# example_list = ['python', 'c++', '', 'scala', 'java']
letter = 'c'
print(count_letter(test_list, letter))