'''
Created on 17 Aug 2014

@author: chris
'''
import numpy as np

def main():
    from telegraph_tips import load_questor_tips
    que_tips = load_questor_tips()[::-1]
    
    buy_tips = [ que_tip for que_tip in que_tips if 'BUY' == que_tip['advice'] ]
#     for tip in buy_tips: print tip['time']
#     raw_input()
    
    from telegraph_tips import tele_tip
    
#     print buy_tips[0]
    tip0 = tele_tip(buy_tips[0])
    dates0, _ = tip0.gen_hist_data()
#     print dates0[-1], dates0[0], np.shape(dates0)
    pc_change = tip0.gen_pc_change()
#     pc_change0 = tip0.gen_pc_change()
    total_invested = np.zeros_like(pc_change) + 1.0
    
    from shares_class import share_base
    FTSE = share_base(r'^FTSE')
    dates_test, _ = FTSE.gen_hist_data(tip0.date_given)#
#     print dates_test[-1], dates_test[0], np.shape(dates_test), type(dates_test)
    pc_FTSE = FTSE.gen_pc_change()
    
#     for date0, date1 in zip(dates0, dates_test): print date0, date1
    
    if len(dates0) != len(dates_test):
        for i in range(len(dates_test)):
            if dates0[i] < dates_test[i]:
                print "bank holiday?  Missing date in FTSE", i, dates0[i], dates_test[i]
                dates_test.insert(i,dates0[i])
                pc_FTSE = np.insert(pc_FTSE, i, pc_FTSE[i-1])
#     print np.shape(pc_FTSE), np.shape(dates_test), np.shape(dates0)
# #     for date0, date1 in zip(dates0, dates_test): print date0, date1
# #     raw_input()    
#     
#     raw_input()
    for buy_tip in buy_tips[1:]:
        if buy_tip['share'] == '[LON:BHP]':
            buy_tip['share'] = '[LON:BLT]'
        tip = tele_tip(buy_tip)
#         print tip.start_time
#         print 'a' 
        try:
            dates, _ = tip.gen_hist_data()
#         print 'b'
        
            for i, date0 in enumerate(dates0):
    #             print date0
                if date0 > dates[0]:
                    break    
            
            i = i - 1
            
            pc_change_new = tip.gen_pc_change()
            pc_change = np.concatenate((pc_change[:i],pc_change[i:]+pc_change_new))
            pc_FTSE[i:] = pc_FTSE[i:] + pc_FTSE[i:]/pc_FTSE[i]
            total_invested[i:] = total_invested[i:] + 1.0
        except:
            print "failed", buy_tip
        
    pc_FTSE   = pc_FTSE/total_invested
    pc_change = pc_change/total_invested
    dates = dates0
    
    from stock_plots import date_v_price
    
    p = date_v_price(dates,pc_change,ylabel='Change',label='Tips')
    p.add_line(pc_FTSE,label=r'FTSE 100')
    
    p.leg(loc='upper left')
    p.show()
    
if __name__ == '__main__':
    main()