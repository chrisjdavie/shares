#!/usr/bin/env python
'''
Created on 7 Dec 2013

@author: chris
'''
# parse the rss feed
# http://wiki.python.org/moin/RssLibraries

# import re

def main():
    print 'a'
    bbc_bus_rss_url = "http://feeds.bbci.co.uk/news/business/rss.xml"
    print 'b'
    
    from words import search_bbc_feed
    bbc_bus_feed = search_bbc_feed(bbc_bus_rss_url)
    
    print bbc_bus_feed.items[0].url
    print bbc_bus_feed.items[0].title
    print bbc_bus_feed.items[0].summ
    bbc_bus_feed.items[0].words_on_page()
    print bbc_bus_feed.items[0].words
    
    
#     print list(bbc_bus_feed.feed["items"][0])
#     print bbc_bus_feed.feed["items"][0]['link']
#     print bbc_bus_feed.feed["items"][0]['summary_detail']['value']
#     
#     print bbc_bus_feed.feed["items"][0]['title']
#     print nltk.clean_html(bbc_bus_feed.feed["items"][0]['title'])
# #     print 'c'
#     bbc_bus_feed.extract_all_summs()
#     print 'd'
#     print bbc_bus_feed.summs[0]
#     company_name = 'RBS'
#     
#     RBS_list = []
#     for i, sum in enumerate(bbc_bus_feed.summs): 
#         if company_name in sum: RBS_list.append(i)
#     print bbc_bus_feed.feed["items"][0]['title']
#     
    #print RBS_list
        
    
#     #company_name = 'NatWest'
#     wordss = []
#     while True: 
#         print bbc_bus_feed.i
#         wordss.append(bbc_bus_feed.extract_words())
        
#     for word in words:
#         print word
    # open the website
        
if __name__ == '__main__':
    main()
