with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('Esta es una nueva linea\n')
    file.write('Otra linea\n')