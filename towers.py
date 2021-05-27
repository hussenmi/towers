def towers(n, start, end, middle):
    if n == 1:
        print("Move %i from tower %s to tower %s" % (n, start, end))
        # print(f"Move {n} from tower {start} to tower {end}")
        # moves += 1
    else:
        towers(n-1, start, middle, end)
        print("Move %i from tower %s to tower %s" % (n, start, end))
        # print(f"Move {n} from tower {start} to tower {end}")
        # moves += 1
        towers(n-1, middle, end, start)

    # print(moves)

towers(2, 'A', 'C', 'B')
