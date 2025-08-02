# write a program to buy the stock and sell it inorder to get the maximum profit from it 
def buystock_sellstock(prices):
    min_price = float('inf') # edar infinite lere bcz 7 < inf aisa toh min price 7  aata 
    max_price = 0 
    for elements in prices:
        if elements < min_price:
            min_price = elements
        elif elements - min_price > max_price:
            max_price = elements - min_price
    return max_price
prices = [7,1,5,3,6,4]
print(buystock_sellstock(prices))