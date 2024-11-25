import re

class PasswordStrengthChecker:
    def __init__(self, min_length=8):
        self.min_length = min_length
    
    def check_password_strength(self, password):
       
        score = 0
        feedback = []

        
        if len(password) >= self.min_length:
            score += 1
        else:
            feedback.append(f"Password should be at least {self.min_length} characters long.")
        
        
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Password should contain at least one lowercase letter.")

        
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Password should contain at least one uppercase letter.")

        
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Password should contain at least one digit.")
        
        
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Password should contain at least one special character (e.g., !@#$%^&*).")
        
        
        if score == 5:
            feedback.append("Password is very strong!")
        elif score == 4:
            feedback.append("Password is strong.")
        elif score == 3:
            feedback.append("Password is moderate.")
        elif score == 2:
            feedback.append("Password is weak.")
        else:
            feedback.append("Password is very weak.")
        
        return score, feedback

# Example usage:
if __name__ == "__main__":
    checker = PasswordStrengthChecker(min_length=8)
    
    # Input password to test
    password = input("Enter a password to check its strength: ")

    # Check the password strength
    score, feedback = checker.check_password_strength(password)

    # Print the feedback
    print("\nPassword Strength Feedback:")
    for f in feedback:
        print(f)
   