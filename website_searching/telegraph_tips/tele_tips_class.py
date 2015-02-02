'''
Created on 17 Aug 2014

@author: chris
'''

from shares_class import share_base

class tele_tip(share_base):
    '''
    classdocs
    '''
    
    
    def __init__(self,tip):
        '''
        Constructor
        '''
        symb = tip['share']
        symb = symb.split(':')
        symb = symb[1][:-1] + '.' + symb[0][1]
        
        super(tele_tip,self).__init__(symb)
        
        import datetime
        self.date_given = datetime.datetime(*tip['time'][:6])
        self.advice = tip['advice']
        
    def gen_hist_data(self,start_date=None):
        if start_date == None:
            start_date = self.date_given
#         print start_date
#         print type(start_date)
        return super(tele_tip,self).gen_hist_data(start_date)