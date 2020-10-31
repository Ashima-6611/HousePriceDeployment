from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        hage = request.form["houseage"]
        hage = int(hage)
        print(hage)
        rooms = request.form["noofrooms"]
        rooms = int(rooms)
        print(rooms)
        bed = request.form["noofbedrooms"]
        bed = int(bed)
        print(bed)
        pop = request.form["areapopulation"]
       	pop = float(pop)
        print(pop)      
        list1=[[hage,rooms,bed,pop]]  
        print(list1)
        price = np.abs(model.predict(list1))
        return render_template('index.html',prediction_text="Price in Lakhs={}".format(price))

if __name__ == "__main__":
    app.run(debug=True)
    
    