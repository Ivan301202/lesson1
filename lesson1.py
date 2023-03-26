# Задание 2
print('Введите трехзначное число')
data=input()
data=int(data)
d1 =data % 10
d2 =data % 100 // 10
d3 =data // 100
print(d1+d2+d3)

# Задание 4
print('Введите количество журавликов')
S = input()
S = int (S)
i=0
while i*6 < S:
    i=i+1
if i*6 == S :
        print('Петя и Сергей сделали по ', i, ',а Катя - ', i*4 )
else:
     print('не существует')
     
    
# Задание 6
print('Введите номер билета')
data=input()
data=int(data)
d1 =data % 10
d2 =data % 100 // 10
d3 =data %1000 // 100
d4 = data %10000 // 1000
d5 = data %100000 // 10000
d6 = data //100000

if (d1+d2+d3) == (d4+d5+d6):
    print('yes')
else:
    print('no')

# Задание 8
print('Введите n')
n = int(input())
print('Введите m')
m = int(input())
print('Введите k')
k = int(input())
if (k >= n or k >= m) and (k%m==0 or k%n==0):
    print('yes')
else:
    print('no')     