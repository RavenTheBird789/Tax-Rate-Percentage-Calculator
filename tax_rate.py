# Tax Rate Percentage Evaluation Program

def tax_rate():
    initial_price = float(int(input("Initial Price: "))); # ask user for listed price of something
    final_price = float(int(input("Final Price: "))); # ask user the final price paid for something after tax

    diff = final_price - initial_price # evaluate the difference between the final price after tax and the price listed

    formula = diff / initial_price * 100 # evaluate the tax percentage using this formula
    
    mes = f"The current tax rate based on your purchase is {formula}"
    print(mes); # show the user the current tax rate based on their purchase
tax_rate();
