Link to this problem is: https://www.codechef.com/problems/COVID19

<b>Simplifying the Problem statement</b>
As you can read the question, If i simplify their statement it simply means, You have to give two values output one value should indicate the minimum and maximum number of people who will get infected by coronavirus if a person is infected. So two find these two vaues you can consider any guy who will get infected which gives us these numbers. Let me explain this by a test case:

Suppose if we have 5 people:
5 people
1 2 5 6 7 (their distances)

then the output will be:
2(min number) 3(max number)

. In one of the best possible scenarios, the person at the position 1 is infected initially and the virus will also infect the person at the position 2

. In one of the worst possible scenarios, the person at the position 5
is infected initially and the virus will also infect the people at the positions 6 and 7.

Even if the person at position 7 will get infected the people at position 6 and 5 will get infected as their distance is 1 and 2 with 7 respectively.

<b> Logic Explanation </b>
Don't get confused with the problem statement, It's very simple problem to solve let me explain you my code logic line by line and will consider the example statement which I have given in the above paragraph. Okay Let's eleaborate

so first we need to get the input of all the test cases and then iterate through it, which I have done by the following line of code
```
for _ in range(int(input())):
```
Now we need to store the input value for total number of people and then their positions which I have done by the following lines of code
```
n=int(input())
pos=list(map(int,input().split()))
```
Now see we have stored the positoins of the people which are [1,2,5,6,7] (if we consider the problem statement example), Now what I have done is to first create a list( or array in c++ or in c) and then store the difference between these people in this list, so that I will know their distances from each other for this I loop through these people positions store the difference of the current person with respect to the next person in the array. For example for the [1,2,5,6,7] the difference of distances between these people will be equal to this list [1,3,1,1] or if I show you how I calculated this so you can view this list as [2-1,5-2,6-5,7-6].

The python3 code for this is given below:

```
distance=list()
for k in range(len(pos)-1):
	distance.append(abs(pos[k]-pos[k+1]))
```

So, The difference of distance between these people are [1,3,1,1].
So from this list you can see that minimum consecutive values which is less than or equal to 2 (2 is the distance value from the infected person to the normal person) is only 1, and for maximum it's 2, so from here you can see your answer that if the minimum number of people who have distance less than or equal to two is 1, then the minimum number of infected people will be 2 (As the distance 1 indicating the distance between two people) and for maximum it's 3 (1+1=2 which is the distance between 3 people).

The code for doing this operation is given below:
```
max_dis=[]
for i in distance:
	if(i<=2):
		count+=1
	else:
		max_dis.append(count)
		count=0
max_dis.append(count) '''In case if all the people will get infected in both cases this line will save the run time error of empty list'''
```

So your answer for this statement will be 2 3.
which will be given by printing the minimum values+1 and maximum value+1 from our max_dis list

```
print(min(max_dis)+1,max(max_dis)+1)
```

2 is minimum number of people who will get infected in the best scenerio and 3 is the maximum number of people who will get infected in worst scenerio.

If you face any problem to understand this logic you can ping me on my instagram which is: vinayk9119

