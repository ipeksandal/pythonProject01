def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    reversed_text = cleaned_text[::-1]
    return cleaned_text == reversed_text


text = input("Metin girin: ")
if text and is_palindrome(text):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
