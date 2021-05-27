def towers(n, start, end, middle):
    if n == 1:
        print("Move %i from tower %s to tower %s" % (n, start, end))
    else:
        towers(n-1, start, middle, end)
        print("Move %i from tower %s to tower %s" % (n, start, end))
        towers(n-1, middle, end, start)

towers(3, 'A', 'B', 'C')
