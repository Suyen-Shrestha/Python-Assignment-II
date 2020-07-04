
def find_john(names_li):
    for name in names_li:
        if name == 'John':
            return True
    return False

friends_li = ['Rupak', 'Anish', 'Manish', 'Jeevesh']    

print(f'The sample friends list: {friends_li}')

if find_john(friends_li):
    print('John Found!')
else:
    print('John Not Found!')    
          