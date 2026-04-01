things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200, 
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

things_p = {}
for name,weight in things.items():
    things_p[weight] = name
things_p = sorted(things_p.items(), reverse=True)

N = int(input()) * 1000
res = []

for weight, name in things_p:
    if N - weight >= 0:
        res.append(name)
        N -= weight

print(*res)