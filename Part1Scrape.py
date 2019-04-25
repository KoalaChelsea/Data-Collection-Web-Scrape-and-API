###########################################################
##
##     Week 4 Assignment: Python
##     Part one
##
##     Course: Advanced Programming Topics 
##     Instructor: Dr. A. Gates
##     Author: Yingjie(Chelsea) Wang
##     Date: 07/27/2018
##
###########################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen


def main():
    prefix = "https://finance.yahoo.com/quote/"

    # Mark bad url
    bad_url = "https://finance.yahoo.com/quote/bad"

    while True:
        print("Pleas enter a stock name to get price, or enter Q to quit.")

        stock_name = input()

        # Quit mark
        if stock_name == 'Q' or stock_name == 'q':
            print('Bye!')
            break

        # mark special letter as invalid stock name
        if '/' in stock_name:
            print("Invalid Stock Name!")
            continue

        if '\\' in stock_name:
            print("Invalid Stock Name!")
            continue

        # Get valid-stock-name url
        url = prefix + stock_name

        # open the url, and get response from the sever
        page = urlopen(url)
        bad_page = urlopen(bad_url)

        # manipulate the url page by lxml method
        # and assign the html code to soup
        soup = BeautifulSoup(page, "lxml")
        bad_soup = BeautifulSoup(bad_page, "lxml")

        # get corresponding 'span' in html page
        all_span = soup.findAll("span")
        bad_all_span = bad_soup.findAll("span")

        # Find the corresponding span in bad url or bad stock name
        # that will be used to compare ad check the valid stock name
        for bad_next_span in bad_all_span:
            bad_content = str(bad_next_span)[
                          str(bad_next_span).find('>') + 1:str(bad_next_span)[str(bad_next_span).find('>'):].find(
                              '<') + str(bad_next_span).find('>')]
            bad_new_content = bad_content.replace(',', '')

            try:
                bad_char = float(bad_new_content)
                break
            except ValueError:
                continue

        for next_span in all_span:
            # get value between '>' and '<'
            content = str(next_span)[
                      str(next_span).find('>') + 1:str(next_span)[str(next_span).find('>'):].find('<') + str(
                          next_span).find('>')]

            # remove comma in string
            new_content = content.replace(',', '')
            try:
                char = float(new_content)
                if char != bad_char:
                    print('CURRENT PRICE: ', char)
                else:
                    print("Invalid Stock Name!")
                break
            except ValueError:
                continue


if __name__ == '__main__':
    main()
