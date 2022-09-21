my_list = [-10, 34, 50, 43, 601, 22, 96]
maxmum = 0
minmium = 100

for num in my_list:
    if num > maxmum:
        maxmum = num
    if num < minmium:
        minmium = num

print('max number: ', maxmum)
print('min number: ', minmium)

