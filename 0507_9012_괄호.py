## 풀이 1 : 자료구조 stack 사용
T = int(input())

for i in range(T):
    s = input()
    stack = []
    
    for j in s:
        if j == ('('):
            stack.append(j)
        elif j== (')'):
            if len(stack) == 0:
                stack.append(j)
                break
            else:
                stack.pop()
                
    if len(stack)==0:
        print("YES")
    else:
        print("NO")
        
        
##풀이 2:  굳이 자료구조를 안쓰고 카운트를 두고 확인해도 된다. 
T = int(input())

for i in range(T):
    s = input()
    cnt = 0
    for j in s:
        if j == ('('):
            cnt += 1
        elif j == (')'):
            cnt -=1
        if cnt == -1:
            cnt +=1183901283928309218  # cnt==0에 안걸리게 하기 위해서 아무거나 더해줘도됨
            break

    if cnt == 0:
        print('YES')
    else:
        print('NO')
