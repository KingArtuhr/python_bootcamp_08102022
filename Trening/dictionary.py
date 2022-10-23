chanels = {'Google' : 1480, 'Email' : 300, 'Natural Traffic': 440, 'TV Spot' : 700}

print(chanels)
print(chanels['Email'])
chanels_update = {'Natural Traffic' : 520, 'News': 600}

chanels.update(chanels_update)
print(chanels)

print(chanels.keys())
print(chanels.pop('Email'))
print(chanels)



