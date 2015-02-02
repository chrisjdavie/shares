'''
Created on 3 Aug 2014

@author: chris
'''
def main():
    data = FTSE_last_price_n_date()
    print data
    
def FTSE_last_price_n_date():
    import urllib2
    
    '''This uses yql_to_more_data to arrange it's form.  Could automate,
    haven't'''
    
    codes = { 'LastTradeDate': 'd1', 'LastTradePriceOnly' : 'l1' }
    request = str.join('',codes.values())
#     print request
    
    data = codes
    
    yql_FTSE_url = 'http://download.finance.yahoo.com/d/quotes.csv?f=' + request + '&s=^FTSE'
    
    lines = urllib2.urlopen(yql_FTSE_url).readlines()
    
#     print lines
    fields = lines[0].split(',')
    fields[-1] = fields[-1][:-2] #removing eof
    for code, field in zip(codes.keys(),fields):
        field = field.strip('"')
        data[code] = field
        
    return data
    

if __name__ == '__main__':
    main()