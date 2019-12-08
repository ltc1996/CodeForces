# 393A: [Nineteen](https://codeforces.com/problemset/problem/393/A)

string = input()

d = {}
d['n'] = d['e'] = d['i'] = d['t'] = 0

for i in string:
    if i in d:
        d[i] += 1

res = min(max(0, (d['n'] - 1) // 2), d['e'] // 3, d['i'], d['t'])

print(res)
