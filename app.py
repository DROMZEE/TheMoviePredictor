
    
    
    return eval(classname)


wc -l imdb_datasets:title.principals.tsv

def get_time():
	return int(round(time.time() * 1000))

def filename_to_class(filename):
	name = ''.join(word.title() for word in filename[:-4].split('.'))
	return str_to_class(f'entity.{name}')
	
def wc(filename):
	return( int(check_output(["wc", "-l", filename]).split()[0])
	
	if __name__ == '__main__':
	db = DB('themoviepredictor')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			compute_time = end_time - start_time
			ops_per_sec = math.ceil(1000 / compute_time * batch_size)
			print(f' - Inserted {executed_lines}/{line_count} lines ({percen