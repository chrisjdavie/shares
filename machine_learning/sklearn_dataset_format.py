'''
Created on 2 Sep 2014

@author: chris
'''
'''File format - data, length of data, containing unicode
               - target, length of data, contains int reference to target
               - target_names, type names relative to target 
               - filenames, names of files storing data (probably target too)
               
               '''
               
               

def main():
    ''' taken from the tutorials, I'm having a look at how they store datasets'''
    from sklearn.datasets import fetch_20newsgroups
#     import numpy as np
    
    
    categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
    
    twenty_train = fetch_20newsgroups(subset='train',
                                      categories=categories, 
                                      shuffle=True, 
                                      random_state=42)
    
    print dir(twenty_train)
    print twenty_train.keys()
#     print twenty_train.data[0]
    print twenty_train.target[0]
    print len(twenty_train.filenames)
    print twenty_train.filenames[0]
    print twenty_train.target_names

if __name__ == '__main__':
    main()