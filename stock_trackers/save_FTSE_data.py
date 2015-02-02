#!/usr/bin/env python
'''
Created on 4 Aug 2014

@author: chris
'''
def main():
    ftse_dir = '/home/chris/Work/projects/shares/docs/stock_market_prices/FTSE_100/'
    
    from pull_FTSE_price import FTSE_last_price_n_date
    price_n_date = FTSE_last_price_n_date()
    
    
    date = price_n_date['LastTradeDate'].split('/')
    
    
    date[0] = str(int(date[0]) + 100)[1:]
    date[1] = str(int(date[1]) + 100)[1:]
    fname = ftse_dir + date[2] + date[0] + date[1]  + '.p'
    
    
    import pickle
    
    f = open(fname,'w')
    pickle.dump( price_n_date, f )
    f.close()
    print fname
    
if __name__ == '__main__':
    main()