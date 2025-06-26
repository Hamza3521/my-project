
names=input('Enter the first and last name of each friend. \n').split(', ')
for name in names:
    print(f'{[name]}')
    parts_names=name.split()
    if len(parts_names)>=2:
     first_name=parts_names[0][0]
     last_name=parts_names[1][0]
     print(f'{first_name}.{last_name}')
    else:
        print('Follow the instructions') 