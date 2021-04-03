from pandas import read_csv, DataFrame
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.ensemble import AdaBoostClassifier


valid_cols = ['Permit Type','Action Type','Work Type','Status','Category']
# Load dataset
def load_train_data(csv_fileName):
	data = read_csv(csv_fileName, usecols=valid_cols)
	dataset = data.values

	X = dataset[:, :-1]
	y = dataset[:, -1]
	X = X.astype(str)
	return X,y

def load_test_data(csv_fileName):
	data = read_csv(csv_fileName, usecols=valid_cols[:-1])
	dataset = data.values
	X = dataset.astype(str)
	return X


def prepare_input(X_tr, X_ts):
	oe = OrdinalEncoder()
	oe.fit(X_tr)
	X_tr_enc = oe.transform(X_tr)
	X_ts_enc = oe.transform(X_ts)
	return X_tr_enc, X_ts_enc

def prepare_target(y_tr):
	le = LabelEncoder()
	le.fit(y_tr)
	y_tr_enc = le.transform(y_tr)
	return y_tr_enc

def reveal_target(y_tr, predicted):
	le = LabelEncoder()
	le.fit(y_tr)
	y = list(le.inverse_transform(predicted))
	return y

def write_to_csv(csv_fileName, prediction):
	data = read_csv(csv_fileName)
	arr1 = list(data['Application/Permit Number'].values)
	arr2 = prediction
	df = DataFrame({'Application/Permit Number':arr1, 'Category':arr2})
	df.to_csv("submissionAdaBoost.csv", index=False)


# load train dataset
X_train, y_train = load_train_data('train_file.csv')
X_test = load_test_data('test_file.csv')

X_train_enc, X_test_enc = prepare_input(X_train, X_test)
y_train_enc = prepare_target(y_train)

# print(X_train_enc.shape)
# print(X_test_enc.shape)
# print(y_train_enc.shape)

clf = AdaBoostClassifier(n_estimators=100, random_state=0)
clf.fit(X_train_enc, y_train_enc)
predicted = clf.predict(X_test_enc)
# print(predicted)
y_predicted = reveal_target(y_train, predicted)

# print(len(y_predicted))
write_to_csv('test_file.csv', y_predicted)
print('submission_AdaBoost.csv file is created')
