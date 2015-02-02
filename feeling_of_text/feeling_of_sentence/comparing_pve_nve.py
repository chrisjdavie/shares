'''
Created on 5 Jul 2014

@author: chris
'''
def main():
    
    bbc_bus_rss_url = "http://feeds.bbci.co.uk/news/business/rss.xml"
    from words import search_bbc_feed
    bbc_bus_feed = search_bbc_feed(bbc_bus_rss_url)
    item = bbc_bus_feed.items[19]
    item.pos_neg_count()
    print item.url.__hash__(), type(item.url)
    raw_input()
    print item.summ
#     print ' xxx negative xxx '
    print item.neg_count
#     print '\n\n\n xxx positive xxx '
    print item.pos_count
    
# def proto(bbc_bus_feed):
#     
#     
#     text_analy_dir = '/home/chris/Work/projects/shares/docs/text_analy/'
#     neg_fname = text_analy_dir + 'negative'
#     pos_fname = text_analy_dir + 'positive'
#     
#     def find_feel_words(fname):
#         feel_file = open(fname, 'r')            
#         words = [ word[:-1] for word in feel_file ]
#         
#         count = 0
#         bbc_bus_feed.items[0].sentences_on_page()
#         for sentence in bbc_bus_feed.items[0].sentences:
# #             print sentence
#             found = False
#             for word in words:
#                 if word in sentence:
#                     print word
#                     found = True
#             if found: count += 1
# 
#         return count
#     
#     print bbc_bus_feed.items[0].summ
#     print ' xxx negative xxx '
#     neg_count = find_feel_words(neg_fname)
#     print '\n\n\n xxx positive xxx '
#     pos_count = find_feel_words(pos_fname)
#     print neg_count, pos_count

if __name__ == '__main__':
    main()