import csv


def write_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        new_list = []

        for row in csv_reader:
            new_list.append(dict(row))
    return new_list        

sample_file = 'sample.csv' #file from previous question.

print(f'Reading from csv file named: {sample_file}')

output = write_csv(sample_file)

print(f'Final Output: {output}')