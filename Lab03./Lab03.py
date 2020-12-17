# Name: Eupheng Vue
# Class: CSCI 1411
# File: EuphengVueLab03.py
# This lab is a program that asks the user input of length
# and width of a box in inches.
# It calculates the perimeter of the box, how many trims
# boards the user will need,
# the cost of the total trim boards, 
# how much trim is wasted, and
# how much money the user wasted.

def main():
    full_name = ( input ( 'Enter your full name: '))  # Prompts user input full name

    print(full_name) # prints the user's input of full name

    length_box = int ( input ('Enter the length of the box in inches: ' ))   # prompts user input for the length of the box

    width_box = float ( input ('Enter the width of the box in inches: ' ))   # prompts user input for the width of the box

    perimeter_box = ( 2 * length_box ) + ( 2 * width_box)    # perimeter formula of the input length & width of the box

    segment_trim = 12      # total of inches per segement trim

    price_trime = 12       # price per segment trim

    total_trim = round ( perimeter_box / segment_trim)       # formula for total trim the user needs for the box

    total_price_trim = ( total_trim * price_trim )            # total price of the total trim the user needs

    loss_trim = round( ( ( segment_trim * total_trim ) - perimeter_box ), 3 )       # total trim wasted forumla

    loss_money = round( ( ( loss_trim/segment_trim ) * price_trim ), 2 )          # total loss of money from the wasted trim
