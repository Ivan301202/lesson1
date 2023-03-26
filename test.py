print('Введите количество журавликов')
S = input()
S = int (S)
for i in range(30):
    if i*2+i*4 == S :
        print("Петя и Сергей сделали по ", i, ",а Катя - ", i*4 )
    
