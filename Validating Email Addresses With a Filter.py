import re

def fun(s):
    # return True if s is a valid email, else return False
    regexPattern =  re.compile(r'^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{,3}$')
    result = re.search(regexPattern, s)
    
    if result:
        return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)