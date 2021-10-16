# pycharm code for assignment 1

import matplotlib.pyplot as plt  # import matplotlib to plot the bar chart
# constants for menu choices
display_1 = '1'
display_2 = '2'
display_3 = '3'
display_4 = '4'
display_5 = '5'
display_6 = '6'
display_7 = '7'
QUIT = '8'


# create an empty list to store and manipulate the text file
book_list = []

def main():
    # the choice variable controls the loop
    # and stores the users choice
    choice = 0
    while choice != QUIT:  # while the users choice isn't quit then display the menu
        display_menu()  # menu function called

    # ask the user what they want to do
        choice = input('What task would you like to perform? ')

        if choice == display_1:  # the user picks a choice and the allocated function is called
            summary()
            titles()
            total_value()
        elif choice == display_2:
            average_value()
        elif choice == display_3:
            tally_genre(book_list)
        elif choice == display_4:
            x = average_value()
            add_book()
            titles()
            y = average_value()
            difference = (y-x)  # calculation to store the old average and find the cost difference
            print('-------------------------------------------- Cost difference --------------------------------------')
            print('The cost difference between the averages is £', format(difference, '.2f'))
        elif choice == display_5:
            stock_level()
        elif choice == display_6:
            Order(book_list)
        elif choice == display_7:
            chart()
        elif choice == QUIT:
            print('Exiting the program')
        else:
            print('Error: Invalid input') # if 1-8 isn't entered the user is told to choice a correct value

def display_menu():
    print(' ----------------------------------------------MENU--------------------------------------------------------')
    print('[1] Display the details of all books, including the total number of tiles and total value of the stock ')
    print('[2] Display the average price of books that are in stock ')
    print('[3] Display the number of books in each genre')
    print('[4] Add a new book and output the increase of titles in stock and the cost difference in the average price')
    print('[5] Query if a book is available and increase or decrease the stock')
    print('[6] Order books by alphabetic order by title or genre')
    print('[7] Plot a bar chart that presents the number of books in each genre')
    print('[8] Quit the program')
    # menu to display the options
def read_file():
    # open the file for reading
    book_file = open("booklist.txt", "r")
    # read the file row by row
    for row in book_file:
        if not row.startswith('#'):  # if the row starts with # don't read in
            row = row.rstrip('\n').split(', ')  # strip , from the list
            book_list.append(row)   # append the book details into the list
    book_file.close()

def summary():
    print('------------------------ Book Details ----------------------')
    for book_details in book_list:
        for row in book_details:  # go through each row in the list
            print(row, " ", end='')  # this tidy's up the list and ends the output with a space
        print()  # print a list of the book details

def titles():
    book_titles = len(book_list)  # count the length if the books list and print it
    print('-----------------------------------------------------------------------------------------------------------')
    print('There are', book_titles, ' book titles available to choose from')
    print('-----------------------------------------------------------------------------------------------------------')

def total_value():
    total = 0  # set an accumulator to be able to total the count
    for book in book_list:  # use a for loop to iterate through the list
        total += float(book[4]) * int(book[5])  # the total will be row 4 (the price) * row 5 (the stock)
    print('-----------------------------------------------------------------------------------------------------------')
    print('The total price of the books in stock is currently £', format(total, '.2f'))
    # format total to 2 decimal places

def average_value():
    print('-------------------------------------------- Average Price ------------------------------------------------')
    stock = 0  # set the accumulator
    for book_stock in book_list:  # use a for loop to search for stocks
        if int(book_stock[5]) > 0:  # only count if stock is over 0
            stock += (float(book_stock[4]))  # add the price of all the books that are in stock
        avg = stock / len(book_list)  # calculate average by dividing total stock by length of list
    print('The average price of a book is currently £ ', format(avg, '.2f'))  # format average to 2 decimal and print
    return avg  # return the avg to use for finding the difference of two averages
    # take this price and then divide it by the length of the list available titles


def tally_genre(book_list):
    print('------------------------------ Titles ---------------------------------------------------------------------')
    # create a dictionary to hold details
    genre_dict = {}

    for category in range(len(book_list)):  # step through the booklist using a for loop
        genre = book_list[category]        # to see if name is in the dictionary
        if genre[6] in genre_dict:  # use an if statement so the code can make a decision
            genre_dict[genre[6]] = genre_dict[genre[6]] + 1  # *int(genre[5]) # if genre found add to value count
        else:
            genre_dict[genre[6]] = 1  # int(genre[5]) # if a genre is found and no other genre like it is found then
                                                      # only add 1 to the count
    for key, value in genre_dict.items():
        print('There are', value, key, 'Titles to choose from')  # print the value (num of genres) and key (genre name)
def add_book():
    # create a new list to store details
    add_new = []
    try:  # exception in case user inputs wrong value eg str where it can only be an int
        # ask the user for the input
        author = input('Enter the Author: ')
        add_new.append(author)
    # write the input to the file
    # repeat this for the other details
        title = input('Enter the title: ')
        add_new.append(title)

        format = input('Enter the Format: ')
        add_new.append(format)

        publisher = input('Enter the Publisher: ')
        add_new.append(publisher)

        cost = float(input('Enter the Cost: '))  # convert to float because its a number that could have decimal places
        add_new.append(cost)

        stock = int(input('Enter the Stock: '))  # convert to integer because its a whole number
        add_new.append(stock)

        genre = input('Enter the Genre: ')
        add_new.append(genre)

        # add the new book to the original list
        book_list.append(add_new)
        print('Book details added to inventory')
        # this will occur when user try's to enter a str in stock/cost
    except ValueError:  # value error for cost and stock since they are numbers (float/int)
        print('---------------------------------------------------')
        print('Try again and enter a correct numerical value')
        print('---------------------------------------------------')

def stock_level():
    book_name = input('What item are you searching for? ')  # create a variable and ask the user to enter it
    for title in book_list:  # loop through to find book_name variable
        if book_name in title:  # if it is found in the list then print that it has been found
            print(book_name, 'Is available.')
            stock = input('To increase stock [1] or to decrease stock [2] ')  # create variable and ask for input
            if stock == '1':
                increase = int(input('How much would you like to increase the stock by? '))  # refer to row 5 in the lis
                (title[5]) = int(title[5]) + int(increase)  # and then increase that number by the users input
                print('-----------------------------------------------------------------------------------------------')
                print('The stock level has been increased by', increase)
                print('The stock level is now ', title[5])  # print final stock level
            if stock == '2':
                decrease = int(input('How much would you like to decrease the stock by? '))
                (title[5]) = int(title[5]) - int(decrease)
                print('-----------------------------------------------------------------------------------------------')
                print('The stock level has been decreased by', decrease)
                print('The stock level is now', title[5])
        if title[5] == 0:
            print('This book is now out of stock')  # if stock is equal to zero then display this

def Order(book_list):
    option = input('To order by title press [1] or to order by genre press [2]: ')  # ask user to select input
    print('\n')  # take a new line to make it look nice
    if option == '1':
        print('------------------- Books sorted by Title ---------------------------')
        title = sorted(book_list, key=lambda x: x[1])  # create a variable and sort it using lambda function
        for x in title:                                # using lambda sorts only the 2nd row alphabetically
            print(x)                                   # using for loop to go through the variable list and print it
                                                       # neatly
    if option == '2':
        print('------------------- Books sorted by Genre ---------------------------')
        genre = sorted(book_list, key=lambda x: x[6])
        for y in genre:
            print(y)

def chart():
    genre_dict = {}

    for i in range(len(book_list)):                             # using the same code for task 3 , use a dictionary to
        genre = book_list[i]                                    # find the total amount of books in each genre (value)
        if genre[6] in genre_dict:                              # and use dictionary function to get the names of the
            genre_dict[genre[6]] = genre_dict[genre[6]] + 1     # genres (key)
        else:
            genre_dict[genre[6]] = 1

    for key, value in genre_dict.items():
        plt.bar(key, value)                                 # use plt to plot the bar chart and assign the values for
    plt.xlabel("Genres")                                    # the x and y axis , key = x axis and value = y axis
    plt.ylabel("Stock")                                     # give appropriate  names to the label and titles
    plt.title("Number of titles available by genre")        # show the bar char
    plt.show()

read_file()
main()
# call read file so it can be used by all functions and then call main to enter the program 
