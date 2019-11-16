lon = []
lon1= []

yes = 'y'

while yes == 'y':
    new = int(input('Введите число, которое хотите добавить в список:\n'))
    lon.append(new)
    print(lon)
    yes = input('Хотите добавить ещё число в список? y/n\n')

for x in lon:
    if x % 2 == 0:
        lon1.append(x)
    else:
        lon1.append(0)

print(lon)
print(lon1)