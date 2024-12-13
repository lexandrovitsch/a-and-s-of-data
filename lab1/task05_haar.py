from my_hadamard_numpy import generate_hadamard

def is_haar_row(row):
    middle = len(row) // 2
    half_1 = row[:middle]
    half_2 = row[middle:]

    for i in range(middle):
        if (half_1[i] == False and half_2[i] != True) or (half_1[i] == True and half_2.all() != False):
            return False
    
    return True

def count_haar_rows(rows):
    counter = 0
    matches = []
    for row in rows:
        if is_haar_row(row):
            matches.append(row)
            counter += 1
    
    return matches, counter

n = (int((input('Введите степень двойки для размера матрицы >> ')))) ** 2

hadamard = generate_hadamard(n)
matches, count = count_haar_rows(hadamard)

print(f'Количество совпадений: {count}\n')

print('Совпадения:')
for i in matches:
    print(i.astype(int))
