def validate(str):
    valid_chars = ({chr(i) for i in range(ord('a'), ord('z')+1)} | 
               {chr(i) for i in range(ord('A'), ord('Z')+1)} | 
               {chr(i) for i in range(ord('0'), ord('9')+1)} | 
               {"@", ".", "_"})
    
    if (set(str)<valid_chars) and ("@" in set(str)) and ("." in set(str)) :
        print("ДА")
    else:
        print("НЕТ")    
    

validate(input())