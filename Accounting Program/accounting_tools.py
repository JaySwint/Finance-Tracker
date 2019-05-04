"""
Purpose: This program was created to allow its users to create text files that could then later be read by it; printing
        out valuable information related to the balance sheet; including: common size balance sheet, debt ratios, and in
        addition it also features plotting capabilities that allow the user to visually analyze the data via a stacked
        bar graph.

Author: Jay Swint
Date: May 6th, 2019
"""

import numpy as np
import matplotlib.pyplot as plt


def new_file(year, assets, liabilities, equities):

    filename = "BS_" + str(year)
    f = open(filename, 'w')
    #
    asset_list, asset_amounts, sum_assets = dictionary_to_list(assets)
    liability_list, liability_amounts, sum_liabilities = dictionary_to_list(liabilities)
    equity_list, equity_amounts, sum_equities = dictionary_to_list(equities)

    print(year, file=f)
    print("~split1~", file=f)

    for asset in asset_list:
        print(asset, int(assets[asset]), sep=',', file=f)
    print("~split2~", file=f)

    for liability in liability_list:
        print(liability, int(liabilities[liability]), sep=',', file=f)
    print("~split3~", file=f)

    for equity in equity_list:
        print(equity, int(equities[equity]), sep=',', file=f)

    f.close()


def file_to_list_type(filename):
    f = open(filename)

    assets = []
    liabilities = []
    equities = []

    split1 = 0  # used to keep track of the split indices
    split2 = 0
    split3 = 0
    year = 0
    parts = []

    for line in f:
        line = line.strip()
        parts.append(line)

    for i in range(len(parts)):   # gives us the index of the splits
        if parts[i] == "~split1~":
            split1 += i
        elif parts[i] == "~split2~":
            split2 += i
        elif parts[i] == "~split3~":
            split3 += i

    for I in range(len(parts)):  # separates the parts into their type (asset, liability, etc.)
        if I < split1:
            year = parts[I]

        elif split2 > I > split1:
            assets.append(parts[I])

        elif split3 > I > split2:
            liabilities.append(parts[I])

        elif I > split3:
            equities.append(parts[I])  # an else statement wasn't used so that the split1 values could be discarded

    f.close()

    return year, assets, liabilities, equities


def list_to_dictionary(assets, liabilities, equities):
    assets_dict = {}
    liabilities_dict = {}
    equities_dict = {}

    for i in range(len(assets)):
        asset_type, asset_amount = assets[i].split(',')
        assets_dict[asset_type] = int(asset_amount)

    for i in range(len(liabilities)):
        liability_type, liability_amount = liabilities[i].split(',')
        liabilities_dict[liability_type] = int(liability_amount)

    for i in range(len(equities)):
        equity_type, equity_amount = equities[i].split(',')
        equities_dict[equity_type] = int(equity_amount)

    return assets_dict, liabilities_dict, equities_dict


def get_total_value_from_dict(dictionary):

    total_value = 0
    for entry in dictionary:
        total_value += int(dictionary[entry])

    return int(total_value)


def dictionary_to_list(dictionary):
    list_of_keys = []
    list_of_values = []
    total_sum = 0

    for key in dictionary:
        list_of_keys.append(key)
        list_of_values.append(int(dictionary[key]))
        total_sum += int(dictionary[key])

    return list_of_keys, list_of_values, int(total_sum)


def get_assets(user_name):
    print()
    print('Hello, %s! Please enter your assets below. When complete, type "done".' % user_name)
    print("--------------------------------------------------------------------------------------------------")

    asset_name = ''
    assets = {}

    while asset_name.lower() != "done" or "~" in asset_name or asset_name in assets:
        asset_name = input("Enter the name of the asset: ")

        if "~" in asset_name or asset_name in assets:
            print('Invalid Entry.')

        elif asset_name.lower() != 'done':
            asset_amount = input("Enter the amount for %s: " % asset_name)

            while not asset_amount.isdigit():
                asset_amount = input("Enter the amount for %s: " % asset_name)
            assets[asset_name] = int(asset_amount)
        else:
            break

    total_short_assets = get_total_value_from_dict(assets)
    print("--------------------------------------------------------------------------------------------------")
    return assets, total_short_assets


def get_liabilities(user_name):
    print()
    print('%s, please enter your liabilities below. When complete, type "done".' % user_name)
    print("--------------------------------------------------------------------------------------------------")

    liability_name = ''
    liabilities = {}

    while liability_name.lower() != "done" or "~" in liability_name or liability_name in liabilities:
        liability_name = input("Enter the name of the liability: ")

        if "~" in liability_name or liability_name in liabilities:
            print('Invalid Entry.')

        elif liability_name.lower() != 'done':
            liability_amount = input("Enter the amount for %s: " % liability_name)

            while not liability_amount.isdigit():
                liability_amount = input("Enter the amount for %s: " % liability_name)
            liabilities[liability_name] = int(liability_amount)
        else:
            break

    total_liabilities = get_total_value_from_dict(liabilities)
    print("--------------------------------------------------------------------------------------------------")
    return liabilities, total_liabilities


def get_equity(user_name):
    print()
    print('%s, please enter your equities below. When complete, type "done".' % user_name)
    print("--------------------------------------------------------------------------------------------------")

    equity_name = ''
    owner_equity = {}

    while equity_name.lower() != "done" or '~' in equity_name or equity_name in owner_equity:
        equity_name = input("Enter the name of the equity: ")

        if "~" in equity_name or equity_name in owner_equity:
            print('Invalid Entry.')

        elif equity_name.lower() != 'done':
            equity_amount = input("Enter the amount for %s: " % equity_name)
            while not equity_amount.isdigit():
                equity_amount = input("Enter the amount for %s: " % equity_name)
                owner_equity[equity_name] = int(equity_amount)
        else:
            break

    total_equity = get_total_value_from_dict(owner_equity)
    print("--------------------------------------------------------------------------------------------------")
    return owner_equity, total_equity


def print_balance_sheet(year, assets, liabilities, equity):

    asset_list, asset_amounts, sum_assets = dictionary_to_list(assets)
    liability_list, liability_amounts, sum_liabilities = dictionary_to_list(liabilities)
    equity_list, equity_amounts, sum_equities = dictionary_to_list(equity)

    print()
    print("  - %s Balance Sheet -" % str(year))
    print()
    print("-------------|--------------")
    print("  - - - - Assets - - - -")
    print("-------------|--------------")
    for i in range(len(asset_list)):
        print(str(asset_list[i]) + (' ' * (13 - len(asset_list[i]))) + "| " + "$" + str(asset_amounts[i]))
        print("-------------|--------------")

    print("  - - - Liabilities - - -")
    print("-------------|--------------")
    for i in range(len(liability_list)):
        print(str(liability_list[i]) + (' ' * (13 - len(liability_list[i]))) + "| " + "$" + str(liability_amounts[i]))
        print("-------------|--------------")

    print("  - - - -  Equity  - - - -")
    print("-------------|--------------")
    for i in range(len(equity_list)):
        print(str(equity_list[i]) + (' ' * (13 - len(equity_list[i]))) + "| " + "$" + str(equity_amounts[i]))
        print("-------------|--------------")


def print_common_size(year, assets, liabilities, equities):

    asset_list, asset_amounts, sum_assets = dictionary_to_list(assets)
    liability_list, liability_amounts, sum_liabilities = dictionary_to_list(liabilities)
    equity_list, equity_amounts, sum_equities = dictionary_to_list(equities)

    print()
    print("- - %s Common-Size Balance Sheet - -" % str(year))
    print()
    print("------------------|-------------------")
    print("    - - - - - - Assets - - - - - -")
    print("------------------|-------------------")
    for i in range(len(asset_list)):
        percent_asset = float((asset_amounts[i] / sum_assets) * 100)
        print(str(asset_list[i]) + (' ' * (18 - len(asset_list[i]))) + "| = %.2f%%" % percent_asset)
        print("------------------|-------------------")
    print("Total Assets      | = 100%")
    print("------------------|-------------------")

    print("    - - - - - Liabilities - - - - -")
    print("------------------|-------------------")
    for i in range(len(liability_list)):
        percent_liability = float((liability_amounts[i] / sum_liabilities) * 100)
        print(str(liability_list[i]) + (' ' * (18 - len(liability_list[i]))) + "| = %.2f%%" % percent_liability)
        print("------------------|--------------")
    print("Total Liabilities | = 100%")
    print("------------------|-------------------")

    print("   - - - - - -  Equity  - - - - - -")
    print("------------------|-------------------")
    for i in range(len(equity_list)):
        percent_equity = float((equity_amounts[i] / sum_equities) * 100)
        print(str(equity_list[i]) + (' ' * (18 - len(equity_list[i]))) + "| = %.2f%%" % percent_equity)
        print("------------------|-------------------")
    print("Total Equity      | = 100%")
    print("------------------|-------------------")


def plot_balance_sheet(year, assets, liabilities, equities, year2, assets2, liabilities2, equities2):
    width = 0.35

    all_unique_types = list(set(assets.keys()) | liabilities.keys() | equities.keys() |
                            assets2.keys() | liabilities2.keys() | equities2.keys())
    all_amounts = []
    all_amounts2 = []
    for element in all_unique_types:
        all_amounts.append(int(assets.get(element, 0)) + int(liabilities.get(element, 0)) + int(equities.get(element, 0)))
        all_amounts2.append(int(assets2.get(element, 0)) + int(liabilities2.get(element, 0)) + int(equities2.get(element, 0)))

    plt.ylabel('Cash amount ($)')
    plt.title('Balance Sheet')
    plt.xticks(np.arange(len(all_unique_types)), all_unique_types)

    ind = np.arange(len(all_unique_types))
    p1 = plt.bar(ind, all_amounts, width)
    p2 = plt.bar(ind, all_amounts2, width,
                 bottom=all_amounts)

    plt.legend((p1[0], p2[0]), (year, year2))
    plt.show()


def get_year():
    year = input("Enter the year here: ")
    while not year.isdigit() and 1000 > int(year) > 3000:  # validates year is within a realistic range and is int
        year = input("Invalid. Please enter again: ")
    return year


def get_filename(ordinal_num):
    x = 0
    while x != 1:  # better way to run this loop?

        try:
            year = input("Enter the" + ordinal_num + " year here: ")
            while not year.isdigit():  # validates year is int
                year = input("Invalid. Please enter again: ")
            f = open('BS_' + str(year))
            f.close()
            x += 1
            return 'BS_' + str(year), year

        except IOError:
            print("file not found. Please try again")
            print()

    # returns 'BS_' + str(year)  # prints 'BS' for 'Balance Sheet' and then the year of the data for the file
    #  used "try" here so user could be asked to enter a year until the file is found


def balance_sheet_ratios(year, assets, liabilities, equities):

    asset_sum = get_total_value_from_dict(assets)
    liability_sum = get_total_value_from_dict(liabilities)
    equity_sum = get_total_value_from_dict(equities)

    debt_to_liability = (liability_sum / asset_sum)
    debt_to_equity = (liability_sum / equity_sum)

    print()
    print("---------------------------------------------------------")
    print("The Debt to Liability Ratio for the year %s is %.2f." % (str(year), debt_to_liability))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("The Debt to Equity Ratio for the year %s is %.2f." % (str(year), debt_to_equity))
    print("---------------------------------------------------------")


def main():

    while True:
        print()
        print("- - - Menu - - -")
        print("1. Enter New Data")
        print("2. Compare Data")
        print('3. Quit')
        print('- - - - - - - - -')
        print()
        user_input = input("Enter your menu choice: ")

        if user_input == '1':  # creates a new file for the year entered
            user_name = input("Please enter your name: ")
            year = get_year()
            assets, total_assets = get_assets(user_name)
            liabilities, total_liabilities = get_liabilities(user_name)
            equities, total_equities = get_equity(user_name)
            new_file(year, assets, liabilities, equities)

        if user_input == '2':
            print('---------------------------------------')
            print('MENU')
            print('1. Print Balance Sheet')
            print('2. Print Common-Size Balance Sheet')
            print('3. Plot Balance Sheets')
            print('4. Quit')
            print('---------------------------------------')

            choice = input("Enter your choice: ")
            while True:
                # Get the user's choice and then does the appropriate action

                if choice in ['1', '2', '3']:
                    filename, year = get_filename(' first')
                    year, asset_list, liability_list, equity_list = file_to_list_type(filename)
                    assets, liabilities, equities = list_to_dictionary(asset_list, liability_list, equity_list)

                    filename2, year2 = get_filename(' second')
                    year2, asset_list2, liability_list2, equity_list2 = file_to_list_type(filename2)
                    assets2, liabilities2, equities2 = list_to_dictionary(asset_list2, liability_list2, equity_list2)

                    if choice == '1':
                        print_balance_sheet(year, assets, liabilities, equities)
                        print_balance_sheet(year2, assets2, liabilities2, equities2)
                        break

                    elif choice == '2':
                        print_common_size(year, assets, liabilities, equities)
                        print_common_size(year2, assets2, liabilities2, equities2)
                        balance_sheet_ratios(year, assets, liabilities, equities)
                        break

                    elif choice == '3':
                        plot_balance_sheet(year, assets, liabilities, equities, year2, assets2, liabilities2, equities2)
                        break

                else:
                    break

        if user_input == '3':
            print("Thank you, have a nice day!")
            break


if __name__ == "__main__": main()
