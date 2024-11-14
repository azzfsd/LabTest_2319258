import csv



#--------- Start of Functions to be implemented for Lab Test 1 -----------------------

##########################################################
# Function to check if the price range is valid          #
# Parameters:                                            #
#  'price_lower_limit': Lower limit price (String type)  #
#  'price_lower_upper': Upper limit price (String type)  #
#                                                        #
# Return value:                                          #
#   'result': True / False (Boolean type)                #
##########################################################
def is_price_range_valid(price_lower_limit, price_upper_limit):
    result = True

    # Add your implementation from here


    return result

##################################################################
# Function to calculate overall average expenses                 #
# Parameters:                                                    #
#  'csv_list': List containing the CSV file contents (List type) #
#                                                                #
# Return value:                                                  #
#    average: Calculated overal averae expenses                  #
##################################################################
def calc_average_expenses(csv_list):
    average = 0

    # Add your implementation from here
    #HINT start with this code: for item in csv_list:



    return average

##################################################################
# Function to calculate Total expenses                           #
# Parameters:                                                    #
#  'csv_list': List containing the CSV file contents (List type) #
#                                                                #
# Return value:                                                  #
#    total_expenses: Calculated overall Total expenses           #
##################################################################
def calc_total_expenses(csv_list):
    total_expenses = 0

    # Add your implementation from here
    #HINT Start with this code: for item in csv_list:


    return total_expenses

##############################################################
# Function to get all items within a price range             #
# Parameters:                                                #
#  'str_price_lower_limit': Lower limit price (String type)  #
#  'str_price_lower_upper': Upper limit price (String type)  #
#                                                            #
# Return value:                                              #
#   'result': List containing items found within price range #
#                                                            #
##############################################################
def get_items_by_price_range(csv_list, str_price_lower_limit, str_price_upper_limit):
    result = []

    # Add your implementation from here
    #HINT start with this code: for item in csv_list:


    return result

##################################################################
# Function to display all items in alphabetical order            #
# Parameters:                                                    #
#  None                                                          #
#                                                                #
# Return value:                                                  #
#   'result': List containing items sorted in alphabetical order #
#                                                                #
##################################################################
def sort_by_items(csv_list):
    result = []

    # Add your implementation from here

    return result

#--------- End of Functions to be implemented for Lab Test 1 -----------------------


##########################################################
# Function to display the main menu of the applicaition #
# Parameters: None                                      #
# Return value = None                                   #
#########################################################
def display_main_menu():

    print("\n----- Expense Tracker -----")

    print("Select option\n")

    print("1 - Display all records")
    print("2 - Display statistics")
    print("3 - Display items within price range")

    print("Q - Quit")

    option = input("Enter selection =>")

    #load CSV textfile database
    csv_list = load_csv_database()

    # Display all records
    if option == '1':
        display_all_records(csv_list)

    # Calculate and display expenses statistics
    elif option == '2':
        get_expenses_statistics(csv_list)

    # Display items by price
    elif option == '3':
        # Get price range from user via console
        price_lower_limit = input("Price (Lower Limit) = ")
        price_upper_limit = input("Price (Uper Limit) = ")

        #Check if valid price range has been entered by the user
        if is_price_range_valid(price_lower_limit, price_upper_limit):
            # Get all items within selected price range
            result_list = get_items_by_price_range(csv_list, price_lower_limit, price_upper_limit)

            # Display items found within selected price range
            display_results(result_list)
        # Invalid price range
        else:
            print("\nInvalid Price Range entered !")

    # Quit application
    elif option == 'Q':
        print("Thank You and have a nice day :-)")
        quit()


##########################################################
# Function to read from a text CSV file                  #
# Parameters: None                                       #
#                                                        #
# Return value:                                          #
#   'csv_list': List containing the CSV file data        #
##########################################################
def load_csv_database():
    print("\nLoading CSV file database")

    with open('expenses.csv', mode='r') as csv_file:
        csv_dict = csv.DictReader(csv_file)

        csv_list = list(csv_dict)

        return csv_list


###########################################################
# Function to display results on the console              #
# Parameters:                                             #
#  'result_list': List containing the results (List type) #
#                                                         #
# Return value: None                                      #
#                                                         #
###########################################################
def display_results(result_list):
    for item in result_list:
        print(item["date"] + "\t\t" + item["expense_item"] + "\t\t" + item["price"])


##################################################################
# Function to display all records from CSV file  on the console  #
# Parameters:                                                    #
#  'csv_list': List containing the CSV file contents (List type) #
#                                                                #
# Return value: None                                             #
#                                                                #
##################################################################
def display_all_records(csv_list):

    print("Date\t\t\tExpense Item\t\tPrice")

    for item in csv_list:
        print(item["date"] + "\t\t"+ item["expense_item"] + "\t\t\t\t" + item["price"])



##################################################################
# Function to display statistics for expenses                    #
# Parameters:                                                    #
#  'csv_list': List containing the CSV file contents (List type) #
#                                                                #
# Return value: None                                             #
#                                                                #
##################################################################
def get_expenses_statistics(csv_list):
    print("\nExpenses Statistics")
    print("-------------------")

    print("Total Expenses = $" + str(calc_total_expenses(csv_list)));
    print("Average Expenses = $" + str(calc_average_expenses(csv_list)))



#############################
# Main Functin              #
# Parameters: None          #
#                           #
# Return value: None        #
#                           #
#############################
def main():

    while (True):
        display_main_menu()


if __name__ == "__main__":
    main()




