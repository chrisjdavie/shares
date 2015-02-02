'''
Created on 5 Jul 2014

@author: chris
'''
def main():
    from shares_class import LSE
    LSE_n = LSE()
    
    bbc_bus_rss_url = "http://feeds.bbci.co.uk/news/business/rss.xml"
    from words import search_bbc_feed
    bbc_bus_feed = search_bbc_feed(bbc_bus_rss_url)
    
    print bbc_bus_feed.items[0].summ
    print bbc_bus_feed.items[0].url
    
    for share in LSE_n.shares:
#         print share.news_names, 'bob'
        if any(news_name in bbc_bus_feed.items[0].summ for news_name in share.news_names):
            print share.news_names
    

if __name__ == '__main__':
    main()