import re

def valid_palindrome(s: str) -> bool:
    s = s.lower()
    only_alpha_numeric_s = [char.lower() for char in s if char.isalnum()]

    # only_alpha_numeric_s = re.sub(r"[^a-zA-Z0-9]", "", s)

    return only_alpha_numeric_s == only_alpha_numeric_s[::-1]

print(valid_palindrome("race a car"))