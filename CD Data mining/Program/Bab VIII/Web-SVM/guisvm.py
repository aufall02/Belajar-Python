from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('svm.html')

@app.route("/predict", methods=['POST'])
def predict():
	"""impor data latih iris""" 
	data=pd.read_csv('penjurusan.csv')
	df=pd.DataFrame(data,columns=['No.','Nilai IPA','Nilai IPS','jurusan'])
	X=np.asarray(data)
	x_train=X[:,1:3]
	y_train=X[:,3:4]
	#model SVM
	models = svm.SVC(kernel='linear', C=5)
	models.fit(x_train, y_train) 
	# ambil data input dan prediksi
	var1 = request.form['variable1']
	var2 = request.form['variable2']
	vara = np.asarray(var1)
	varb = np.asarray(var2)
	data = [[vara,varb]]
	y=models.predict(data)

	return render_template('result.html', hasil=y)
if __name__ == '__main__':
    app.run(port=4995)