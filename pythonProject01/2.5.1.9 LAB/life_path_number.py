def life_path_number(birth_date):
    total = sum(int(digit) for digit in birth_date)
    while total > 9:
        total = sum(int(digit) for digit in str(total))

    return total
birth_date = input("Doğum tarihinizi girin (YYYYMMDD, YYYYDDMM veya MMDDYYYY biçiminde): ")
life_path_number = life_path_number(birth_date)
print("Yaşam Numarası:", life_path_number)
