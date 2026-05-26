import string

def has_length(password):
    if len(password) >= 8:
        return True
    return False

def has_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False
            
def has_uppercase(password):            
    for char in password:          
        if char.isupper():
            return True
    return False

def has_lowercase(password):          
    for char in password:         
        if char.islower():
            return True               
    return False

def has_specialcharacters(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False


def evaluate_password(password):
    checks = [has_length, has_number, has_uppercase, has_lowercase, has_specialcharacters]
    score = 0
    for function in checks:
        if function(password):
            score += 1
    if score >= 4:
        return f"Strong password, rating of {score} out of 5"
    elif score == 3:
        return f"Medium password , rating of {score} out of 5"
    else:
        return f"Weak password, rating of {score} out of 5"
    
password = input("Please enter a password: ")
print(evaluate_password(password))