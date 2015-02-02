'''
Created on 8 Aug 2014

@author: chris
'''
def main():
    print 'if you actually want to restart questor analysis, uncomment the next lines and re-run'
#     tips_fname = '/home/chris/Work/projects/shares/analysed_files/questor/all_tips.p'
#     
#     tips_sort = dl_questor_tips()
#     
#     for tip in tips_sort:
#         print tip
#     
#     import pickle
#     f = open(tips_fname,'w')
#     pickle.dump(tips_sort,f)
#     f.close()
    
def dl_questor_tips():
    import feedparser
    
    rss_url = 'http://www.telegraph.co.uk/finance/markets/questor/rss'
    feed = feedparser.parse(rss_url)
#     print dir(feed)
#     print list(feed.items()[0])
    items = feed['items']
    
    tip_parse = {}
    tips = []
    
    import copy
    
    for item in items:
        tmp_quest = questor(item)
        if tmp_quest.is_tip_q() and tmp_quest.find_tip_q():
            tip_parse['share']  = tmp_quest.share_tip
            tip_parse['advice'] = tmp_quest.advice
            tip_parse['time']   = tmp_quest.item.published_parsed
            tip_parse['hash']   = tmp_quest.hash
            tips.append(copy.copy(tip_parse))
    
    from operator import itemgetter
    tips_sort = sorted(tips, key=itemgetter('time'))[::-1]
    return tips_sort
    

words_folder = '/home/chris/Work/projects/shares/workspace/website_searching/'
import sys
if words_folder not in sys.path:
#     print 'hello?'
    sys.path.insert(0, words_folder)
       
from words import _feed_item
                    
class questor(_feed_item):
    def __init__(self,item):
        self.item_save_dir = '/home/chris/Work/projects/shares/analysed_files/questor/'
        self.item = item

        super(questor,self).__init__(self.item.link)
        
        self.title = self.item.title
        
    def is_tip_q(self):
        self.tip_q = 'tip' in self.title
        return self.tip_q
    
    def find_tip_q(self):
        ''' currently finding out if Questor is giving us the share symbol '''
        self.easy_tip_q = False
        self.find_tip()
        if self.share_tip != None and self.advice != None:
            self.easy_tip_q = True
        return self.easy_tip_q
         
         
    def find_tip(self):   
        self.open_html()
        
        import re
        _alphanum = re.compile('\w')
        def contains_alphanum(stri):
            return bool(_alphanum.search(stri))
        
        _share = re.compile('\[\w*:\w*\]')
        def contains_share(stri):
            return bool(_share.search(stri))
        
        
        import nltk
        article_raw_lines = nltk.clean_html(self.html).splitlines()
        
        self.share_tip = None
        self.advice = None
        for line in article_raw_lines:
            if 'Questor says' in line:
                answer = line.split(' ')
                answer = [ s for s in answer if contains_alphanum(s) ]
                self.advice = answer[-1]
            if contains_share(line):
                self.share_tip = _share.search(line).group()
                
        if self.advice == None and self.share_tip != None:
            tips = ['BUY','SELL','HOLD']
            for tip in tips:
                if tip.lower() in self.title.lower():
                    self.advice = tip
            if self.advice == None:
                print 'Questor is being inconsistent, couldnt find advice'
                print self.title
                print self.url
            
            
        return self.share_tip, self.advice
        
if __name__ == '__main__':
    main()