from tsv import TSV
import os
import psutil
process = psutil.Process(os.getpid())

tsv = TSV('./title.principals.tsv')
lines = []
batch_number = 1
line_number = 0
lines = tsv.read_sequential(10000)
while lines:
    #print(f"Batch #{batch_number}")
    batch_number += 1
    for line in lines:
        line_number += 1
        if line_number % 100000 == 0:
            print(f'{process.memory_info().rss/1024/1024}Mb')
            print(line_number)
        # print(
        #    f"{line['id']}: {line['first_name']} {line['last_name']} <{line['email']}>")

    lines = tsv.read_sequential(10000)
