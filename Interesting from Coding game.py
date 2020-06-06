def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    return text[(text.find(begin)+len(begin)) if text.find(begin) != -1 else 0: (text.find(end)) if text.find(end) != -1 else len(text)]


print(between_markers('What is >apple<', '>', '<'))
print(between_markers('No[/b] hi', '[b]', '[/b]')) # 'No', 'No opened'
print(between_markers('No [b]hi', '[b]', '[/b]')) # 'hi', 'No close'
print(between_markers('No hi', '[b]', '[/b]')) # 'No hi', 'No markers at all'

def is_stressful(subj):
    """
        recognize stressful subject
    """

#    >> > foo = 'mppmt' >> > ''.join(sorted(set(foo), key=foo.index))
#    'mpt'

    try:

        if subj.isupper():
            return True
        if subj[-3:] == '!!!':
            return True

        subj = subj.split()
        for subject in subj:

            subject = subject.replace('-', '')
            subject = subject.replace('.', '')

            subject = ''.join(sorted(set(subject), key=subject.index))  # !!!!!!!!!!!!!!
            subject = subject.replace('!', '')
            if 'help' in subject.lower() or 'urgent' in subject.lower() or 'asap' in subject.lower() or 'asp' in subject.lower():
                return True
        return False
    except IndexError:
        return False


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# подсчет количества рекурсий.

def persistence(n):
    number = list(str(n))
    if len(number) == 1:
        return 0
    number1 = 1
    for i in range(len(number)):
        number1 = number1*int(number[i])
    print(number1)
    return persistence(number1) + 1

def summation(num):
    output = 0
    for i in range(num+1):
        output = output + i
    return output



print(summation(8))   # 36


def summation(num):
    if num == 0:
        return 0
    return num + summation(num-1)

print(summation(8))   # 36

def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

===================================

#убрать дубликаты в списке или строке:

def unique_in_order(iterable):
  r = []
  for x in iterable:
    x in r[-1:] or r.append(x)
  return r

def unique_in_order(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

# геренарция перестановок N числе в M позициях.

def find(number, A):
    for x in A:
        if number == x:
            return True
    return False

def generate_permutations(N:int, M:int = -1, prefix = None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(2)

#==============================

# располагаем цифры по убыванию:

def descending_order(num):
    num = str(num)
    numbers = ''
    for i in range(len(num)):
        numbers = numbers + max(num)
        num = num.replace(max(num), '')

    return int(numbers)
#========================================

#через рекурсию:

def descending_order(num):

    if num == '':
        return num
    num = str(num)
    global numbers

    numbers += max(num)
    num = num.replace(max(num), '')
    descending_order(num)

    return int(numbers)

#через сортировку:

def descending_order(num):
    return int(''.join(sorted([number for number in str(num)], reverse=True)))

#====================================
# сортировка по фразы по цифрам в словах.

def order(sentence):

    list_string = sentence.split()
    dictionary = {}
    for i in list_string:
        for z in i:
            if z.isdigit():
                dictionary.update({z: i})
                break
    dictionary = dict(sorted(dictionary.items(), key=lambda t: t[0]))
    return str(' '.join(dictionary.values()))

print(order("is2 Thi1s T4est 3a")) #, "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2")) #, "Fo1r the2 g3ood 4of th5e pe6ople")
print(order("")) #, "")

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

def order(sentence):
  return " ".join(sorted(sentence.split(), key=min))

def comp(x):
  for i in x:
      if i.isdigit():
          return int(i)

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=comp))

#================================================================

# вывести буквы из середины строки для четного и нечетного случаев.

def get_middle(s):

    return s[(len(s) // 2)-1:(len(s) // 2)+1] if len(s) % 2 == 0 else s[(len(s) // 2)]

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]

print(get_middle("test")) #,"es")
print(get_middle("testing")) #,"t")

#================================================================
# записать число в развернутой форме.

def expanded_form(num):
    a = list(reversed(list(enumerate(reversed(str(num))))))
    print(a)
    enumerated = [z for z in a if z[1] != '0']

    string = ''
    for i in range(len(enumerated)):
        print(i)
        if i != (len(enumerated)-1):
            string = string + f'{int(enumerated[i][1])*(10**int(enumerated[i][0]))} + '
        else:
            string = string + f'{int(enumerated[i][1])*(10**int(enumerated[i][0]))}'
    return string

print(expanded_form(12)) #, '10 + 2');
print(expanded_form(42)) #, '40 + 2');
print(expanded_form(70304)) #, '70000 + 300 + 4');

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

#====================================================
# является ли строка исограммой.

    def is_isogram(string):
        for i in string.lower():
            if string.lower().count(i) > 1:
                return False
        return True


print(is_isogram("Dermatoglyphics"))  # , True)
print(is_isogram("isogram"))  # , True)
print(is_isogram("aba"))  # , False, "same chars may not be adjacent")
print(is_isogram("moOse"))  # , False, "same chars may not be same case")
print(is_isogram("isIsogram"))  # , False)
print(is_isogram(""))  # , True, "an empty string is a valid isogram")

# еще классное решение:

def is_isogram(string):
    return len(string) == len(set(string.lower()))

#================================================

# возвести в квадрат

def square_digits(num):
    return (''.join(list(map(str, ([int(x)**2 for x in str(num)])))))

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))  # можно на объект сразу делать join и он будет выдаваться строкой!!


print(square_digits(9119)) #, 811181)

#==========================================
# сдвинуть английские буквы на 13 по шифру Цезаря.


def rot13(message):
    string = ''
    for i in message:
        if ord(i) >= 97 and ord(i) <= 109:
            string = string + chr(ord(i) + 13)
        elif ord(i) > 109 and ord(i) <= 122:
            string = string + chr(ord(i) - 13)
        elif ord(i) >= 65 and ord(i) <= 77:
            string = string + chr(ord(i) + 13)
        elif ord(i) > 77 and ord(i) <= 90:
            string = string + chr(ord(i) - 13)
        else:
            string = string + i
    return string

print(rot13("test")) #,"grfg")
print(rot13("Test"))  #,"Grfg")


import string

def rot13(message):
    return message.encode('rot13')

#==================================================
# просуммировать последовательность между двумя данными числами а и b:

def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


#===================================================

# кодирование и декодирование: каждый второй сначала, затем остальная часть.

def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))    # берем по очереди из двух строк!
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text




#===============================

def encrypt(text, n):

    if n <= 0:
        return text

    output_string_1 = ''
    output_string_2 = ''

    for i in range(1, len(text)+1):
        if i % 2 == 0:
            output_string_1 = output_string_1 + text[i-1]
        else:
            output_string_2 = output_string_2 + text[i-1]
    full_string = output_string_1 + output_string_2
    n -= 1

    out_string = encrypt(full_string, n)

    return out_string

def decrypt(encrypted_text, n):

    if n <= 0:
        return encrypted_text

    part_1 = encrypted_text[:len(encrypted_text)//2]
    part_2 = encrypted_text[len(encrypted_text)//2:]
    print(part_1)
    print(part_2)
    output_string = ''
    z = 0
    j = 0
    for i in range(1, len(encrypted_text)+1):

        if i % 2 == 0:
            output_string = output_string + part_1[z]
            z += 1
        else:
            output_string = output_string + part_2[j]
            j += 1
    n -= 1
    out_string = decrypt(output_string, n)

    return out_string


print(encrypt("This is a test!", 101)) #, "This is a test!")

#====================================================================

# вместо camel case добавить пробелы.

def solution(s):

    string = ''.join([f" {i}" if i.isupper() else i for i in s])

    return string



print(solution("breakCamelCase")) #, "break Camel Case")

#====================================================================

# содержит ли строка все буквы от a до z:

import string

def is_pangram(s):
    for i in string.ascii_uppercase:
        if i not in s.upper():
            return False
    return True

import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))  #, True)

#===============================================================

# если буква встр. один раз - ( если больше )

def duplicate_encode(word):
    output_string = ''
    for i in word.lower():
        if (word.lower()).count(i) > 1:
            output_string = output_string + ')'
        else:
            output_string = output_string + '('
    return output_string

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

print(duplicate_encode("din")) #, "(((")
print(duplicate_encode("recede")) # , "()()()")
print(duplicate_encode("Success")) #, ")())())", "should ignore case")
print(duplicate_encode("(( @")) #, "))((")

#===============================================================

def sum_pairs(ints, s):
    answers = {}
    for i in range(len(ints)):
        for z in range(i+1, len(ints)):
            if ints[i] + ints[z] == s:
                answers.update({z: [ints[i], ints[z]]})
    if answers.values():
        return answers[(min(answers.keys()))]
    return None


def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)



l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

#test.describe("Testing For Sum of Pairs")
print(sum_pairs(l1, 8)) #== [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
print(sum_pairs(l2, -6))# == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
print(sum_pairs(l3, -7))# == None, "No Match: %s should return None for sum = -7" % l3)
print(sum_pairs(l4, 2)) #== [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
print(sum_pairs(l5, 10)) #== [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
print(sum_pairs(l6, 8)) #== [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
print(sum_pairs(l7, 0)) #== [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
print(sum_pairs(l8, 10)) #== [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)

#==================================================================

# нужно, чтобы человек пришел обратно на старт и прогулка заняла 10 мин.

def is_valid_walk(walk):

    if len(walk) == 10 and (walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')):
        return True
    return False

def is_valid_walk(walk):

    walk_dist_n_s = 0
    walk_dist_w_e = 0
    for i in walk:
        if i == 'n':
            walk_dist_n_s += 1
            continue
        if i == 's':
            walk_dist_n_s -= 1
            continue
        if i == 'w':
            walk_dist_w_e += 1
            continue
        if i == 'e':
            walk_dist_w_e -= 1
            continue
    if walk_dist_n_s == 0 and walk_dist_w_e == 0:
        if len(walk) <= 10:
            return True

    return False

#===================================================================================================


def stock_list(listOfArt, listOfCat):
    import re
    dictionary = []
    for i in listOfCat:
        for j in listOfArt:
            if j[0] == i:
                number = int((re.search(r'\d+', j)).group())
                if i in dictionary:
                    dictionary[dictionary.index(i)+1] = dictionary[dictionary.index(i)+1] + number
                else:
                    dictionary.append(i)
                    dictionary.append(number)

    string = ''
    for i in range(len(listOfCat)):
        if i == len(listOfCat) - 1:
            string = string + f'({dictionary[0]} : {dictionary[1]})'
            break
        string = string + f'({dictionary[0]} : {dictionary[1]}) - '

    return string

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))  #, "(A : 200) - (B : 1140)")



def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
    return " - ".join("({} : {})".format(category, sum(int(item.split()[1]) for item in stocklist if item[0] == category)) for category in categories)

#=====================================================================

# посчитать сколько разных повторяющихся букв в строке:

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c) > 1]) # мы перебираем неповторяющиеся элементы и добавляем их в список только если их количество в изначальном массиве больше одного.

def duplicate_count(text):

    number = []
    for i in text.lower():
        if ((text.lower()).count(i)) > 1 and i not in number:
            number.append(i)
            continue

    return len(number)




print(duplicate_count("abcde")) #, 0)
print(duplicate_count("abcdea")) #, 1)
print(duplicate_count("indivisibility")) #, 1)
# ======================================================================

# регулярка для проверки пароля:

# Вот так выглядит выражение целиком:

#/(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}/g
# Вот пример на regex101. Можете попробовать написать свои пароли и проверить работу регулярного выражения на соответствие своим требованиям.

#Пояснение:

#(?=.*[0-9]) - строка содержит хотя бы одно число;
#(?=.*[!@#$%^&*]) - строка содержит хотя бы один спецсимвол;
#(?=.*[a-z]) - строка содержит хотя бы одну латинскую букву в нижнем регистре;
#(?=.*[A-Z]) - строка содержит хотя бы одну латинскую букву в верхнем регистре;
#[0-9a-zA-Z!@#$%^&*]{6,} - строка состоит не менее, чем из 6 вышеупомянутых символов.

from re import search

regex = "^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{6,}$"

import re

match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12')
print(match[0] if match else 'Not found')

match = re.search(r'\d\d\D\d\d', r'Телефон 1231212')
print(match[0] if match else 'Not found')
# -> Not found

match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
print('YES' if match else 'NO')
print(match[0])
# -> YES
match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12')
print('YES' if match else 'NO')
# -> NO

print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'))
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', '']

print(re.findall(r'\d\d\.\d\d\.\d{4}',
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
# -> ['19.01.2018', '01.09.2017']





