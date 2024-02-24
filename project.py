# -*- coding: utf-8 -*-
"""Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rY3o2-DwoluKb4ssYR6epqUtPs0Zv00V
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('NSL_KDD_SET.csv')
df.head()

df.drop('id',axis=1,inplace=True)
df.head()

df_dup=pd.read_csv("NSL_KDD_SET.csv")
df_dup.drop(["'protocol_type'","'service'","'flag'","id"],1,inplace=True)
df_dup["'class'"]=df_dup["'class'"].replace({"normal":1,"anomaly":0})

cor=df_dup.corr()

plt.figure(figsize=(12,14))
sns.heatmap(cor,annot=True,cmap=plt.cm.Reds)
plt.show()

cor_tgt=abs(cor["'class'"])
req_ftr=cor_tgt[cor_tgt>0.5]

df.drop(["'duration'","'protocol_type'","'src_bytes'","'dst_bytes'","'land'","'wrong_fragment'","'urgent'","'hot'","'num_failed_logins'","'num_compromised'","'root_shell'","'su_attempted'","'num_root'","'num_file_creations'","'num_shells'","'num_access_files'","'num_outbound_cmds'","'is_host_login'","'is_guest_login'","'srv_count'","'rerror_rate'","'srv_rerror_rate'","'diff_srv_rate'","'srv_diff_host_rate'","'dst_host_count'","'dst_host_diff_srv_rate'","'dst_host_same_src_port_rate'","'dst_host_srv_diff_host_rate'","'dst_host_rerror_rate'","'dst_host_srv_rerror_rate'"],axis=1,inplace=True)
df.head()

X=df.iloc[:,:-1].values
Y=df.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0,1])],remainder='passthrough')
XN=ct.fit_transform(X)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
YN=le.fit_transform(Y)

from sklearn.model_selection import train_test_split
X_tr,X_te,Y_tr,Y_te=train_test_split(XN,YN,test_size=0.3,random_state=5,stratify=YN)

from sklearn.preprocessing import Normalizer
nm=Normalizer()
X_tr[:,:]=nm.fit_transform(X_tr[:,:])

from sklearn.preprocessing import Normalizer
nm1=Normalizer()
X_te[:,:]=nm1.fit_transform(X_te[:,:])

from sklearn.ensemble import RandomForestClassifier
randomForest=RandomForestClassifier(n_estimators=3,criterion='entropy',random_state=5)

randomForest.fit(X_tr,Y_tr)
Y_pred=randomForest.predict(X_te)

from sklearn.metrics import confusion_matrix,accuracy_score,f1_score,recall_score, mean_squared_error
from math import sqrt
accuracy_RF = accuracy_score(Y_te,Y_pred)
f1_RF = f1_score(Y_te,Y_pred)
recall_RF = recall_score(Y_te,Y_pred)
rmse_RF = sqrt(mean_squared_error(Y_te,Y_pred))

print("Confusion matrix: ",confusion_matrix(Y_te,Y_pred))
print("Accuracy: ", accuracy_RF)
print("F1 Score: ",f1_RF)
print("Recall: ",recall_RF)
print("RMSE: ",rmse_RF)

from sklearn.model_selection import GridSearchCV
rf=RandomForestClassifier(random_state=5)
params={'n_estimators':[5, 10, 25, 50, 75, 100, 125, 150]}
rf_gs=GridSearchCV(rf,params,'accuracy')
rf_gs.fit(X_tr,Y_tr)

rf_best=rf_gs.best_estimator_
print(rf_gs.best_params_)
Y_rf_predict= rf_best.predict(X_te)

accuracy_GRF = accuracy_score(Y_te,Y_rf_predict)
f1_GRF = f1_score(Y_te,Y_rf_predict)
recall_GRF = recall_score(Y_te,Y_rf_predict)
rmse_GRF = sqrt(mean_squared_error(Y_te,Y_rf_predict))

print("Accuracy: ",accuracy_GRF)
print("F1 Score: ",f1_GRF)
print("Recall: ",recall_GRF)
print("RMSE: ",rmse_GRF)

from pandas import DataFrame
data = []
rf = []
rf.append(accuracy_RF)
rf.append(f1_RF)
rf.append(recall_RF)
rf.append(rmse_RF)
rf.append('RandomForest')
grf = []
grf.append(accuracy_GRF)
grf.append(f1_GRF)
grf.append(recall_GRF)
grf.append(rmse_GRF)
grf.append('GridSearch_RF')
data.append(rf)
data.append(grf)
df = DataFrame (data,columns=['accuracy', 'f1_score', 'recall', 'RMSE', 'class'])

ax = df.plot(x='class', y=["accuracy", "f1_score", "recall",'RMSE'], kind="bar",figsize=(10,10), width=0.6)
for p in ax.patches:
  ax.annotate(str(round(p.get_height(),4)), (p.get_x() * 1.005, p.get_height() * 1.005))
plt.show()

"""AdaBoost"""

from sklearn.ensemble import AdaBoostClassifier
adaBoost=AdaBoostClassifier(random_state=5)
adaBoost.fit(X_tr,Y_tr)
Y1_pred=adaBoost.predict(X_te)

accuracy_AB = accuracy_score(Y_te,Y1_pred)
f1_AB  = f1_score(Y_te,Y1_pred)
recall_AB = recall_score(Y_te,Y1_pred)
rmse_AB=sqrt(mean_squared_error(Y_te,Y1_pred))

print("Confusion matrix: ",confusion_matrix(Y_te,Y1_pred))
print("Accuracy: ",accuracy_AB)
print("F1 Score: ",f1_AB)
print("Recall: ",recall_AB)
print("RMSE: ",rmse_AB)

ada_clf=AdaBoostClassifier(random_state=5)
ada_clf_gs=GridSearchCV(ada_clf,params,'accuracy')
ada_clf_gs.fit(X_tr,Y_tr)

ada_clf_best=ada_clf_gs.best_estimator_
print(ada_clf_gs.best_params_)

Y_ada_predict = ada_clf_best.predict(X_te)

accuracy_GAB = accuracy_score(Y_te,Y_ada_predict)
f1_GAB = f1_score(Y_te,Y_ada_predict)
recall_GAB = recall_score(Y_te,Y_ada_predict)
rmse_GAB=sqrt(mean_squared_error(Y_te,Y_ada_predict))

print("Accuracy: ",accuracy_GAB)
print("F1 Score: ",f1_GAB)
print("Recall: ",recall_GAB)
print("RMSE: ",rmse_GAB)

data = []
ab = []
ab.append(accuracy_AB)
ab.append(f1_AB)
ab.append(recall_AB)
ab.append(rmse_AB)
ab.append('AdaBoost')
gab = []
gab.append(accuracy_GAB)
gab.append(f1_GAB)
gab.append(recall_GAB)
gab.append(rmse_GAB)
gab.append('GridSearch_AB')
data.append(ab)
data.append(gab)
df = DataFrame (data,columns=['accuracy', 'f1_score', 'recall', 'RMSE', 'class'])

ax = df.plot(x='class', y=["accuracy", "f1_score", "recall",'RMSE'], kind="bar",figsize=(10,10), width=0.6)
for p in ax.patches:
  ax.annotate(str(round(p.get_height(),4)), (p.get_x() * 1.005, p.get_height() * 1.005))
plt.show()

"""XGBoost"""

from xgboost import XGBClassifier
mdl=XGBClassifier(random_state=5)
mdl.fit(X_tr,Y_tr)
Y2_pred=mdl.predict(X_te)

accuracy_XB = accuracy_score(Y_te,Y2_pred)
f1_XB = f1_score(Y_te,Y2_pred)
recall_XB = recall_score(Y_te,Y2_pred)
rmse_XB=sqrt(mean_squared_error(Y_te,Y2_pred))

print("Confusion matrix: ", confusion_matrix(Y_te,Y2_pred))
print("Accuracy: ",accuracy_XB)
print("F1 Score: ",f1_XB)
print("Recall: ",recall_XB)
print("RMSE: ",rmse_XB)

from sklearn.model_selection import GridSearchCV
xg=XGBClassifier(random_state=5)
xg_gs=GridSearchCV(xg,params,'accuracy')
xg_gs.fit(X_tr,Y_tr)

xg_best=xg_gs.best_estimator_
print(xg_gs.best_params_)
Y_xg_predict= xg_best.predict(X_te)

accuracy_GXB = accuracy_score(Y_te,Y_xg_predict)
f1_GXB = f1_score(Y_te,Y_xg_predict)
recall_GXB = recall_score(Y_te,Y_xg_predict)
rmse_GXB=sqrt(mean_squared_error(Y_te,Y_xg_predict))

print("Accuracy: ",accuracy_GXB)
print("F1 Score: ",f1_GXB)
print("Recall: ",recall_GXB)
print("RMSE: ",rmse_GXB)

data = []
xb = []
xb.append(accuracy_XB)
xb.append(f1_XB)
xb.append(recall_XB)
xb.append(rmse_XB)
xb.append('XgBoost')
gxb = []
gxb.append(accuracy_GXB)
gxb.append(f1_GXB)
gxb.append(recall_GXB)
gxb.append(rmse_GXB)
gxb.append('GridSearch_XB')
data.append(xb)
data.append(gxb)
df = DataFrame (data,columns=['accuracy', 'f1_score', 'recall', 'RMSE', 'class'])

ax = df.plot(x='class', y=["accuracy", "f1_score", "recall",'RMSE'], kind="bar",figsize=(10,10), width=0.6)
for p in ax.patches:
  ax.annotate(str(round(p.get_height(),4)), (p.get_x() * 1.005, p.get_height() * 1.005))
plt.show()

"""Ensemble Model - VotingClassifier"""

from sklearn.ensemble import VotingClassifier
estimators=[('rf',rf_best),('ada_clf',ada_clf_best),('xg',xg_best)]
ensemble = VotingClassifier(estimators, voting='hard')
ensemble.fit(X_tr,Y_tr)

Y_ens_pred=ensemble.predict(X_te)

accuracy_ensemble = accuracy_score(Y_te,Y_ens_pred)
f1_ensemble = f1_score(Y_te,Y_ens_pred)
recall_ensemble = recall_score(Y_te,Y_ens_pred)
rmse_ensemble = sqrt(mean_squared_error(Y_te,Y_ens_pred))

print("Accuracy: ",accuracy_ensemble)
print("F1 score: ",f1_ensemble)
print("Recall: ",recall_ensemble)
print("RMSE: ",rmse_ensemble)

from pandas import DataFrame
data = []

grf = []
grf.append(accuracy_GRF)
grf.append(f1_GRF)
grf.append(recall_GRF)
grf.append(rmse_GRF)
grf.append('GridSearch_RF')

gab = []
gab.append(accuracy_GAB)
gab.append(f1_GAB)
gab.append(recall_GAB)
gab.append(rmse_GAB)
gab.append('GridSearch_AB')

gxb = []
gxb.append(accuracy_GXB)
gxb.append(f1_GXB)
gxb.append(recall_GXB)
gxb.append(rmse_GXB)
gxb.append('GridSearch_XB')

ens = []
ens.append(accuracy_ensemble)
ens.append(f1_ensemble)
ens.append(recall_ensemble)
ens.append(rmse_ensemble)
ens.append('Ensemble')

data.append(grf)
data.append(gab)
data.append(gxb)
data.append(ens)

df = DataFrame (data,columns=['accuracy', 'f1_score', 'recall', 'RMSE', 'model'])

ax = df.plot(x='model', y='accuracy', kind="bar",figsize=(8,8), width=0.5, legend=None, ylim=(0.9,1))
for p in ax.patches:
  ax.annotate(str(round(p.get_height(),4)), (p.get_x() * 1.004, p.get_height() * 1.001))
plt.title('Comparison of accuracy of all models')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.show()

ax = df.plot(x='model', y='f1_score', kind="bar",figsize=(8,8), width=0.5, legend=None, ylim=(0.9,1))
for p in ax.patches:
  ax.annotate(str(round(p.get_height(),4)), (p.get_x() * 1.004, p.get_height() * 1.001))
plt.title('Comparison of F1 Score of all models')
plt.xlabel('Models')
plt.ylabel('F1 Score')
plt.show()

ax = df.plot(x='model', y='recall', kind="bar",figsize=(8,8), width=0.5,legend=None, ylim=(0.9,1))
for p in ax.patches:
  ax.annotate(str(round(p.get_height(),4)), (p.get_x() * 1.004, p.get_height() * 1.001))
plt.title('Comparison of Recall of all models')
plt.xlabel('Models')
plt.ylabel('Recall')
plt.show()

ax = df.plot(x='model', y='RMSE', kind="bar",figsize=(8,8), width=0.5,legend=None)
for p in ax.patches:
  ax.annotate(str(round(p.get_height(),4)), (p.get_x() * 1.003, p.get_height() * 1.005))
plt.title('Comparison of RMSE of all models')
plt.xlabel('Models')
plt.ylabel('RMSE')
plt.show()

import pickle
filename = 'model_file.sav'
pickle.dump(rf_best, open(filename, 'wb'))

