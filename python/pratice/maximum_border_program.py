#this is the solution of maximum border calculating
#problem stetment from hackerearth https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/maximum-border-9767e14c/
"""sample input
2
2 15
.....####......
.....#.........
7 9
...###...
...###...
..#......
.####....
..#......
...#####.
........
sample output
2
5
"""
t = int(input())
while t>0:
    t -= 1
    n,m = map(int,input().split(maxsplit=1))
    count = 0
    for i in range(0,n):
        bor = (input()[:m+1]).replace('.','')
        if count < len(bor):
            count = len(bor)
    print(count)