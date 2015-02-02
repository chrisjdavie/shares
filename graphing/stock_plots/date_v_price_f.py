'''
Created on 15 Aug 2014

@author: chris
'''
from linplots_cjd import linear_plot

class date_v_price(linear_plot):
    '''
    classdocs
    '''


    def __init__(self,dates,prices,ylabel='Prices',fig_i=1,label=r''):
        '''
        Constructor
        '''
        super(date_v_price,self).__init__(dates,prices)
        super(date_v_price,self).plot_init(xlabel='Dates',ylabel=ylabel,fig_i=fig_i)
        
        import matplotlib.dates as mdates        
        yearsFmt = mdates.DateFormatter('%Y-%m-%d')
#         days = mdates.DayLocator()
        
#         self.ax.xaxis.set_major_locator(days)
        self.ax.xaxis.set_major_formatter(yearsFmt)
        self.plot(label=label)
        
        import matplotlib.pyplot as pl
        fig = pl.gcf()
        fig.autofmt_xdate()
        