
import pickle
import sklearn
from sklearn import linear_model
import numpy as np

__model = None

def get_HealthStatus(MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Shimmer,HNR,RPDE,DFA,SPREAD2,D2,PPE):

	x = np.zeros(11)
	x[0] = MDVP_Fo
	x[1] = MDVP_Fhi
	x[2] = MDVP_Flo
	x[3] = MDVP_Jitter
	x[4] = MDVP_Shimmer
	x[5] = HNR
	x[6] = RPDE
	x[7] = DFA
	x[8] = SPREAD2
	x[9] = D2
	x[10] = PPE



	with open("Pearkinson_Prediction_model.pickle", 'rb') as f:
		__model = pickle.load(f)

		return int(__model.predict([x])[0])





if __name__ == "__main__":

	print(get_HealthStatus(119.992,157.302,74.997,0.007,0.0437,21.033,0.414783,0.815285,0.266,2.301,0.28))



