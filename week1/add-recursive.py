#덧셈
# 재귀 연습을 위하여 덧셈을 하는 재귀 함수를 백지에서 작성해봅니다.

t = int(input())
f = 1

def add_from_to(f,t):
    if f >= t :
        return t
    return add_from_to(f,t-1)+t


print(add_from_to(f,t))