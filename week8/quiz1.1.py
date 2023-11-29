def cut_rod1(p, n):
    if n == 0:
        return 0
    q = -10**7
    for i in range(n):
        q = max(q, p[i] + cut_rod1(p,n-i))
    return q





print(cut_rod1([1,5,8,9,10], 4))