import csv
import uuid
import string
import random


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


with open('random_data_file.csv', mode='w') as random_data_file:
    random_writer = csv.writer(
        random_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    random_writer.writerow(['uuid', 'Code', 'Redeemed'])

    for i in range(1, 1000):
        random_ID = uuid.uuid4()
        random_code = id_generator()
        random_writer.writerow([random_ID, random_code, 'False'])
