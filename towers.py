def towers(n, start, end, middle):
    if n == 1:
        print(f"Move {n} from tower {start} to tower {end}")
    else:
        towers(n-1, start, middle, end)
        print(f"Move {n} from tower {start} to tower {end}")
        towers(n-1, middle, end, start)


towers(2, 'A', 'C', 'B')
