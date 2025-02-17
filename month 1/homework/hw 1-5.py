data = ['O!', 'Megaphon', '0705', 'Beeline', '0550', '0770', 'Katel', '0510', 'Fonex', '0543']

designations = []
codes = []

for i in data:
    if i.isnumeric():
        codes.append(i)
    else:
        designations.append(i)

# word = designations.insert(0, data.pop(data.index('O!')))
# word1 = designations.insert(0, data.pop(data.index('Megaphon')))
# word2 = designations.insert(1, data.pop(data.index('Beeline')))
# word3 = designations.insert(3, data.pop(data.index('Katel')))
# word4 = designations.insert(4, data.pop(data.index('Fonex')))
#
# code = codes.insert(0, data.pop(data.index('0705')))
# code1 = codes.insert(1, data.pop(data.index('0550')))
# code2 = codes.insert(2, data.pop(data.index('0770')))
# code3 = codes.insert(3, data.pop(data.index('0510')))
# code4 = codes.insert(4, data.pop(data.index('0543')))

print(designations)
print(codes)

operators = dict(zip(designations, codes))

del operators["Katel"]
del operators['Fonex']
# print(operators)

operators["O!"] = "952"
operators["Megaphon"] = "908"
operators["Beeline"] = "951"

for key, value in operators.items():
    print(key, '==>', value)

