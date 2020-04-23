# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:09:03 2020

@author: Menios
"""

import requests 
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}')
    return res

    
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    print(hash_to_check)
    for h, count in hashes:
        if h == hash_to_check:
            exit
            return count
    return 0
    
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        
        if count:
            print(f'{password} found {count} you should change your password')
        else:
            print(f'{password} not found')
    return 'done'


if __name__ == '__main__':
  main(sys.argv[1:])