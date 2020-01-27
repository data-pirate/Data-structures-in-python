import numpy as np

lst = list()
print('<================Array Generator ====================>')
print('type \'done\' when finished !!!')

while True:
    inp = input('Enter the numbers to be added in array: ')
    if inp.lower() == 'done':
        break
    try:
        inp = int(inp)
        lst.append(inp)
    except:
        print('Please Enter a valid number you enterded {}'.format(inp))

arr = np.array(lst)

print('array :', arr)