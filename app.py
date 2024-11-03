from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open("log_model.pkl", "rb"))

@app.route('/', methods=["GET", "POST"])
def index():
    prediction = ""
    
    if request.method == "POST":
        # Retrieve form data and ensure correct data types
        try:
            GENDER = int(request.form["Gender"])
            MARRIED = int(request.form["Married"])
            DEPENDENTS = int(request.form["Dependents"])
            EDUCATION = int(request.form["Education"])
            SELF_EMPLOYED = int(request.form["Self_Employed"])
            APPLICANT_INCOME = int(request.form["ApplicantIncome"])
            COAPPLICANT_INCOME = float(request.form["CoapplicantIncome"])
            LOAN_AMOUNT = float(request.form["LoanAmount"])
            LOAN_AMOUNT_TERM = int(request.form["Loan_Amount_Term"])
            CREDIT_HISTORY = float(request.form["Credit_History"])
            PROPERTY_AREA = int(request.form["Property_Area"])
        
            # Arrange data for prediction
            data = np.array([[GENDER, MARRIED, DEPENDENTS, EDUCATION, SELF_EMPLOYED, 
                             APPLICANT_INCOME, COAPPLICANT_INCOME, LOAN_AMOUNT, 
                             LOAN_AMOUNT_TERM, CREDIT_HISTORY, PROPERTY_AREA]])

            # Make prediction
            result = model.predict(data)
            
            if result[0] == 1:
                prediction = "LOAN APPROVED"
            else:
                prediction = "LOAN NOT APPROVED"
        except Exception as e:
            prediction = f"Error in input: {e}"

    return render_template("home.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)


