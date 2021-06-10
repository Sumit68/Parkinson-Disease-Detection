from flask import Flask,request,jsonify
import util
app = Flask(__name__)

@app.route('/predict_disease',methods=['POST'])
def predict_disease():
	MDVP_Fo = request.form['MDVP_Fo']
	MDVP_Fhi = request.form['MDVP_Fhi']
	MDVP_Flo = float(request.form['MDVP_Flo'])
	MDVP_Jitter = request.form['MDVP_Jitter']
	MDVP_Shimmer = request.form['MDVP_Shimmer']
	HNR = request.form['HNR']
	RPDE = request.form['RPDE']
	DFA = float(request.form['DFA'])
	SPREAD2 = float(request.form['SPREAD2'])
	D2 = float(request.form['D2'])
	PPE = float(request.form['PPE'])

	response = jsonify({
		'HealthStatus': util.get_HealthStatus(MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Shimmer,HNR,RPDE,DFA,SPREAD2,D2,PPE)
	})

	response.headers.add('Access-Control-Allow-Origin', '*')

	return response


if __name__ == "__main__":
	print("Starting Server.")
	app.run() 