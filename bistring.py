"""
s = input()
pre = '1'
"""

seq = []
count = 0
for c in s:
    if c == pre:
        count += 1
    else:
        pre = c
        seq.append(count)
        count = 1