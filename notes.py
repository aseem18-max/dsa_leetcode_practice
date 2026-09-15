s = input()
new_s = ''
l = set()
l.add(0)
for i in s:
    if i not in new_s:
        new_s = new_s + i
    else:
        l.add(len(new_s))
        new_s = new_s[new_s.index(i) + 1:] + i
    l.add(len(new_s))
print(max(l))
