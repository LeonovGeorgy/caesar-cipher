# На вход программе подается строка текста на английском языке,
# в которой нужно зашифровать все слова. Каждое слово строки следует
# зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.

a = input()
new = []
new = a.split(' ')
new_end2 = []

for i in new:
    new2 = []
    new2.extend(i)
    cnt = 0
    for n in new2:
        if n.isalpha():
            cnt += 1
            new_end = []
    for f in new2:
        if f.islower():
            f = ord(f) + cnt
            if f > 122:
                f = f - 26
                new_end.append(chr(f))
            else:
                new_end.append(chr(f))
        elif f.isupper():
            f = ord(f) + cnt
            if f > 90:
                f = f - 26
                new_end.append(chr(f))
            else:
                new_end.append(chr(f))
        else:
            new_end.append(f)

    a = ''.join(new_end)
    new_end2.append(a)
print(*new_end2)