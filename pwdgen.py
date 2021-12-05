import requests, string, random

def checkquota():
    r_url = 'https://www.random.org/quota/?format=plain'
    quota = int(requests.get(r_url).text)
    if quota < 1:
        raise Exception('Quota aufgebaucht!')
    return quota


#def generate_pwd_from_str(**params):
    checkquota()
    length = params.get('length', 10)
    digits = params.get('digits', 'on')
    upperalpha = params.get('upperalpha', 'on')
    loweralpha = params.get('loweralpha', 'on')
    unique = params.get('unique', 'on')
    return requests.get('https://www.random.org/strings/?num=1&len={}&digits={}&upperalpha={}&loweralpha={}&unique={}&rnd=new&format=plain'.format(length, digits, upperalpha, loweralpha, unique)).text


#print(generate_pwd_from_str(length=20))

characters = [char for char in string.printable]
remove = ['\t', '\n', '\r', '\x0b', '\x0c']
characters = [elem for elem in characters if elem not in remove]

def get_rando_numbers(num):
    checkquota()
    numbers = requests.get('https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new&format=plain'.format(num, len(characters)-1)).text.split('\n')
    numbers.remove('')
    return numbers


def generate_pwd(num):
    pwd = ''
    random.shuffle(characters)
    numbers = get_rando_numbers(num)
    for number in numbers:
        pwd += characters[int(number)]
    return print(pwd)

generate_pwd(20)