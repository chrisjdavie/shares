'''
Created on 3 Aug 2014

@author: chris
'''
def main():
#     yahoo_url = 'http://download.finance.yahoo.com/d/quotes.csv?f=d1d2ee1e7e8e9ghjkg1g3g4g5g6ii5j1j3j4j5j6k1k2k4k5ll1l2l3mm2m3m4m5m6m7m8nn4opp1p2p5p6qrr1r2r5r6r7ss1s7t1t7t8vv1v7ww1w4xy&s=%255EFTSE'
#     
#     codes = { 'last trade date':'d1' }
#     
#     import urllib2
#     
#     lines = urllib2.urlopen(yahoo_url).readlines()
#     
#     for line in lines:
#         print line
    '''when you put 
    https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%22%255EFTSE%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=
    (generated using yql)
    into the url bit of a browser, there is a diagnostic section with reveals
    many extra bits of information available, with "columns" as the headers,
    and in the url given "f=..." are the codes in a format of either 
    'alpha' or 'alpha-numer', that in the given URL return
    that information (probably).  This is a much cleaner way of doing this.
    
    The below code, based on the current results, maps the corresponding things
    onto each other.  I think.  I can't see that this would work any other way,
    but that's only sometimes valid. 
    '''

    headers='Ask,AverageDailyVolume,Bid,AskRealtime,BidRealtime,BookValue,Change&PercentChange,Change,Commission,Currency,ChangeRealtime,AfterHoursChangeRealtime,DividendShare,LastTradeDate,TradeDate,EarningsShare,ErrorIndicationreturnedforsymbolchangedinvalid,EPSEstimateCurrentYear,EPSEstimateNextYear,EPSEstimateNextQuarter,DaysLow,DaysHigh,YearLow,YearHigh,HoldingsGainPercent,AnnualizedGain,HoldingsGain,HoldingsGainPercentRealtime,HoldingsGainRealtime,MoreInfo,OrderBookRealtime,MarketCapitalization,MarketCapRealtime,EBITDA,ChangeFromYearLow,PercentChangeFromYearLow,LastTradeRealtimeWithTime,ChangePercentRealtime,ChangeFromYearHigh,PercebtChangeFromYearHigh,LastTradeWithTime,LastTradePriceOnly,HighLimit,LowLimit,DaysRange,DaysRangeRealtime,FiftydayMovingAverage,TwoHundreddayMovingAverage,ChangeFromTwoHundreddayMovingAverage,PercentChangeFromTwoHundreddayMovingAverage,ChangeFromFiftydayMovingAverage,PercentChangeFromFiftydayMovingAverage,Name,Notes,Open,PreviousClose,PricePaid,ChangeinPercent,PriceSales,PriceBook,ExDividendDate,PERatio,DividendPayDate,PERatioRealtime,PEGRatio,PriceEPSEstimateCurrentYear,PriceEPSEstimateNextYear,Symbol,SharesOwned,ShortRatio,LastTradeTime,TickerTrend,OneyrTargetPrice,Volume,HoldingsValue,HoldingsValueRealtime,YearRange,DaysValueChange,DaysValueChangeRealtime,StockExchange,DividendYield'
    vals = 'N/A,0,N/A,N/A,N/A,N/A,"-50.93 - -0.76%",-50.93,-,"GBP","-50.93","N/A - N/A",N/A,"8/1/2014",-,N/A,"N/A",N/A,N/A,N/A,6624.72,6730.11,6316.90,6894.90,"- - -","-",-,"- - -",-,"cnv","N/A",N/A,N/A,N/A,N/A,N/A,"Aug  1 - <b>6679.18</b>","-50.93 - -0.76%",N/A,N/A,"Aug  1 - <b>6679.18</b>",6679.18,-,-,"6624.72 - 6730.11","6624.72 - 6730.11",N/A,N/A,N/A,N/A,N/A,N/A,"FTSE 100","-",6730.11,6730.11,-,"-0.76%",N/A,N/A,"N/A",N/A,"N/A",N/A,N/A,N/A,N/A,"^FTSE",-,N/A,"11:35am","N/A",N/A,0,-,-,"6316.90 - 6894.90","- - -0.76%","- - -0.76%","FSI",N/A'
    headers = headers.split(',')
    vals = vals.split(',')
    
    codes='aa2bb2b3b4cc1c3c4c6c8dd1d2ee1e7e8e9ghjkg1g3g4g5g6ii5j1j3j4j5j6k1k2k4k5ll1l2l3mm2m3m4m5m6m7m8nn4opp1p2p5p6qrr1r2r5r6r7ss1s7t1t7t8vv1v7ww1w4xy'
    codes_split = []
    codes_tmp = codes[0]
    for a in codes[1:]:
        if not a.isalpha():
            codes_tmp = codes_tmp + a
        else:
            codes_split.append(codes_tmp)
            codes_tmp = a
    codes_split.append(codes_tmp)
    codes = codes_split
    
    for header, code, val in zip(headers, codes, vals):
        print header, code, val     
        


if __name__ == '__main__':
    main()