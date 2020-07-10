if __debug__:
	import sys
	sys.stdin = open('inputpy.txt', 'r')
	sys.stdout = open('outputpy.txt', 'w')

def merge(a, b):
	i, j = 0, 0
	n, m = len(a), len(b)
	l = list()
	while(i != n and j != m):
		if(a[i] < b[j]):
			l.append(a[i])
			i += 1
		else:
			l.append(b[j])
			j += 1
	l.extend(a[i:])
	l.extend(b[j:])
	return l

a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = merge(a, b)
print(*l)