# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2019/7/16 13:51
# @Author  : wanghd
# @note    : 银行二分类电话营销预测 https://www.kesci.com/home/competition/5c234c6626ba91002bfdfdd3

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report as cr
import xgboost as xgb
from sklearn.base import TransformerMixin
from copy import deepcopy
import warnings


class CustomDummifier(TransformerMixin):
    """类别（定类）特征热编码，利用pandas.get_dummies"""

    def __init__(self, cols=None):
        self.cols = cols

    def transform(self, x):
        return pd.get_dummies(x, columns=self.cols)

    def fit(self, *_):
        return self


class CustomEncoder(TransformerMixin):
    """定序特征标签编码（相当于映射为数值, 从小到大）"""

    def __init__(self, col, ordering=None):
        self.ordering = ordering
        self.col = col

    def transform(self, x):
        map_dict = {k: v for k, v in zip(self.ordering, range(len(self.ordering)))}
        # x[self.col] = x[self.col].map(lambda value: self.ordering.index(value))
        x[self.col] = x[self.col].map(map_dict)
        return x

    def fit(self, *_):
        return self


def get_data():
    train_set = pd.read_csv("../data/train_set.csv")
    train_set.drop(columns=["ID"], inplace=True)
    train_y = train_set.pop("y")
    return train_set, train_y


def feature_engineering(train_x):
    discrete_cols = ["job", "marital", 'education', 'contact', 'poutcome', 'month']
    label_cols = ["default", "housing", 'loan']
    # pipeline_list = [("onehot",CustomDummifier(discreate_cols)),
    #                  "label_encoder", CustomEncoder(label_cols, ["no", "yes"])]
    # pipeline = Pipeline(pipeline_list)
    ccc = CustomDummifier(cols=discrete_cols)
    train_x = ccc.fit_transform(train_x)
    for col in label_cols:
        ddd = CustomEncoder(col, ["no", "yes"])
        train_x = ddd.fit_transform(train_x)
    print(train_x)
    print(train_x.columns)
    print(train_x.loc[:, label_cols])
    return train_x


def model_base_selection(train_x, train_y):
    training_score = []
    testing_score = []
    model = []
    classifiers = [
        LogisticRegression(),
        KNeighborsClassifier(),
        SVC(),
        DecisionTreeClassifier(), ]
    # RandomForestClassifier(),
    # AdaBoostClassifier(),
    # GaussianNB()]

    x_train, x_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.2, random_state=666)
    for classifier in classifiers:
        model.append(classifier.__class__.__name__)
        classifier.fit(x_train, y_train)
        training_score.append(classifier.score(x_train, y_train))
        testing_score.append(classifier.score(x_test, y_test))
        print("{} : trainning classification report".format(classifier.__class__.__name__))
        print(cr(y_train, classifier.predict(x_train), digits=4))
        print("{} : testing classification report".format(classifier.__class__.__name__))
        print(cr(y_test, classifier.predict(x_test), digits=4))

    for i in range(len(model)):
        print("The {:<25} has a training score of {:^10.4f} and testing score of {:^10.4}".format(model[i],
                                                                                                  training_score[i],
                                                                                                  testing_score[i]))


def my_model_selection(train_x, train_y):
    dt = DecisionTreeClassifier()
    dt_param = {"max_depth": list(range(2, 10)),
                "max_leaf_nodes": np.arange(5, 10, 1),
                "spliters": ["best", "random"]}
    lr = LogisticRegression()
    lr_param = {
        "penalty": ["l2", 'l1'],
        "C": np.linspace(0.001, 0.1, 10)
    }
    svc = SVC()
    svc_param = {
        "C": np.linspace(0.01, 1, 10)
    }
    knn = KNeighborsClassifier()
    knn_param = {
        "n_neighbors": list(range(3, 8))
    }
    xx = xgb.XGBClassifier(objective="binary:logistic", booster='gbtree', n_jobs=-1, random_state=999)
    xx_param = {
        "n_estimators": list(range(50, 200, 50)),
        "learning": [0.05, 0.1, 0.15, 0.2],
        "max_depth": list(range(3, 7)),
        "gamma": np.linspace(0.1, 0.2, 5),
        "subsample": np.linspace(0.5, 1, 5),
        "colsample_bytree":np.linspace(0.5, 1, 5),
    }
    models = [dt, lr, svc, knn]
    models = [lr, xx]
    params = [dt_param, lr_param, svc_param, knn_param]
    params = [lr_param, xx_param]
    for model, param in zip(models, params):
        try:
            clf = GridSearchCV(model,
                               param_grid=param,
                               cv=10,
                               error_score=0, )
            # scoring=roc_auc_score)
            clf.fit(train_x, train_y)
            print("{:*^30}".format(model.__class__.__name__))
            print(clf.best_params_)
            print(clf.best_score_)
            print("Average Time to Fit(s) {}".format(round(clf.cv_results_['mean_fit_time'].mean(), 3)))
            print("Average Time to Score(s) {}".format(round(clf.cv_results_['mean_score_time'].mean(), 3)))
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    train_x, train_y = get_data()
    train_x = feature_engineering(train_x)
    my_model_selection(train_x, train_y)
