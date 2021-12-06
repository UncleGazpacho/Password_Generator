import requests, string, random
import os

# *** Part 1 ***
def checkquota():
    r_url = 'https://www.random.org/quota/?format=plain'
    quota = int(requests.get(r_url).text)
    if quota < 1:
        raise Exception('Quota aufgebaucht!')
    return quota

# *** Part 2 ***
characters = [char for char in string.printable]
remove = [' ', '\t', '\n', '\r', '\x0b', '\x0c']
characters = [elem for elem in characters if elem not in remove]

def get_rando_numbers(num):
    checkquota()
    numbers = requests.get('https://www.random.org/integers/?num={}&min=0&max={}&col=1&base=10&format=plain&rnd=new&format=plain'.format(num, len(characters)-1)).text.split('\n')
    numbers.remove('')
    return numbers

# *** Part 3 ***
def generate_pwd(num):
    pwd = ''
    random.shuffle(characters)
    numbers = get_rando_numbers(num)
    for number in numbers:
        pwd += characters[int(number)]
    return print(pwd)

num = input('Please enter the length of your password! ')
generate_pwd(num)
