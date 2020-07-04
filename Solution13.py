import csv


def create_csv(filename,tuples_list):
    fields_names = ['name', 'address', 'age'] 
    with open(filename,'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(fields_names)
        csv_writer.writerows(tuples_list) 


sample_list_of_tuples = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
file_name = 'sample.csv' 
create_csv(file_name,sample_list_of_tuples)

print(f'The csv file of name "{file_name}" has been created!')