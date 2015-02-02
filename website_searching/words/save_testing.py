'''
Created on 19 Jul 2014

@author: chris
'''
def main():
    from words import search_bbc_bus_feed
    
    feed = search_bbc_bus_feed()
    print feed.items[0]._save_flag
#     feed.items[0].save_item()
    
if __name__ == '__main__':
    main()