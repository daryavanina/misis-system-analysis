from math import e, log2


def main(v: tuple[list[list]]) -> tuple[float]:
    C = -1/e*log2(1/e)
    k = len(v[0])
    
    ans = []
    for item in v:
        n = sum([sum(row) for row in item])
        H_max = C*n*k
    
        H_s = log2(n-1)
    
        h = H_s/H_max
        ans.append(h)
        
    return tuple(ans)
    
r1 = ([[False, True, True, True, True, False, False], [False, False, False, False, False, True, True], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False], [True, False, False, False, False, False, False], [True, False, False, False, False, False, False], [True, False, False, False, False, False, False], [True, False, False, False, False, False, False], [False, True, False, False, False, False, False], [False, True, False, False, False, False, False]], [[False, False, False, False, False, True, True], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [False, False, False, False, False, False, False], [True, False, False, False, False, False, False], [True, False, False, False, False, False, False]], [[False, False, False, False, False, False, False], [False, False, True, True, True, False, False], [False, True, False, True, True, False, False], [False, True, True, False, True, False, False], [False, True, True, True, False, False, False], [False, False, False, False, False, False, True], [False, False, False, False, False, True, False]])

print(main(r1))