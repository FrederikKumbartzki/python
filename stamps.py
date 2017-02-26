def stamps(n):
    five = str(n / 5)
    rest = n % 5

    two = str(rest / 2)
    rest = rest % 2

    one = rest

    print int(five), int(two), one




stamps(50)
