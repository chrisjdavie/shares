'''
Created on 17 Aug 2014

@author: chris
'''
from shares_class import share_base
def main():
    each_week = 1.0 # GBP, but arb 
    
    from telegraph_tips import load_questor_tips
    que_tips = load_questor_tips()[::-1]
    
    from telegraph_tips import tele_tip
    
    buy_tips = []
    for que_tip in que_tips:
        if que_tip['share'] == '[LON:BHP]':
            que_tip['share'] = '[LON:BLT]'        
        if 'BUY' == que_tip['advice']:
            buy_tips.append(tele_tip(que_tip))
    
    buy_tips = [ tele_tip(que_tip) for que_tip in que_tips if 'BUY' == que_tip['advice'] ]
    
    sell_tips = [ tele_tip(que_tip) for que_tip in que_tips if 'SELL' == que_tip['advice'] ]
    
    buy_symbs = [ buy_tip.symb for buy_tip in buy_tips ]
    sell_symbs = [ sell_tip.symb for sell_tip in sell_tips ]
    if any(sell_symb in buy_symbs for sell_symb in sell_symbs):
        '''if this is slow, the set and intersection generates hashes, which are much faster for long lists'''
        print "implement sell routines"
        exit(2)
    
    tip0 = buy_tips[0]
    date0 = tip0.date_given
    
    from dateutil.relativedelta import relativedelta
    
    
    
#     print 'date0: ', date0.strftime('%d/%m/%Y')
#     print 'date1: ', date1.strftime('%d/%m/%Y')
    
    for buy_tip in buy_tips:
        print buy_tip.symb
    
    print "\n"
    
    date1 = date0 + relativedelta(weeks=1)


    FTSE = FTSE100_indi()
    test_dates, _ = buy_tips[0].gen_hist_data(date1)
    total_dates, _ = FTSE.gen_hist_data(date1,test_dates=test_dates)
    
    print len(test_dates), len(total_dates)
#     raw_input()
    import numpy as np
    total_earnings_FTSE = np.zeros_like(FTSE.gen_pc_change() )
    total_earnings = np.zeros_like(FTSE.gen_pc_change() )
    total_invested = np.zeros_like(FTSE.gen_pc_change() )
    
    for i in range(4):
        
        date1 = date0 + relativedelta(weeks=1)
        
        weeks_tips = []
        for buy_tip in buy_tips:
            if (buy_tip.date_given >= date0) and (buy_tip.date_given < date1):
                weeks_tips.append(buy_tip)
        
        for tip in weeks_tips:
            print tip.symb
    #     print len(weeks_tips)
        each_tip = each_week/len(weeks_tips)
        
        _, prices0 = weeks_tips[0].gen_hist_data(date1)
        
        weeks_earnings = np.zeros_like(prices0)
        
        for tip in weeks_tips:
            test_dates, _ = tip.gen_hist_data(date1)
            pc_change = tip.gen_pc_change()
            weeks_earnings += each_tip*pc_change
           
        from stock_plots import date_v_price
        
        FTSE.gen_hist_data(date1,test_dates=test_dates)            
        weeks_earnings_FTSE = each_week*FTSE.gen_pc_change()
        i = len(weeks_earnings)
        print i, len(total_earnings_FTSE[-i:]), len(total_earnings_FTSE)
        total_earnings_FTSE[-i:] = total_earnings_FTSE[-i:] + weeks_earnings_FTSE
        total_earnings[-i:] = total_earnings[-i:] + weeks_earnings
        total_invested[-i:] = total_invested[-i:] + 1.0
        
        
        date0 = date1
        
    p = date_v_price(total_dates,total_earnings,ylabel=r'Money investments',label='Tips')
    p.add_line(total_earnings_FTSE,label=r'FTSE 100')
    p.leg('upper left')

    pc_earnings = total_earnings/total_invested
    pc_earnings_FTSE = total_earnings_FTSE/total_invested
    
    p = date_v_price(total_dates,pc_earnings,ylabel=r'Change',fig_i=2,label='Tips')
    p.add_line(pc_earnings_FTSE,label=r'FTSE 100')
    p.leg('upper left')
        
    p.show()
#  
import numpy as np
       
class FTSE100_indi(share_base):
    def __init__(self):
        super(FTSE100_indi,self).__init__(r'^FTSE')
        
    def gen_hist_data(self, start_time, end_time=None, test_dates=None):
        super(FTSE100_indi,self).gen_hist_data(start_time, end_time=end_time)
        if test_dates != None:
            if len(test_dates) != len(self.hist_dates):
                for i in range(len(self.hist_dates)):
                    if test_dates[i] < self.hist_dates[i]:
                        print "bank holiday?  Missing date in FTSE", i, test_dates[i], self.hist_dates[i]
                        self.hist_dates.insert(i,test_dates[i])
                        self.hist_prices = np.insert(self.hist_prices, i, self.hist_prices[i-1])
            
        
        return self.hist_dates, self.hist_prices  

if __name__ == '__main__':
    main()