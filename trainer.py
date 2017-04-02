import pandas
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
import numpy
import matplotlib.pylab as plt

def return_nonstring_col(data_cols):
	cols_to_keep=[]
	train_cols=[]
	for col in data_cols:
		if col!='URL' and col!='host' and col!='path':
			cols_to_keep.append(col)
			if col!='malicious' and col!='result':
				train_cols.append(col)
	return [cols_to_keep,train_cols]

# Called from gui
def forest_classifier_gui(training_set,query,train_cols):

	rf = RandomForestClassifier(n_estimators=150)

	print rf.fit(training_set[train_cols], training_set['malicious'])

	query['result']=rf.predict(query[train_cols])

	print query[['URL','result']].head(2)
	return query['result']

def train_and_test(db,test_db):
	
	query_csv = pandas.read_csv(test_db)
	train_csv = pandas.read_csv(db)

	cols_to_keep,train_cols=return_nonstring_col(train_csv.columns)

	return forest_classifier_gui(train_csv,query_csv,train_cols)	

