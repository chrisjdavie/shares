'''
Created on 19 Jul 2014

@author: chris
'''
def main():
    bbc_bus_rss_url = "http://feeds.bbci.co.uk/news/business/rss.xml"
    from words import search_bbc_feed
    bbc_bus_feed = search_bbc_feed(bbc_bus_rss_url)
    item = bbc_bus_feed.items[19]
#     print item.summ
    item.sentences_on_page()
    for sentence in item.sentences:
        print sentence
#     item.pos_neg_count()
#     print item.neg_count, item.pos_count

if __name__ == '__main__':
    main()