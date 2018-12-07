def permute(s):
    if len(s) == 0:
        return [[]]

    ret = [s[0:1] + x for x in permute(s[1:])]

    for i in range(1, len(s)):
        if s[i] == s[0]:
            continue
        s[0], s[i] = s[i], s[0]
        ret += [s[0:1] + x for x in permute(s[1:])]

    return ret

#s = [int(i) for i in input().split()]
s=[6, 12]
for x in permute(s):
    for i in range(len(x)):
        x[i]=x[i]+i
    if(x==sorted(x)):
        print(x)