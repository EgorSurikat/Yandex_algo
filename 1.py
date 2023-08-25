data = [0] * (ord('z') + 1)
max_count = 0
input_file = open('input.txt', 'r')
for line in input_file:
    for el in line:
        if el != ' ' and el != '\n':
            data[ord(el)] += 1
            if data[ord(el)] > max_count:
                max_count = data[ord(el)]
input_file.close()
new_data = ''
symbols = ''
for i in range(max_count):
    for count_symbol in range(len(data)):
        if data[count_symbol] != 0:
            if data[count_symbol] > max_count - i - 1:
                new_data += '#'
            else:
                new_data += ' '
            if i == 0:
                symbols += chr(count_symbol)
    new_data += '\n'
new_data += symbols
output_file = open('output.txt', 'w')
output_file.write(new_data)
output_file.close()