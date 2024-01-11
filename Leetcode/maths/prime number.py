def countPrimes(n):
    if n < 3:
        return 0
    li = [1] * n
    li[0] = li[1] = 0
    primes = []
    # 这里从第3个元素开始遍历，遍历到列表长度的平方根位置len(n**0.5)即可
    for i in range(2, int(n ** 0.5) + 1):
            # 将当前元素的倍数位置(从i*i算起，因为上面遍历到int(n**0.5)为止)的元素都替换成"0"
            li[i * i:n:i] = [0] * len(li[i * i:n:i])
    # print(primes)
    for j in range(n):
        if li[j] == 1:
            primes.append(j)
    print(sum(li))
    print(li)
    # for j in primes:
    #     print(j)
    print(primes)
    return

countPrimes(16)


