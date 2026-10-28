shopping_amount=int(input("enter shopping amount: "))
if shopping_amount>1000:
    discount=shopping_amount*0.1
    final_amount=shopping_amount-discount
    print("final amount after discount is:",final_amount)