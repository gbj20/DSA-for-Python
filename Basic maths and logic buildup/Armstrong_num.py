n = 153
num = n
total = 0
nod = len(str(n))

while num > 0:
    last_digit = num % 10
    total = total+last_digit**nod
    num = num//10
print(n == total)
