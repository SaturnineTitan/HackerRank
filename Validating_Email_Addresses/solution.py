def fun(s):
    # return True if s is a valid email, else return False
    # Copy string for processing 
    copy = s
    # Invalid username characters 
    invalid_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '~', '`', ';', ':', '/', '\'', '\\', '<', '>', 
                     '.', '?', ',', '|', '{', '}', '[', ']', '"']
    # remove @ and . from copy before splitting into list 
    copy = copy.replace('@', ' ')
    copy = copy.replace('.', ' ')
    copy = copy.strip()
    # Separate email username, website, and extension for processing
    email = copy.split(' ')
    # Check all elements of email address are in list 
    if len(email) != 3:
        return False 
    # Check format of s matches valid email format 
    if s == email[0] + '@' + email[1] + '.' + email[2]:
        pass
    else:
        return False
    # Check length and characters of email extension 
    if len(email[2]) > 3 or not email[2].isalpha(): 
        return False
    # Check website is alphanumeric 
    elif not email[1].isalnum():
        return False
    # Check username contains only alphanumerics and _ ; -
    for elem in invalid_chars:
        if elem in email[0]:
            return False
    # if s passes all falsifications, return True 
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
