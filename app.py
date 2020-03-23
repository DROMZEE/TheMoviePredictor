import entity
from db import DB
from tsv import TSV
from subprocess import check_output
import os
import sys
import glob
import math
import time

batch_size = 50000


def str_to_class(classname):
    # Warning, evel() is not safe!
    return eval(classname)


def get_time():
    return int(round(time.time() * 1000))


def filename_to_class(filename):
    name = ''.join(word.title() for word in filename[:-4].split('.'))
    return str_to_class(f'entity.{name}')


def wc(filename):
    return int(check_output(["wc", "-l", filename]).split()[0])


if __name__ == '__main__':
    db = DB('themoviepredictor')
    db.reset()

    filepaths = glob.glob('./imdb_datasets/*.tsv')
    #filenames = ['name.basics.tsv', 'title.basics.tsv', 'title.principals.tsv']
    #filepaths = ['./imdb_datasets/title.principals.tsv']
    for filepath in filepaths:
        filename = filepath.split('/').pop()
        line_count = wc(filepath)
        collection_name = filename[:-4]
        class_name = filename_to_class(filename)
        tsv = TSV(f'./imdb_datasets/{filename}')
        print(f'x Importing {filename} ({line_count} lines)...')
        executed_lines = 0
        while True:
            start_time = get_time()
            lines = tsv.read_sequential(batch_size)
            if not lines:
                break

            db.bulk_insert(collection_name, class_name.dict_to_object(lines))
            end_time = get_time()
            executed_lines += batch_size
            percent = math.floor(executed_lines / line_count * 100 * 100) / 100
            compute_time = end_time - start_time
            ops_per_sec = math.ceil(1000 / compute_time * batch_size)
            print(
                f'  - Inserted {executed_lines}/{line_count} lines ({percent}% - {ops_per_sec}ops)')
