# Test python env
def print_hello():
    animals = ['dog', 'cat', 'hamster', 'tiger'] # in oneline
    foods = [
	'Spagetti',
	'Pizza',
	'bibimbob'  # trailing comma X
    ]
    names = [
	'John', 
	'Jane', 
	'Gil-dong',
	'Dong-eun',    #trailing comma O
    ]
    for f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
