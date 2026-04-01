year = [x for x in range(1,13)]
year[0] =  year[2] =  year[4] =  year[6] =  year[7] =  year[9] =  year[11] = list(range(1,32))
year[3] =  year[5] =  year[8] =  year[10] = list(range(1,31))
year[1] = list(range(1,29))

m,d = map(int,input().split())

if d == len(year[m-1]):     #условие для последнего дня месяца m
    print (f"{m:0>2}.{d-1:0>2} {m+1:0>2}.01")   
elif d == 1:                #условие для первого дня любого месяца
    print (f"{m-1:0>2}.{year[m-2][-1]:0>2} {m:0>2}.{d+1:0>2}" )
else:                       #любые остальные случае, проверки на валидность даты нет
    print(f"{m:0>2}.{d-1:0>2} {m:0>2}.{d+1:0>2}")