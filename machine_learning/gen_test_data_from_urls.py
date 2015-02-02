'''
Created on 2 Sep 2014

@author: chris
'''
def main():
    fname = '/home/chris/Work/projects/shares/docs/training_data/url_n_cat.csv'
    f = file(fname)
    data = f.read().split('\n')
    url_s = []
    pos_neg_s = []
    for dat in data[:-1]:
        dat_tmp = dat.split(',')
        url_s.append(dat_tmp[0])
        pos_neg_s.append(dat_tmp[1])
        
    i_s = 0
    for i, (pos_neg, url) in enumerate(zip(pos_neg_s, url_s)[i_s:]):
        print i + i_s
        
        base_url = '/home/chris/Work/projects/shares/analysed_files/learning/'
        url_dir = base_url + str(url.__hash__()) +'/'
        import urllib2
        html = urllib2.urlopen(url).read()
        
        
        import os
        if not os.path.exists(url_dir):
            os.makedirs(url_dir)
            
        import pickle
        f = open(url_dir + 'pos_neg.p','w+')
        pickle.dump(pos_neg, f)
        f = open(url_dir + 'url.p','w+')
        pickle.dump(url, f)
        f = open(url_dir + 'html.p','w+')
        pickle.dump(html, f)
        
        import time
        time.sleep(2)
#     print url_dir
    
#     from urllib import urlopen
#     self.html = urlopen(self.url).read()
    

if __name__ == '__main__':
    main()