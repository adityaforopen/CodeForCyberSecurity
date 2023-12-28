def check_password_strength(password):
    
    # Password strength criteria
    
    length_criteria = 8
    complexity_criteria = {'uppercase' : 1, 'lowercase': 1, 'numbers': 1, 'special_characters': 1}
    
    # Check Length
    
    if len(password) < length_criteria:
        return 'WEAK PASSWORD should be atleast {} characters long'.format(length_criteria)
    
    # Check Complexity
    
    complexity_score = sum(1 for criteria in complexity_criteria if any(char.isalpha() == criteria == 'special_characters' or char.isdigit() == criteria for char in password))
    
    if complexity_score < len(complexity_criteria):
        return 'WEAK: password should be include at least on UPPERCASE letter, one lowercase letter, one number, and one special character.'
    
    # If Password is considered strong
    return 'Strong: Password meets the criteria for strength'

# User Input Here

user_password = input("Enter Your Password: \n")

# Analyze and Print Password Strength

print(check_password_strength(user_password))