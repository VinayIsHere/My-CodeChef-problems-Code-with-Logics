Link to this problem is: https://www.codechef.com/problems/MXCH

To view the pdf file to which I have uploaded on repository, You can just donwload that directly.

<b>Simplifying the Problem statement</b>
Let's simplify the statement.
The statement is preety confusing but it's very simple problem to solve, In short, Question is telling us to rearrange the number into ascending order, It means when it give you N and K, If you have arrange the last K elements of list containing integers values 1 to N in ascending order.

If you didn't get the above paragraph no problem, let me elaborate this more.
Accoridng to question the ball will be at the left most player means the 1st element of list and question is telling us he will throw the ball to it's right side to that dinosaur whose height is bigger than him means an integer values which is bigger than the 1st value present in list. You need to repeatedly do this operation till the ball reach to the highest integer value( or you can say to a dinosaur who is tallest).

<b> Logic Explanation </b>

Let's elaborate with an example:
Suppose they give you the N=10 and k=3
It means you need to throw the ball to the heighest dinosaur in just 3 passes and initially the ball will be present to the 1st value in the list.

So 1st of all we will create the list, As it has given us N=10 so initially our list will be equal to [1,2,3,4,5,6,7,8,9,10]. Now consider the value of k which is 3. So what we need to do is that we need to pass the ball to the value 10 in three passes so we need to change our list accordingly as I told you we just need to take last k+1 elements and just put them in start in reverse order. So the answer of this question will equal to [7,8,9,10,1,2,3,4,5,6]. The ball will reach to the heighest dinosaur in three passes as follows:
```
7->8->9->10
```
1st from 7 to 8
2nd from 8 to 9
3rd from 9 to 10
As we can see there is no bigger value present in right of the value 10 so this list will be our answer.

<b> Working Of Code </b>

So first we will need to take the input of the number of test cases and then the value of N and K, which will be done by the following code:

```
for _ in range(int(input())):
    n,k=map(int,input().split())
```

Now I am check whether the value of N and K is equal or not if they are equal we just simple print the pattern for 1 to N, In code I am subracting k by 1 so that my other portion of code will not generate an error.

It is done by following code:

```
if(n==k):
	k-=1
```
Now I am just initializing the starting of the list with the value N-(K+1) which means if our N is 10 and K is 3 then the starting 4 elements of the list will be [7,8,9,10] which is done by the following code

```
for i in range(n-(k+1),n,1):
	dino.append(i+1)
```

Now i just appended the remaining values which are missing (for example in our test case these values are [1,2,3,4,5]) at the end of the list by the following code:

```
for i in range(n-(k+1)):
	dino.append(i+1)
```

Now I just print out the element in list by code
```
print(*dino)
```

If you face any problem to understand this logic you can ping me on my instagram which is: vinayk9119

