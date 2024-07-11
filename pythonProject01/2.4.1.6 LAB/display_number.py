def display_number(number):
    
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

    
    num_str = str(number)

   
    lines = [""] * 5

    
    for digit in num_str:
        d = int(digit)
        for i in range(5):
            lines[i] += digits[d][i] + " "

  
    for line in lines:
        print(line.rstrip())



display_number(123)
print()
display_number(9081726354)
