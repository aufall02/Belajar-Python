from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
import keras
from keras.models import model_from_yaml
app = Flask(__name__)

#ambil model JST yg sudah dilatih
yaml_file = open('jurusan.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
#Mengambil bobot JST
loaded_model.load_weights("jurusan.h5")
loaded_model.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])
loaded_model.summary()

@app.route("/")
def template_test():
    return render_template('jst.html')

@app.route("/predict", methods=['POST'])
def predict():
	model=loaded_model
	#model.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])	
	ipa = request.form['variable1']
	ips = request.form['variable2']
	vara = np.asarray(ipa)
	varb = np.asarray(ips)
	data = [[vara,varb]]
	y=model.predict(np.asarray(data))
	#y=1;
	#y = loaded_model.predict(np.asarray(data))
	return render_template('result.html', hasil=y)
if __name__ == '__main__':
    app.run(debug=True,port=4995)
