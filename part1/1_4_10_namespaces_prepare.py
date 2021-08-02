# Dictionary

capitals = dict()

capitals['Russia'] = 'Moscow'
capitals['Ukraine'] = 'Kiev'
capitals['USA'] = 'Washington'

countries = ['Russia', 'France', 'USA', 'Russia']

for country in countries:
    if country in capitals:
        print("Capital of country " + country + ":" + capitals[country])
    else:
        print("There isn't the country in base " + country)


# create dictionary
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
Capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
print(Capitals)



# Work with dictionary
A = {'ab' : 'ba', 'aa' : 'aa', 'bb' : 'bb', 'ba' : 'ab'}

key = "ac"

if key in A:
    del A[key]
try:
    del A[key]
except KeyError:
    print('There is no element with key "' + key + '" in dict')
print(A)

# work with iteration
A = dict(zip('abcdef', list(range(6))))
for key in A:
    print(key, A[key])

for key, val in A.items():
    print(key, val)