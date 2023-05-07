## 풀이: 파이썬 내장함수 sort 이용
n,m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int, input().split()))
res = []

res = a+b
res.sort()

print(" ".join(map(str, res)))

## 풀이 2(참고): 투포인터 (Merge sort)
# 애초에 A,B가 정렬되어 있다는 조건이 있기에 가능한 풀이이다. 
# (처음에 위 조건을 못보고 어떻게 이 풀이가 가능하지? 생각하며 헤맸다..!)

n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0 
b = 0 

res = []

while a != len(A) or b != len(B):
    if a == len(A): # a 포인터가 A배열의 끝에 다 오면
        res.append(B[b]) # B배열의 값 추가
        b += 1

    elif b == len(B): # b 포인터가 B 배열의 끝에 다왔다면
        res.append(A[a]) # a 배열의 값 추가
        a += 1
    else: # A,B 비교해서 더 작은 값 넣어줌
        if A[a] < B[b]:
            res.append(A[a])
            a += 1
        else:
            res.append(B[b])
            b += 1
    
print(" ".join(map(str, res)))
