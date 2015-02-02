'''
Created on 5 Jul 2014

@author: chris
'''
def main():

#     bbc_bus_rss_url = "http://feeds.bbci.co.uk/news/business/rss.xml"
    
    from words import search_bbc_bus_feed
    bbc_bus_feed = search_bbc_bus_feed()

#     print bbc_bus_feed.items[0].summ
    for i, item in enumerate(bbc_bus_feed.items):
        print i
        if 'Lloyds' in item.summ:
            print 'Fiesta'

if __name__ == '__main__':
    main()