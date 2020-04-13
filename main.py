import yfinance as yf
import argparse

def main():
    print("--Welcome--\nEnter a comma separated list of"
          "tickers you want to analyze")
    tickers = input()
    tickers = tickers.replace(' ', '')
    tickers = tickers.upper()
    tickers = tickers.split(',')
    print(tickers)



def loadDataFromFile():
    # open file containing list of tickers i want to watch
    tickerfile = open('tickers.txt')
    watchlist = ""
    for line in tickerfile:
        line.strip()
        watchlist += line + " "
    data = yf.download(tickers=watchlist, period="day", interval="1h", group_by='ticker')

    watchlist = watchlist.split()
    datafile = open("data.txt", "a")

    for ticker in watchlist:
        cur = data[ticker]
        datafile.write(str(ticker.upper()) + "\n" + str(cur) + "\n\n")


if __name__ == '__main__':
    main()
