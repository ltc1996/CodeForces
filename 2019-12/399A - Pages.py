# 399A: [Pages](https://codeforces.com/problemset/problem/399/A
# )

nums = input().split(' ')
n, p, k = [int(i) for i in nums]

front = last = ''
if p - k > 1:
    front = '<< '
if p + k < n:
    last = ' >>'

f, l = [], []
for i in range(max(1, p - k), p):
    f.append(str(i))
for i in range(p + 1, 1 + min(n, p + k)):
    l.append(str(i))
res = front + ' '.join(f + ['(' + str(p) + ')'] + l) + last

print(res)
