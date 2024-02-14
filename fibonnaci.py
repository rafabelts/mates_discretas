def fibonnaci(n):
    
    print(f"{n}")
    if n == 1:
        return n
    elif n == 2:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)
fibonnaci(4)
