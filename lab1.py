import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
data,target=load_boston(return_X_y=True)
from sklearn.model_selection import cross_val_score, ShuffleSplit
from sklearn import linear_model
    #回归函数\
def regression(model,boston_data,boston_target,splits,size):
   #n折交叉验证并打乱数据集顺序
        shuffle = ShuffleSplit(n_splits=splits, test_size=size, random_state=7)
        n_fold = 1
        score_all = 0
        X = boston_data
        Y = boston_target
        #训练测试循环
        for train_indices, test_indices in shuffle.split(boston_data):
            print('fold {}/{}'.format(n_fold,splits))
            #获取此折的数据
            x_train = X[train_indices]
            y_train = Y[train_indices]
            x_test = X[test_indices]
            y_test = Y[test_indices]
            #模型训练
            model.fit(x_train,y_train)
            #计算决定系数R^2
            score = model.score(x_test, y_test)
            #测试
            result = model.predict(x_test)
            #画图
            plt.plot(np.arange(len(result)), y_test,label='true value')
            plt.plot(np.arange(len(result)),result,label='predict value')
            plt.show()
            print(score)
            score_all += score
            n_fold += 1
        print("average score:",score_all/splits)
#加载数据/这里由于load_boston将在1.2版本中取消，此时使用会有警告，
#为了展示的连续性与美观，故使用其他方式加载该数据集
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
print("data of boston:",data.shape)
print("target of boston:",target.shape)
#实例化线性回归模型
model_Linear = linear_model.LinearRegression()
#参数为5折验证，测试集占20%
regression(model_Linear,data,target,splits=5,size=0.2)
