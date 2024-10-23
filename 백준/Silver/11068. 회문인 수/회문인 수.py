def is_palindrome(s):
    return s == s[::-1]

def to_base(n, base):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    result = ""
    while n > 0:
        n, remainder = divmod(n, base)
        result = chars[remainder] + result
    return result

def check_palindrome_in_bases(n):
    for base in range(2, 65):
        converted = to_base(n, base)
        if is_palindrome(converted):
            return 1
    return 0

T = int(input())
numbers = [int(input()) for _ in range(T)]

for num in numbers:
    print(check_palindrome_in_bases(num))
