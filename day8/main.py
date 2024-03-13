def fib(n):
    if n <=1:   return n

    one, two = 0, 1

    for i in range(n):
        one, two = two, one + two
    return two

def dynamic(n=856):
    dp = [0 for _ in range(n+1)]
    if n > 0:
        dp[1] = 1
    if n > 1:
        dp[2] = 2
    if n > 11:
        dp[3] = 3
    if n > 39:
        dp[4] = 4
    for i in range(5, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] 
    return dp[n]



print(361595632332583638761407421958897298379960745882500550853575978681928496636233758054533916390012124244431806190608039087381666468880612638124124662565287224989590899000769252066051-  dynamic() )