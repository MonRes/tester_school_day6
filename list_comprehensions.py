dev_id = []

for i in range(1, 5):
    dev_id.append('device_' + str(i))

print(dev_id)
print(['device_' + str(i) for i in range(1, 5)]) #składnia wyrażenia listowego


print([i ** 2 for i in range(0, 100)]) #liczby do kwadratu w zakresie od 0 do 100

dict = [{'id': 2, 'model': 'Radeon'}, {'id': 3, 'model': 'Xeon'}, {'id': 4, 'model': 'Sth'}]

print ([record['id'] for record in dict])

lst = ['abcrr', 'cded', 'fgh', 'ijk']

for record in lst:
    print(len(record))

print([len(record) for record in lst])
