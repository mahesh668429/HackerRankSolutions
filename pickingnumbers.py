def pickingnumbers(a):
    # Write your code here
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if abs(a[j] - a[i]) <= 1:
                ans = max(ans, j - i + 1)
    return ans


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(pickingnumbers(a))