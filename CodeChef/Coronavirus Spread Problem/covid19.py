for _ in range(int(input())):
	n=int(input())
	pos=list(map(int,input().split()))
	distance=list()
	count=0
	for k in range(len(pos)-1):
		distance.append(abs(pos[k]-pos[k+1]))
	max_dis=[]
	for i in distance:
		if(i<=2):
			count+=1
		else:
			max_dis.append(count)
			count=0
	max_dis.append(count)
	print(min(max_dis)+1,max(max_dis)+1)
		
