## 풀이 1
# deque 자료구조에 원소들을 저장해서 popleft로 하나씩 꺼내버리고 rotate 함수로 회전시키는 풀이
# pop을 두 번 하는 대신 rotate 함수를 씀으로써 시간 복잡도를 줄일 수 있음
import sys
from collections import deque

a = int(input())
lst = deque([i for i in range(1, a+1)])

while len(lst) > 1: # 길이가 1이 되면 while문 멈추겠다
    lst.popleft() # deque를 쓰면 pop(0)을 할 필요 없이 popleft를 써서 왼쪽값을 그냥 pop 할 수 있어서 편리함
    lst.rotate(-1) # 왼쪽으로 한 칸씩 돌림 (rotate(1) 하면 오른쪽 방향이고 이게 디폴트)
    #print(lst)

print(lst[0])

# while 문 안에서 print 찍어보면 다음과 같이 진행됨
#deque([3, 4, 5, 6, 2])
#deque([5, 6, 2, 4])
#deque([2, 4, 6])
#deque([6, 4])
#deque([4])


## 풀이 2
# 풀이 1에서는 밑으로보내는 카드를 rotate를 써서 보냈는데, 그냥 pop한걸 다시 append 해줘도 된다. 
import sys
from collections import deque

a = int(input())
lst = deque([i for i in range(1, a+1)])

while len(lst) > 1: # 길이가 1이 되면 while문 멈추겠다
    lst.popleft() # 하나 버리고
    lst.append(lst.popleft()) # 하나는 뽑은다음에 맨밑에다 추가 
    #print(lst)

print(lst[0])

# 풀이 1/ 풀이 2 각각의 메모리: 55040 / 55012 (KB)
# 풀이 1/ 풀이 2 각각의 런타임 시간: 208 / 204 (ms)
# 큰 차이 없음
