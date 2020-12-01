
from flask import Flask,render_template,request
import numpy as np
import pandas as pd
app = Flask(__name__)
import pickle
model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/predict", methods=["GET","POST"])
def predict():
   int_features = [float(x) for x in request.form.values()]
   final_features = [np.array(int_features)]
   if (final_features[0][2] == 3):
     cp_3 = 1.0
   else:
     cp_3 = 0.0
   if (final_features[0][2] == 2):
     cp_2 = 1.0
   else:
     cp_2 = 0.0
   if (final_features[0][2] == 1):
     cp_1 = 1.0
   else:
     cp_1 = 0.0
   if (final_features[0][2] == 0):
     cp_0 = 1.0
   else:
     cp_0 = 0.0

   if (final_features[0][6] == 2):
     ecg_2 = 1.0
   else:
     ecg_2 = 0.0
   if (final_features[0][6] == 1):
     ecg_1 = 1.0
   else:
     ecg_1 = 0.0
   if (final_features[0][6] == 0):
     ecg_0 = 1.0
   else:
     ecg_0 = 0.0

   dictionary = {'age':[final_features[0][0]], 'gender':[final_features[0][1]], 'trestbps':[final_features[0][3]],
              'chol':[final_features[0][4]], 'fbs':[final_features[0][5]], 'thalach':[final_features[0][7]],
              'exang':[final_features[0][8]], 'cp_0':[cp_0], 'cp_1':[cp_1], 'cp_2':[cp_2],
              'cp_3':[cp_3], 'restecg_0':[ecg_0], 'restecg_1':[ecg_1], 'restecg_2':[ecg_2]}
   df = pd.DataFrame(dictionary)
   result = model.predict(np.array(df))
   if (result == 0):
     text = "You don't have any Heart Disease."
   else:
     text = "You have the Heart Disease. Consult a doctor as soon as possible."
   return render_template('index.html', prediction_text= text)

if __name__ == "__main__":
  app.run()