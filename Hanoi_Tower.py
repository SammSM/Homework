def Hanoi(Discs, fromm, too):
    by=6-fromm-too
    if Discs==1:
        print(f'Disc_{Discs} from({fromm}) -> to({too})')
    else:
        Hanoi(Discs-1, fromm, by)
        print(f'Disc_{Discs} from({fromm}) -> to({too})')
        Hanoi(Discs-1, by, too)

Hanoi(3, 1, 3)