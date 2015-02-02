'''
Created on 3 Sep 2014

@author: chris

From sklearn tutorials - reduced
'''
"""Build a sentiment analysis / polarity model

Sentiment analysis can be casted as a binary text classification problem,
that is fitting a linear classifier on features extracted from the text
of the user messages so as to guess wether the opinion of the author is
positive or negative.

In this examples we will use a movie review dataset.

"""
# Author: Olivier Grisel <olivier.grisel@ensta.org>
# License: Simplified BSD

import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn import metrics


if __name__ == "__main__":
    # NOTE: we put the following in a 'if __name__ == "__main__"' protected
    # block to be able to use a multi-core grid search that also works under
    # Windows, see: http://docs.python.org/library/multiprocessing.html#windows
    # The multiprocessing module is used as the backend of joblib.Parallel
    # that is used when n_jobs != 1 in GridSearchCV
    
    movie_reviews_data_folder = '/home/chris/Work/projects/shares/learning/scikits_learn/tutorial/text_analytics/data/movie_reviews/txt_sentoken/'
    dataset = load_files(movie_reviews_data_folder, shuffle=True)
    
    N_samp = 800
    print("n_samples: %d" % len(dataset.data[:N_samp]))

    # split the dataset in training and test set:
    data = dataset.data[:N_samp]
    target = dataset.target[:N_samp]
    print dataset.target_names
    
    docs_train, docs_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=5)

    # TASK: Build a vectorizer / classifier pipeline that filters out tokens
    # that are too rare or too frequent
    
    vect = TfidfVectorizer(stop_words='english')
    
    # TASK: Build a grid search to find out whether unigrams or bigrams are
    # more useful.
    # Fit the pipeline on the training set using grid search for the parameters
    
    clf = Pipeline([('vect', vect),
                    ('clf',LinearSVC())
                   ]) 
    
    parameters = {'vect__ngram_range': [(1, 1), (1, 2)]
                 }

    
    gs_clf = GridSearchCV(clf, parameters, n_jobs=-1)
    
    gs_clf = gs_clf.fit(docs_train, y_train)
    
    best_parameters, score, _ = max(gs_clf.grid_scores_, key=lambda x: x[1])
    for param_name in sorted(parameters.keys()):
        print("%s: %r" % (param_name, best_parameters[param_name]))
        
    y_predicted = gs_clf.predict(docs_test)
    
    print metrics.classification_report(y_test,y_predicted,
                                        target_names=dataset.target_names)
    
    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)

    import matplotlib.pyplot as plt
    plt.matshow(cm)
    plt.show()
    