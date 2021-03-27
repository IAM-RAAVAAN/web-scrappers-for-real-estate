price = [1750, 1750, 1500, 1500, 800, 780, 780, 725, 720, 655, 600, 600, 550, 450, 430, 385, 300, 300, 275, 275, 210, 165, 125]
a = [1300, 4500, 3100, 1250, 1800, 4800, 4000, 4800, 4800, 4800, 1350, 1350, 2100, 750, 600, 1000, 1450, 1450, 650, 650, 400, 440, 400]

print(len(price))
print(len(a))

r = []

print('Maximum Buy:\t\t', max(price))
print('Minimum Buy:\t\t', min(price))

for i in range(0, len(price)):
    r.append(price[i]/a[i])
   
print('List of rent:\t\t', r)

# print(sum(r))
print('Total Properties:\t', len(r))
print('Average Buy/sq ft.:\t',(sum(r)/len(r))*100000)
