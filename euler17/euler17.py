#!/usr/bin/python3

'''
If the numbers 1 to 5 are written out in words:
    one, two, three, four, five
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
    342: (three hundred and forty-two) is 23 letters
    115: (one hundred and fifteen) is 20 letters
'''

import time


start = time.time()


digits = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
        90: 'ninety'}

def get_name(num):
    if num <= 20: # value is in digits dict
        return digits[num]
    elif num < 100: # break into tens and ones, search digits
        r = num % 10
        tens = num - r
        return digits[tens] + digits[r]
    elif num < 1000: # break into hundreds, recurse with remainder
        r = num % 100
        hund = int((num - r) / 100)
        result = digits[hund] + 'hundred'
        if r > 0:
            result += 'and' + get_name(r)
        return result
    else:
        return 'onethousand'

total = 0
for i in range(1, 1001):
    total += len(get_name(i))

print(total)

end = time.time()
print('{}s'.format(end-start))
