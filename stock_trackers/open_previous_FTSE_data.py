'''
Created on 4 Aug 2014

@author: chris
'''
def main():
    from os_fns import open_file_list
    dir_ftse = '/home/chris/Work/projects/shares/docs/stock_market_prices/FTSE_100/'
    flist = open_file_list(dir_ftse)
    import pickle
    import dateutil.parser
    dates  = []
    prices = []
    for fname in flist:
        print fname
        f = open(fname,'r')
        data = pickle.load( f )
        print list(data)
        f.close()
#         print data['LastTradeDate']
        date = data['LastTradeDate'].split('/')[::-1]
        date[1] = str(int(date[1])+100)[1:]
        date[2] = str(int(date[2])+100)[1:]
        date = date[0] + '-' + date[2] + '-' + date[1]
        dates.append(dateutil.parser.parse(date))
        
        prices.append(float(data['LastTradePriceOnly']))
        
        print dateutil.parser.parse(date), float(data['LastTradePriceOnly'])
        
        
    from stock_plots import date_v_price
    p = date_v_price(dates,prices)
    p.show()
#     import matplotlib.pyplot as pl
#     import matplotlib.dates as mdates
#     yearsFmt = mdates.DateFormatter('%Y-%m-%d')
#     days = mdates.DayLocator()
#     
#     fig, ax = pl.subplots()
#     ax.plot(dates,prices)
#     
#     ax.xaxis.set_major_locator(days)
#     ax.xaxis.set_major_formatter(yearsFmt)
# #     ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
#     fig.autofmt_xdate()
#     pl.show()
    
    
if __name__ == '__main__':
    main()