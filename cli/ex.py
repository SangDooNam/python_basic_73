from loader import Loader

personnel = Loader(model='personnel')
stock = Loader(model='stock')


for employee in personnel:
    print(employee)

print(personnel)

print(len(list(stock)))