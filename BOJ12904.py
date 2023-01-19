# A와 B - 골드 5
    
S = [*input()]
T = [*input()]

while len(S) != len(T):
    if T.pop() == 'B':
        T = T[::-1]

print(1) if S == T else print(0)
