'''
Created on 15 Aug 2014

@author: chris
'''
def main():
    from telegraph_tips import load_questor_tips
    que_tips = load_questor_tips()
    
    for tip in que_tips[::-1]:
        if tip['advice'] == 'BUY':
            break
    
    from telegraph_tips import tele_tip
    tip = tele_tip(tip)
    dates,prices = tip.gen_hist_data()

    from stock_plots import date_v_pc_change
    p = date_v_pc_change(dates,prices)
    
    from shares_class import share_base
    FTSE = share_base(r'^FTSE')
    dates,prices = FTSE.gen_hist_data(tip.date_given)
    
    p.add_line(prices, dates)
    
    p.show()
#     from shares_class import share
#     test = share(symb)
#     test.gen_yahoo_name()
    
    
    
if __name__ == '__main__':
    main()