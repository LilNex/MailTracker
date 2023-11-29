import csv

csv_file_path = 'data.csv'

def write_data(name, email, url):
    with open(csv_file_path, 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, url])


def csv_to_python_object():
    result = {}
    
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            sender = row[0]
            receiver = row[1]
            identifier = int(row[2])
            
            if identifier not in result:
                result[identifier] = [sender, receiver]
            else:
                result[identifier].extend([sender, receiver])

    return result
