
def average_age(names_list):
    average_age = 0
    age_sum = 0
    age_count = 0 # for counting no. of ages ignoring 'None' ages.
    for name in names_list:
        if name[2] != None:
            age_count += 1
            age_sum += name[2]    
    average_age = round((age_sum / age_count),2)    
    return average_age


def check_age(age,av_age):
    if age != None:
        if age > av_age:
            return 'old'
        else:
            return 'young'
    else:
        return None     


friends_detail_list = [('Ramesh', 'Maharjan', None),('Geeta', 'Poudel', 23),('Bibhu', 'Thapa', 25),('Hrithik', 'Yadav', 22),('Manish', 'Parajuli', None)]
avg_age = average_age(friends_detail_list)


print(f'The sample list of tuple with firstname, lastname and age: {friends_detail_list}')
print(f'The average age after skipping "None" is: {avg_age}')


for friend in friends_detail_list:
    print(f'Name:{friend[0]}, {check_age(friend[2],avg_age)}')            