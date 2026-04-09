def transliter(source, sep = '-'):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 
        'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 
        'э': 'e', 'ю': 'yu', 'я': 'ya'}
    
    words = source.lower().split()
    res = []
    for word in words:
        trans_word = ""
        for char in word:
            trans_word += t.get(char,char)
        res.append(trans_word)
    return sep.join(res)
    
      
lst_in = input()
print(transliter(lst_in))