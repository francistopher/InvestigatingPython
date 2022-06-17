wisl = ['what', 'is', 'a', 'list?']
idk = ['where', 'should', 'i', 'start', 'off?']
print('indexing', wisl[0], wisl[1], wisl[2], wisl[3])
print(idk)
print("was that a negative index", wisl[-1])
print("and that a splice with a negative index", wisl[-3:])
print('splice all items', idk[:])
print('concatenate items', wisl + idk)
wisl[3] = 'list'
print(wisl + idk)
idk.append('well')
print(idk)
idk[2:] = ['you', 'start']
print('after mutating list through splice assignment', idk)
idk[1:] = []
print(idk)
idk[:] = []
print(idk)
print("how long?", len(wisl))
nest = [wisl, wisl]
print('nesting', nest)
