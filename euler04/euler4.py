#!/usr/bin/python3

'''
Find the largest palindrome made from the product of two 3-digit numbers
'''


def is_palindrome(text):
    str_len = int(len(text) / 2)
    for i in range(str_len):
        if text[i] != text[-(i+1)]:
            return False
    return True

biggest = 0
for num1 in range(999, 100, -1):
    for num2 in range(999, 100, -1):
        result = num1 * num2
        # skips looping for numbers that can't beat biggest
        if result < biggest:
            break

        if is_palindrome(str(result)):
            if result > biggest:
                biggest = result
                break

print(biggest)
