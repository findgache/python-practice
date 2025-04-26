def reversestring(r):
    reversed=""
    for char in r:
        reversed = char + reversed
    return reversed
print(reversestring("Good"))