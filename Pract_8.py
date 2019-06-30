"""
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

"""
'''
S = str(input("Введите строку S: "))

print("Строка \'%s\' имеет длину %d сиволов." % (S, len(S)))

subs_set = set()
# subs_dict = {}
for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        subs_set.add(hash(S[i:j]))
        # print(S[i:j], i, j)
        # subs_dict[S[i:j]] = hash(S[i:j])

# print(len(list(subs_dict.keys())), list(subs_dict.keys()))
print("Количество различных подстрок в этой строке:", len(subs_set))
'''


'''2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.'''

def huffman_encode(s):
    return {ch: ch for ch in s}

def main():
    s = input()
    code = huffman_encode()
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)

if __name__ == "__main__":
    main()
