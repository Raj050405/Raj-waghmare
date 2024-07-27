def palindrome(num):
    reverse = ""
    for x in num:
        reverse = x + reverse
    print(reverse)
palindrome("10201021")