#!/usr/bin/env python3
for _ in range(int(input())):
	n = int(input())
	val = list(map(int,input().split()))
	
	x = max(val)
	val.remove(x)
	
	y = min(val)
	val.remove(y)
	
	z = min(val)
	val.remove(z)
	
	print(abs(x-y)+abs(y-z)+abs(z-x))
