import re

def calculate_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 2
    if len(password) >= 12:
        score += 2
    if re.search(r"[A-Z]", password):  
        score += 1
    if re.search(r"[a-z]", password):  
        score += 1
    if re.search(r"[0-9]", password):  
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  
        score += 2
    if score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return score, strength

password = input("Enter a password to check its strength: ")
score, strength = calculate_password_strength(password)

print(f"Password Strength Score: {score}")
print(f"Password Strength: {strength}")
