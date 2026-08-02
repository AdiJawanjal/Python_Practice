mixed = ["Adi",54]
mix = [51,52]
print(mixed)
mixed.append(True)
print(mixed)
mixed.pop(1)
print(mixed)
mixed.extend(mix)
print(mixed)

'''
O/P
['Adi', 54]
['Adi', 54, True]
['Adi', True]
['Adi', True, 51, 52]
'''
