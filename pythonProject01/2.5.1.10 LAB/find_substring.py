def find_substring(main_string, sub_string):
    if sub_string in main_string:
        return f'"{sub_string}" dizisi "{main_string}" dizisi içinde bulundu.'
    else:
        return f'"{sub_string}" dizisi "{main_string}" dizisi içinde bulunamadı.'


sub_string = input("Alt diziyi girin: ")
main_string = input("Ana diziyi girin: ")
result = find_substring(main_string, sub_string)
print(result)
