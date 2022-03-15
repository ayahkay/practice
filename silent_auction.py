#10/02/2022
#Ayah Kayed

def check_number(message, lower_boundary):
    while True:
        try:
            user_input = float(input(message))
            if user_input > lower_boundary:
                return user_input
            else:
                print(f"Please input  a number over {lower_boundary}!")
        except ValueError:
            print("Please input a valid number in integers only!")

def get_reserve():
    reserve_price = check_number("What is the reserve price?\n$", 0)
    return reserve_price

def determine_winner():
    bidder_name=""
    highest_bid=0
    while bidder_name!="E":
        bidder_name=input("What is your name? Press 'E' to end\n").title()
        if bidder_name!="E":
            new_bid = check_number("What is your bid?\n$",0)
            if new_bid > highest_bid:
                winner_name = bidder_name
                highest_bid = new_bid
    return winner_name, highest_bid

def print_summary(winning_bidder, reserve_price, winning_bid):
    if winning_bid > reserve_price:
        print(f"Auction won by {winning_bidder} with a bid of ${winning_bid:.2f}")
    else:
        print("Auction did not meet reserve price")

#main
reserve_price = get_reserve()
winning_bidder, winning_bid=determine_winner()
print_summary(winning_bidder, reserve_price, winning_bid)
