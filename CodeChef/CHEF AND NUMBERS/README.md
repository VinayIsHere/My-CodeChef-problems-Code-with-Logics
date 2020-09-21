Link to this problem is: https://www.codechef.com/problems/RECNDNOS

To view the pdf file to which I have uploaded on repository, You can just donwload that directly.

<b>SIMPLIFYING THE STATEMENT</b>
In simple terms Chef has given some dishes and he has to choose one dish which appears most times but if the adjacent dish of the dish he is selecting is same he won't count that. In more simple terms if I had to explain this problem I will say you will be given some numbers like below:
[1,2,2,1,2,1,1,1,1] and you have to select one distinct number which has appear most time without counting the same adjacent number.

If you still didn't get what I mean, No problem see the below example:
Suppose you have this list: [1,2,2,1,2,1,1,1,1]
the distinct number in this list is [1,2]
and If we count their occurances in the original list then {1: 6,2: 3}, 1 appears 6 times and 2 appears 3 times. But in this question what you have to do is if a number appears consecutively two times you have to count that number appearance as one, like if we apply this approach to this list then 1 will appear 4 times and 2 will appear 2 times only.

Suppose if we replace consecutively appearing number with some character or number (I am taking 'x' here) so the list [1,2,2,1,2,1,1,1,1] will become [1,2,'x',1,2,1,'x',1,'x'] see whenever a number appears second team in sequence we replace it with a character so you can see in the second list 1 is there 3 timers and 2 is there 2 times, in short {1:3,2:2}.

And according to question you have to select a dish which  appears most number of times, so here it is 1.

[Note: If two dishes(or numbers) appears same number of Times, you have to select the lowest number dish. If 1 and 2 both will appear three times then your answer should be 1 because 1<2].

Hope I explain you the problem statement very carefully.

<b>Logic Explanation</b>

First we will take the input of Number of test cases, Which I have done with the following code
```
for _ in range(int(input())):
```
Now I will take the number of dishes input and then dishes number list by code
```
n = int(input())
A = list(map(int, input().split()))
```
Now I will replace every second consecutive occurance of a number to some values(here I am taking 'x' character).

I already define you this thing in "Simplifying The Statement" block. so what we will do we will convert this list [1,2,2,1,2,1,1,1,1] into [1,2,'x',1,2,1,'x',1,'x'] this list by replacing every consecutive second appearance of that number with some character so that at last we will just count the number of occurances of distinct dishes and will print the dishes which appears most time.

So here's my python code for this

```
for i in range(n-1):
	if A[i] == A[i+1]:
		A[i+1] = 'x'
```
so now i need to count the occurance of the most appear value and just print that dish number. Remeber we also need to check when the count of the most appear dish is same we need to print the less value dish number. Which I implement by the following code:

```
y = A[0]
count = A.count(A[0])
for j in range(n):
	if A[j] != 'x':
		temp = A.count(A[j])
        if temp > count:
                count = temp
                y = A[j]
       elif temp == count:
                count = temp
                if y > A[j]:
                	y = A[j]
```
Don't worry it's not that much complecated. So what I've done here is that I am using variable ```y``` to store the dish number and ```count,temp``` just to store their number appearances.
So first I assign the first values of the list to ```y``` and counts it's appearance in ```count``` variable and then loop through whole list, Here the line 
```
if A[j] != 'x':
```
means to exclude the counting of appearance of the character which we have used to replace the consecutive appears dublicate.
So inside this ```if``` condition I am just counting the appearance of the current number and if it's count is bigger than the previously store value in ```count``` variable we assign that dish number to ```y``` with it's count to ```count``` variable and the statement
```
elif temp == count:
	count = temp
	if y > A[j]:
		y = A[j]
```
will be evaluated if both the values will be same, Here I am just comparing the ```y``` value with the current ```A[j]``` values and assign the small dish number to ```y``` variable and at last just printing our output:
```
print(y)
```
Which is the dish number appears most of the time without considering it's second consecutive occurace in the list.

If you face any problem to understand this logic you can ping me on my instagram which is: vinayk9119.
