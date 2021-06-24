    """
    Contiene las funciones de machine learning
    """
    import os, sys
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.svm import SVC
    from sklearn import metrics
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import GridSearchCV, RepeatedKFold
    from sklearn.model_selection import train_test_split
    from sklearn.decomposition import PCA



    def mlear(dataframe):

        x = np.array(dataframe.iloc[:, :-1])
        y = np.array(dataframe.iloc[:, -1])

        x_train, x_test, y_train, y_test =train_test_split(x, y, test_size= 0.2, random_state= 42)
        
        pipe = Pipeline(steps=[('pca', PCA())
    ('classifier', RandomForestClassifier())])

        log_reg_params = {
            'classifier': [LogisticRegression()],
            
        }

        random_forest_params = {
            'classifier': [RandomForestClassifier()],
            'classifier__n_estimators': [10, 100],
            'classifierr__max_features': [1,2,3]
        }

        svm_params = {
            'classifier': [svm.SVC()],
            'classifier__kernel': ('linear'),
            'classifier__C': [0.001, 0.1, 0.5, 1, 5, 10],
            'classifier__gamma': ('scale', 'auto')
            
        }

        search_space = [
            log_reg_params,
            random_forest_params,
            svm_params
        ]

        clf = GridSearchCV(estimator = pipe,
                        param_grid = search_space,
                        cv = 10,
                        verbose=50,
                        n_jobs=-1)

        clf.fit(x_train, y_train)

        return clf.best_estimator_.predict(x)


