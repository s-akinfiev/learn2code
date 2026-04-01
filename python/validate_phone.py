s = input()
s_places = s[:2] + s[2] + s[6] + s[10] + s[13]
template = '+7(xxx)xxx-xx-xx'

res = 'ДА'
if len(s) == 16 and s_places == '+7()--':
    for ind, val in enumerate(template):
        if val == 'x':
            if s[ind].isdigit():
                continue
            else:
                res = 'НЕТ'
                break
else:
    res = 'НЕТ'
        
print(res)