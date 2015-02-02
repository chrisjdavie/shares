'''
Created on 3 Sep 2014

@author: chris
'''
        
import nltk
import numpy as np

def main():
    sentiment = parse_for_learning()
    print sentiment.keys()
    
def parse_for_learning():
    pages = parse_text()
    news_data = []
    news_target = []
    for page in pages:
        news_data.append(page.article_raw)
        news_target.append(page.pos_neg)
    
#     i = 0 
#     for target in news_target:
#         if target == 0:
#             i += 1
#     print i
#     raw_input() 
    dataset = news_sentiment(news_data,news_target)
    
    return dataset

class news_sentiment(object):
    def __init__(self,news_data,news_target):
        self.data = news_data
        self.target = news_target
        self.target_names = [  'bad news', 'good news' ]
        
def parse_text():
    base_url = '/home/chris/Work/projects/shares/analysed_files/learning/'
    from os_fns import open_file_list
    dirs = open_file_list(base_url)
    
    import pickle
    
    pages = []
    for i, url_dir in enumerate(dirs):
        print i
        url_dir = url_dir + '/'
        f = open(url_dir + 'pos_neg.p','r')
        pos_neg = pickle.load(f)
#         print 'pos_neg', pos_neg
        f = open(url_dir + 'url.p','r')
        url = pickle.load(f)
#         print 'url', url
        f = open(url_dir + 'html.p','r')
        html = pickle.load(f)
        
        if 'bbc' in url[:20]:
            page = _bbc_story(url)
        elif 'telegraph' in url[:26]:
            page =  _tele_story(url)
        elif 'reuters' in url[:21]:
            page = _reuters_story(url)
        elif 'www.ft.' in url[:18]:
            page = _ft_story(url)
        elif 'blogs.ft.' in url[:18]:
            page = _ft_blog(url)
        else:
            print pos_neg
            print url
            break
        
        page._pos_neg(pos_neg)
        page._open_html(html)
        page.article_content()
#         page.teaching_form()
        pages.append(page)
#         print page.pos_neg
        
    return pages
#         raw_input()
        
        
#         print page._content_chunk_starts_html[0][0]
#         for line in page.html.splitlines():
#             if page._content_chunk_starts_html[0][0] in line:
#                 print line
#                 raw_input()
        
#         tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#         print np.shape(page.article_raw)
#         sentences = tokenizer.tokenize(page.article_raw)
#         for sentence in sentences:
#             print sentence
#         print pos_neg
#         print url
#         raw_input()


class _story(object):
    def __init__(self,url):
        self.url = url
    
    def _open_html(self,html):
        self.html = html
        
    def _pos_neg(self,pos_neg):
        '''positive -> 1, neg -> 0'''
        if pos_neg == 'p':
            self.pos_neg = 1
        elif pos_neg == 'n':
            self.pos_neg = 0
        else:
            self.pos_neg = 'Nan'
        
    def teaching_form(self):
        if not hasattr(self, 'article_raw'): self.article_content()
        
        '''needs to be string, is string'''
        print type(self.article_raw) 
            
        
    def article_content(self):
        self.article_raw = ''
        for content_start_html in self._content_chunk_starts_html:
            self.article_raw += self._parse_chunk(content_start_html, self._content_chunk_ends_html)
            
    def _parse_chunk(self,content_start_html,content_end_html):
        html_lines = self.html.splitlines()
        started = False
        
        article_html = ''
        for line in html_lines:
#             if 'rapha' in line.lower():
#                 print self.url
#                 raw_input()
            if any(s in line for s in content_start_html) and not started:
#                 print "a"
                
                    
                for s in content_start_html:
                    if s in line:
                        line = line[line.index(s)+len(s):] + '<p> # <\p>' 
                
                
                if any(s in line for s in content_end_html):
                    for s in content_end_html:
                        print s
                        print line
                        print s in line
                        print 'bp'
                started = True
#                 raw_input()
            if started: 
                if any(s in line for s in content_end_html):
                    for s in content_end_html:
                        if s in line:
                            article_html += line[:line.index(s)] + '<p> # <\p>' 
#                         print s in line
#                         print s
#                         print line
#                     print('d')
                    
                    break
                article_html += line
                
        return nltk.clean_html(article_html).replace('#',' ')

'''There is a difference in 
      self._content_chunk_starts_html   - [[str1,str2],[str3],[str4,str5,str6],...,[str7]]
      and self._content_chunk_ends_html - [ str_a,str_b, str_c,...,str_d ]
   it may be that features are missing, so it doesn't need to start, 
   but I do want it to stop.'''
    
class _ft_story(_story):
    def __init__(self,url):
        self._content_chunk_starts_html = [ [ r'EPA</a>'], [ r"</li></ul></div><p>" ], [r'<a href="http://video.ft.com/">More video</a>']  ]
        self._content_chunk_ends_html = [ r'<div class="insideArticleShare">', r'<div class="storyvideonojs">', r'<div class="insideArticleRelatedTopics ft-spc-btm-full"' ]
        super(_ft_story,self).__init__(url)
        
class _ft_blog(_ft_story):
    def __init__(self,url):
        super(_ft_blog,self).__init__(url)
        self._content_chunk_starts_html.append([ r'<div class="entry-content">' ])
        self._content_chunk_ends_html.append( r'<!-- .entry-content -->' )
        super(_ft_blog,self).__init__(url)
        

class _reuters_story(_story):
    def __init__(self,url):
        self._content_chunk_starts_html = [ [ r'<span id="midArticle_0">' ] ]
        self._content_chunk_ends_html = [ r'<div class="module shareLinks horizontal">' ]
        super(_reuters_story,self).__init__(url)


class _tele_story(_story):
    def __init__(self,url):
        self._content_chunk_starts_html = [ [ r'<div class="firstPar">' ], [ r'<div class="body">' ] ]
        self._content_chunk_ends_html = [ r'<span>Related Articles</span>', r'<!-- googleoff: all -->' ]
        super(_tele_story,self).__init__(url)


class _bbc_story(_story):
    def __init__(self,url):
        self._content_chunk_starts_html = [ [ r'<p class="introduction" id="story_continues_1">' ] ]
        self._content_chunk_ends_html = [ r'<strong>Are you affected by this? You can share your experience with us by emailing </strong>', r'<!-- / story-body -->' ]
        super(_bbc_story,self).__init__(url)
       
            
        

        
    
    
        
#         article = article.replace('\n\n','')
#         article = article.splitlines()
#         
#         for line in article:
#             print line
#         print 'html', html

if __name__ == '__main__':
    main()