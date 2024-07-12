def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def calculate_char_frequency(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def print_histogram(frequency):
    for char, count in sorted(frequency.items()):
        print(f'{char}: {"*" * count} ({count})')

def main():
    filename = input("Lütfen dosya adını girin: ")
    try:
        text = read_file(filename)
        frequency = calculate_char_frequency(text)
        print_histogram(frequency)
    except FileNotFoundError:
        print(f"Dosya '{filename}' bulunamadı.")

if __name__ == "__main__":
    main()
