cars = {'car_name': 'mers', 'model': 'AMG', 'price': 50000}
word = input('write a key: ')

if word in cars:
    print(cars[word])
else:
    print('Error')
