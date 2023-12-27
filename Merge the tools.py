def merge_the_tools(string, k):
    mylist = []
    for i in range(0,len(string),k):
        mylist.append((string[i:i+k]))

    #print(mylist)
    for item in mylist:
        result = ""
        for char in item:
            if char not in result:
                result = result + char
        print(result)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)