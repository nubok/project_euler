largest_number = 0

for fst in range(100, 999):
    for snd in range(100, 999):
        number = fst * snd
        if (number > largest_number):
            number_str = str(number)
            if (number_str == number_str[::-1]):
                largest_number = number
                
print largest_number
