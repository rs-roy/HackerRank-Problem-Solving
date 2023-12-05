def count_substring(string, sub_string):    
    count = 0

    for i in range(len(string)):
        if len(string)- i >= len(sub_string):
            partialMatch = 0
            temp = i
            for j in range(len(sub_string)):
                if string[temp] == sub_string[j]:
                    #print(f"{a[temp]}, {b[j]}")
                    partialMatch +=1
                    temp+=1           
                else:
                    break
            if partialMatch == len(sub_string):
                count+=1
        else:
            break
        
    return count