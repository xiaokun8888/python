def fillable(stock, merch, n):
    # Your code goes here.
    if stock.get(merch,0)>=n:
        return True
    else:
        return False