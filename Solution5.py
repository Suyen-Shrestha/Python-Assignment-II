my_tuple = ('Suyen', 'Shrestha', 24)

print(f'The initial tuple: {my_tuple}')
people = []

people.append(my_tuple)

friends_tup1 = ('Ramesh', 'Maharjan', 25)
friends_tup2 = ('Geeta', 'Poudel', 23)
friends_tup3 = ('Bibhu', 'Thapa', 25)
friends_tup4 = ('Hrithik', 'Yadav', 21)

print(f'The tuples to be appended to people\'s list: {friends_tup1}, {friends_tup2}, {friends_tup3}, {friends_tup4}')

people.append(friends_tup1)
people.append(friends_tup2)
people.append(friends_tup3)
people.append(friends_tup4)

print(f'The people\'s list after appending the tuples: {people}')

print(f'The list of people: {people}')

people.sort(key=lambda x: x[2])

print(f'The sorted list of people according to their age: {people}')