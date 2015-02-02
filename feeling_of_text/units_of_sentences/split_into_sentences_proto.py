'''
Created on 20 Jun 2014

@author: chris
'''
def main():
#     from words import bbc
    from words import search_bbc_feed
    
#     print 'a'
    bbc_bus_rss_url = "http://feeds.bbci.co.uk/news/business/rss.xml"
#     print 'b'
    bbc_bus_feed = search_bbc_feed(bbc_bus_rss_url)
    
#     print bbc_bus_feed.items[0].url
#     print bbc_bus_feed.items[0].title
#     print bbc_bus_feed.items[0].summ
    bbc_bus_feed.items[0].sentences_on_page()
    
    for sentence in bbc_bus_feed.items[0].sentences:
        print sentence
        
    
#     proto(bbc_bus_feed)
    
def proto(bbc_bus_feed):
    html = bbc_bus_feed.items[0].html
    bbc_start_intro = r'<p class="introduction" id="story_continues_1">'
    bbc_ends = [ '<strong>Are you affected by this? You can share your experience with us by emailing </strong>', '<!-- / story-body -->' ]
    
    html = html.splitlines()
    started = False
    
    article_html = ''
    for line in html:
        if (bbc_start_intro in line) and not started:
            started = True
        if started: 
            if any(s in line for s in bbc_ends):
                break
            article_html += line
            
    import nltk
    article_raw = nltk.clean_html(article_html)
     
#     import nltk.data
#      
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    bob = tokenizer.tokenize(article_raw)
    print len(bob)
    for sentence in bob:
        print sentence

if __name__ == '__main__':
    main()