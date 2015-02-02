'''
Created on 17 Aug 2014

@author: chris
'''

from date_v_price_f import date_v_price
import numpy as np

class date_v_pc_change(date_v_price):
    '''
    classdocs
    '''


    def __init__(self,dates,prices):
        '''
        Constructor
        '''
        pc_change = np.array(prices)/np.float(prices[0])
        print pc_change[0]
        
        super(date_v_pc_change,self).__init__(dates,pc_change,ylabel='\% change')
        
    def add_line(self, new_y, new_x=None, label=''):
        new_y = np.array(new_y)/new_y[0]
        super(date_v_pc_change,self).add_line(new_y, new_x=new_x, label=label)