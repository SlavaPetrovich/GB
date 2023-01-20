def letters(n):
    x = [n[0]]
    s = ''
    count = 1
    for i in range(1, len(n)):
        if n[i] == x[-1]:
            x.append(n[i])
            count = count + 1
            if len(x) == len(n):
                s = s + str(count) + x[-1]
        else:
            s = s + str(count) + x[-1]
            x.append(n[i])
            count = 1
    return s

def numbers(n):
    d = ''
    for i in range(0, len(n), 2):
        d = d + (n[i + 1] * int(n[i]))
    return d

n = input()
a = '123456789'

if n[0] in a:
    print(numbers(n))
else:
    print(letters(n))

