print("{0}은 {1}다 {2}".format(1, "바보", 5))

print("%s는 %s다" % ("이상빈", "바보"))


a = [1, 2, 2, 1, 1]
b = 0
c = 0
for m in a:
    if m == 1:
        b += 1
    if m == 2:
        c += 1

print(b)
print(c)

