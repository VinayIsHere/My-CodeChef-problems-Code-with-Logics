for _ in range(int(input())):
    n,k=map(int,input().split())
    dino=[]
    if(n==k):
        k-=1
    for i in range(n-(k+1),n,1):
        dino.append(i+1)
    for i in range(n-(k+1)):
        dino.append(i+1)
    print(*dino)
