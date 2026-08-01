

letter_count = {
    '2':3,
    '3':3,
    '4':3,
    '5':3,
    '6':3,
    '7':4,
    '8':3,
    '9':4
}

def count_sequence(s:str)->int:
    def ways_for_group(length,k):
        dp = [0]*(length+1)
        dp[0]=1
        for n in range(1,length+1):
            for step in range(1,k+1):
                if n-step>=0:
                    dp[n]+=dp[n-step]
        return dp[length]
    # find number of grouping for consecutive same numbers
    i=0
    n=len(s)
    groups = []
    while i<n:
        j=i
        while j<n and s[i]==s[j]:
            j+=1
        groups.append((s[i], j - i))
        i=j


    result = 1
    for digit, length in groups:
        k = letter_count.get(digit, 1)
        result *= ways_for_group(length, k)

    return result


print(count_sequence("22233"))