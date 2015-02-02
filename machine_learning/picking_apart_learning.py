'''
This is an adaption of the Duke sklearn training guide

Created on 4 Sep 2014

@author: chris
'''


def main():
    from parse_for_learning import parse_for_learning
    dataset = parse_for_learning()
    
    from sklearn.cross_validation import train_test_split
    news_train, news_test, y_train, y_test = train_test_split(
          dataset.data, dataset.target, test_size=0.25, random_state=5)
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    tfidf = TfidfVectorizer(stop_words='english',ngram_range=(1, 1))
    news_train_tf = tfidf.fit_transform(news_train)
    
    print dir(tfidf)
    feature_names = tfidf.get_feature_names()
    import numpy as np
    print np.shape(feature_names)
    print np.shape(news_train_tf)
    print np.shape(news_train)
    
    from sklearn.svm import LinearSVC
    clf = LinearSVC().fit(news_train_tf,y_train)
    trained_coefs = clf.coef_[0]
    
    print np.shape(trained_coefs)
    
    inds_max = trained_coefs.argsort()[-20:][::-1]
    inds_min = trained_coefs.argsort()[:20]
    print type(inds_max)
    feature_names = np.array(feature_names)
    for feature_name, coef in zip(feature_names[inds_min],trained_coefs[inds_min]):
        print feature_name, coef
    
    for feature_name, coef in zip(feature_names[inds_max],trained_coefs[inds_max]):
        print feature_name, coef
    
#     response = tfidf.transform([str])
#     feature_names = tfidf.get_feature_names()
#     for col in response.nonzero()[1]:
#         print feature_names[col], ' - ', response[0, col]
    

if __name__ == '__main__':
    main()