# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2019/11/21 13:44
# @Author  : wanghd
# @note    : lightgbm练习

import os
from loguru import logger
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(BASE_DIR, f"Log/{os.path.basename(__file__)}.log")
# 仅记录100kb日志， 保留近10天的日志
logger.add(log_file_path, encoding='utf-8', rotation='100 kb', retention='10 days')


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report as cr
import xgboost as xgb
import lightgbm as lgb
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
        "n_estimators": list(range(50, 200, 50)),  # 候选1000
        "learning": [0.01, 0.05, 0.1, 0.15, 0.2],
        "max_depth": list(range(3, 7)),  # 候选 8
        "gamma": np.linspace(0.1, 0.2, 5),
        "subsample": np.linspace(0.5, 1, 5),
        "colsample_bytree": np.linspace(0.5, 1, 5),
    }
    # lgb_model = lgb.LGBMClassifier(objective='binary')
    lgb_model = lgb.LGBMClassifier(objective='binary', num_leaves=40, max_depth=9, learning_rate=0.05)
    lgb_param = {
        # "num_leaves": list(range(10, 60, 10)),
        # 'max_depth': list(range(3, 10, 1)),
        # 'learning_rate': [0.001, 0.01, 0.05, 0.1, 0.2, 0.3],
        'n_estimators': list(range(100, 300, 10)),
    }
    models = [dt, lr, svc, knn, xx, lgb_model]
    models = [lgb_model]
    params = [dt_param, lr_param, svc_param, knn_param, xx_param]
    params = [lgb_param]
    for model, param in zip(models, params):
        try:
            # clf = GridSearchCV(model,
            #                    param_grid=param,
            #                    cv=5,
            #                    error_score=0,
            #                    scoring='roc_auc')
            clf = RandomizedSearchCV(model,
                                     param_distributions=param,
                                     cv=5,
                                     error_score=0,
                                     scoring='roc_auc')
            clf.fit(train_x, train_y)
            print("{:*^30}".format(model.__class__.__name__))
            print("best_params:", clf.best_params_)
            print("best_scores:", clf.best_score_)
            print("best_auc:", roc_auc_score(train_y, clf.best_estimator_.predict(train_x)))
            print("best_accuracy:", accuracy_score(train_y, clf.best_estimator_.predict(train_x)))
            print("best confusion matrix:")
            print(confusion_matrix(train_y, clf.best_estimator_.predict(train_x)))
            print("Average Time to Fit(s) {}".format(round(clf.cv_results_['mean_fit_time'].mean(), 3)))
            print("Average Time to Score(s) {}".format(round(clf.cv_results_['mean_score_time'].mean(), 3)))
            print("feature_importance:", clf.best_estimator_.feature_importances_)
        except Exception as e:
            print(str(e))
    return clf.best_estimator_

@logger.catch
def main():
    import lightgbm as lgb
    from sklearn.datasets import load_iris

    # 加载数据
    iris = load_iris()
    data = iris.data
    target = iris.target
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2)

    # 创建模型，训练模型
    gbm = lgb.LGBMClassifier(objective='multiclass', num_leaves=31, learning_rate=0.05, n_estimators=40)
    gbm.fit(X_train, y_train, feature_name=iris.feature_names, eval_set=[(X_test, y_test)], eval_metric='logloss',
            early_stopping_rounds=5)

    # 测试机预测
    y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration_)

    # 模型评估
    print('confusion matrix:', confusion_matrix(y_test, y_pred))
    print('accuracy::', accuracy_score(y_test, y_pred))

    # feature importances
    print(gbm.n_features_)
    print('Feature importances:', list(gbm.feature_importances_))

    # 网格搜索，参数优化
    estimator = lgb.LGBMRegressor(num_leaves=31)
    param_grid = {
        'learning_rate': [0.01, 0.1],
        'n_estimators': [20, 40, 50]
    }
    gbm = GridSearchCV(estimator, param_grid)
    gbm.fit(X_train, y_train)
    print('Best parameters found by grid search are:', gbm.best_params_)


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    train_x, train_y = get_data()
    train_x = feature_engineering(train_x)
    # best_estimator = my_model_selection(train_x, train_y)
    best_estimator = lgb.LGBMClassifier(objective='binary', num_leaves=40, max_depth=9, learning_rate=0.05,
                                        n_estimators=140, random_state=999)
    best_estimator.fit(train_x, train_y)
    print(best_estimator)
    print("best_scores:", best_estimator.best_score_)
    print("best_auc:", roc_auc_score(train_y, best_estimator.predict(train_x)))
    print("best_accuracy:", accuracy_score(train_y, best_estimator.predict(train_x)))
    print("best confusion matrix:")
    print(confusion_matrix(train_y, best_estimator.predict(train_x)))
    test_x = pd.read_csv("../data/test_set.csv")
    test_index = test_x.pop("ID")
    test_x = feature_engineering(test_x)
    pred_label = pd.DataFrame(best_estimator.predict_proba(test_x)[:, 1], columns=['pred'], index=test_index)
    pred_label.to_csv("../data/result_lgb.csv", index=True, header=True)

    random_state = 999
    classifiers = [DecisionTreeClassifier(random_state=random_state),
                   # LogisticRegression(random_state=random_state),
                   best_estimator,
                   # KNeighborsClassifier(),
                   RandomForestClassifier(random_state=random_state),
                   GradientBoostingClassifier(random_state=random_state)]
    from combo.models.classifier_stacking import Stacking
    from combo.utils.data import evaluate_print

    clf = Stacking(base_estimators=classifiers, n_folds=3, shuffle_data=True,
                   keep_original=True, use_proba=False, random_state=random_state)

    clf.fit(train_x, train_y)
    y_test_predict = clf.predict(train_x)
    evaluate_print('Stacking | ', train_y, y_test_predict)

    from combo.models.classifier_comb import SimpleClassifierAggregator

    clf = SimpleClassifierAggregator(classifiers, method='average')
    clf.fit(train_x, train_y)
    y_test_predicted = clf.predict(train_x)
    evaluate_print('Combination by avg   |', train_y, y_test_predicted)