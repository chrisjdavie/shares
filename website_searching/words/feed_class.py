'''
Created on 19 Jul 2014

@author: chris
'''
import feedparser
import nltk
import time
import pickle

    
class search_bbc_feed(object):
    
    def __init__(self,rss_url,db=False):
        self.feed = feedparser.parse(rss_url)
        
        items_raw = self.feed["items"]
        self.items = []
        self.I = len(items_raw)
        for i in range(self.I):
            item = self.feed["items"][i]
            beeb_item = bbc_feed_item(item)
            
            if not db:
                try:
                    with open(beeb_item.hash_fname,'r') as f:
                        
                        beeb_item = pickle.load( f )
                
                except IOError:
                    pass
            
            self.items.append(beeb_item)
#             print self.items[i].title
    
#     def extract_summ(self,i=None):
#         if i != None:
#             self.i = i        
#         def int_extract(self,sec):
#             str_i = self.feed["items"][self.i][sec]
#             return nltk.clean_html(str_i)
#         ''' This all needs to initalise a feed_item object, containing the relevant information'''
#         
#         raw_summ = 0
#         self.i += 1
#         return re.findall("[\w]+",raw, re.I)
#     
#     def extract_all_summs(self):
#         items = self.feed["items"]
#         self.summs = []
#         while self.i < len(items):
#             self.summs.append(self.extract_summ())

class search_bbc_bus_feed(search_bbc_feed):
    
    def __init__(self,db=False):
        bbc_bus_rss_url = "http://feeds.bbci.co.uk/news/business/rss.xml"
        super(search_bbc_bus_feed,self).__init__(bbc_bus_rss_url,db)


        
class _feed_item(object):
    ''' this will contain all the bits from at item - so far, summary and title, but
        I'll need to extract more than that from it'''
    def __init__(self,url):
        self.url = url
        self.hash = url.__hash__()
        self.hash_fname = self.item_save_dir + str(self.hash) + '.p'
        self.pos_neg_done = False
        self._save_flag = False

    def sentences_on_page(self):
        
        self.open_html()
        
        #extracting the main part of the text
        
        html_lines = self.html.splitlines()
        started = False
        
        article_html = ''
        for line in html_lines:
            if (self._content_start_html in line) and not started:
                started = True
            if started: 
                if any(s in line for s in self._content_end_html):
                    break
                article_html += line    
            
        article_raw = nltk.clean_html(article_html)
        
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        self.sentences = tokenizer.tokenize(article_raw)
        
    def open_html(self):
        from urllib import urlopen
        self.html = urlopen(self.url).read() 
        return self.html       
                
    def pos_neg_count(self,symb,db=False):
        self.pos_neg_share_symb = symb
        if db or not self.pos_neg_done:
            self._pos_neg_count()
            self.pos_neg_done = True
            self.save_item()
        else:
            print "Analysis already done and saved, def pos_neg_count, class _feed_item, search_company_name.py"
    
    def _pos_neg_count(self):
        text_analy_dir = '/home/chris/Work/projects/shares/docs/text_analy/'
        neg_fname = text_analy_dir + 'negative'
        pos_fname = text_analy_dir + 'positive'
        
        def find_feel_words(fname):
            feel_file = open(fname, 'r')            
            words = [ word[:-1] for word in feel_file ]
            
            count = 0
            self.sentences_on_page()
            for sentence in self.sentences:
    #             print sentence
                found = False
                for word in words:
                    if word in sentence:
                        start_ends = [ ' ', '&quot;', "\'" ]
                        combs = [ start_end1 + word + start_end2 in sentence for start_end1 in start_ends for start_end2 in start_ends ]
                        if any(combs):
                            found = True
                        
                if found: 
                    count += 1
    
            return count
        
#         print ' xxx negative xxx '
        self.neg_count = find_feel_words(neg_fname)
        
#         print '\n\n\n xxx positive xxx '
        self.pos_count = find_feel_words(pos_fname)
        

#         self.html = self.html.decode('utf-8')
#         self.raw = nltk.clean_html(self.html) 
#         
#         # search the text for words
#         self.words = re.findall("[\w]+",self.raw, re.I)    
    def save_item(self):
        '''This is going for the award of the most half-assed way I've ever thought of of doing anything.'''
        self._save_item(self.hash_fname)
        self._save_item(self.hash_fname[:-2]+'_dbl.p')
        print self._save_item(self.hash_fname[:-2]+'_dbl.p')
        self._save_flag = True
        
    def _save_item(self,fname):
        f = open(fname,'w')
        pickle.dump( self, f )
        f.close()
        

        
class bbc_feed_item(_feed_item):
    def __init__(self,item):
        self.item  = item
#         print dir(item)
#         raw_input()
        self.item_save_dir = '/home/chris/Work/projects/shares/analysed_files/bbc/'
        super(bbc_feed_item,self).__init__(self.item['link'])
        
        self.title = self.item['title']
        self.summ  = self.item['summary_detail']['value']

        self._content_start_html = r'<p class="introduction" id="story_continues_1">'
        self._content_end_html = [ '<strong>Are you affected by this? You can share your experience with us by emailing </strong>', '<!-- / story-body -->' ]
        
    
class saved_feed_details(object):
    def __init__(self,feed_item,pve_nve_score):
        self.url           = feed_item.url
        self.pve_nve_score = pve_nve_score
        self.analy_date    = time.strftime("%y%m%d")
        
        
        
class _all_proced_feed_items(object):
    def __init__(self):
        fname_pref = 'proced_list'
        fname_suff = '.p'
        self.dump_fname = self.fname_dir + fname_pref + fname_suff
        self.load_feed_items_list()
        
    def _load_feed_items_list(self):
        
        try:
            with open(self.dump_fname,'r') as f:
                
                self.feed_items_list = pickle.load( f )
        
        except IOError:
            
            print "feed items file doesn't exist yet, def _load_feed_items_list, class _all_proced_feed_items, search_company_name.py"
            self.feed_items_list = []
            
        self.save_shares()
        
    def _save_shares(self):
        ''' this is a delete-and-write (I think)'''
        f = open(self.dump_fname,'w')
        pickle.dump( self.feed_items_list, f )
        f.close()
        
class bbc_proced_feed_items(_all_proced_feed_items):
    def __init__(self):
        self.fname_dir  = '/home/chris/Work/projects/shares/docs/proced_feed_items/bbc/'
        
    def load_feed_items_list(self):
        self._load_feed_items_list()
        
    def save_shares(self):
        self._save_shares()
