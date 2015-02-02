'''
Created on 3 Sep 2014

@author: chris
'''
def main():
    from parse_for_learning import parse_for_learning
    dataset = parse_for_learning()
#     print dataset.target
    
    
    
    N_samp = -1
    from sklearn.cross_validation import train_test_split
    news_train, news_test, y_train, y_test = train_test_split(
        dataset.data[:N_samp], dataset.target[:N_samp], test_size=0.25, random_state=5)
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    vect = TfidfVectorizer(stop_words='english')
    
    from sklearn.pipeline import Pipeline
    from sklearn.svm import LinearSVC
    from sklearn.feature_extraction.text import CountVectorizer
    clf0 = LinearSVC()
    clf = Pipeline([('vect', vect),
                    ('clf',clf0)
                   ]) 
    
    parameters = {'vect__ngram_range': [(1, 1), (1, 2)]
                 }    

    from sklearn.grid_search import GridSearchCV    
    gs_clf = GridSearchCV(clf, parameters, n_jobs=-1)
    
    gs_clf = gs_clf.fit(news_train, y_train)
    
    best_parameters, score, _ = max(gs_clf.grid_scores_, key=lambda x: x[1])
    for param_name in sorted(parameters.keys()):
        print("%s: %r" % (param_name, best_parameters[param_name]))
        
    y_predicted = gs_clf.predict(news_test)
    
    from sklearn import metrics
    from sklearn.metrics import accuracy_score
    print accuracy_score(y_test,y_predicted)
    print metrics.classification_report(y_test,y_predicted,
                                        target_names=dataset.target_names)
    
    params = gs_clf.get_params()
    import numpy as np
#     print params
#     print clf0.coef_
    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)

    bounds = np.linspace(2,15,14)
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    cmap = plt.cm.bone_r
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
    from cplots_ig_cjd import plot_font_setup
    plot_font_setup()
    p = plt.matshow(cm,cmap='bone_r', norm=norm)
    p.axes.set_xticklabels(('a',r'{\bf Bad news}',r'{\bf Good news}'))
    p.axes.set_yticklabels(('a',r'{\bf Bad news}',r'{\bf Good news}'), rotation=90)
    cbar = plt.colorbar()
    cbar.solids.set_edgecolor("face")
    cbar.set_ticks(np.arange(3,15.5,2))
    cbar.set_label(r'{\bf No. articles}')
#     print dir(cbar)
#     plt.savefig('/home/chris/Work/projects/shares/writeups/machine_learning/pics/bad_case.pdf',format='pdf')
    
if __name__ == '__main__':
    main()