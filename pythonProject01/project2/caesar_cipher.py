def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char
    return result

def get_valid_shift():
    while True:
        try:
            shift = int(input("Lütfen 1 ile 25 arasında bir kaydırma değeri girin: "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Kaydırma değeri 1 ile 25 arasında olmalıdır.")
        except ValueError:
            print("Geçerli bir tam sayı girin.")

text = input("Şifrelenecek metni girin: ")


shift = get_valid_shift()


encrypted_text = caesar_cipher(text, shift)
print("Şifrelenmiş metin:", encrypted_text)
