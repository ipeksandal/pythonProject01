def display_number(number):
    # Her rakamın yedi segmentli ekran karşılığını tanımla
    digits = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", "  #", "  #", "  #", "  #"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", "  #", "  #"],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"]  # 9
    ]

    # Girdiyi string olarak al ve her rakamı ayrı ayrı işle
    num_str = str(number)

    # Beş satır için dizileri başlat
    lines = [""] * 5

    # Her rakamı sırayla işle ve uygun satıra ekle
    for digit in num_str:
        d = int(digit)
        for i in range(5):
            lines[i] += digits[d][i] + " "

    # Her satırı yazdır
    for line in lines:
        print(line.rstrip())


# Örnek girdi ve çıktı
display_number(123)
print()
display_number(9081726354)
