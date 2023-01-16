from morse_code_alphabet import alphabet_dict

str_to_convert = input('Input the text you want to convert to morse code: ')

morse_code_str = ""
error = False
for char in str_to_convert:
    try:
        morse_code_str += f'{alphabet_dict[char.lower()]} '
    except KeyError:
        error = True
        break

if not error:
    print(f'{str_to_convert} in morse code is: {morse_code_str}')
else:
    print('This is not a valid string.')
