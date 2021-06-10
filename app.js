
function OnClickPredict(e) {
			e.preventDefault();
			
			var MDVP_Fo = document.getElementById("mdvp:fo");
			var MDVP_Fhi = document.getElementById("mdvp:fhi");
			var MDVP_Flo = document.getElementById("mdvp:flo");
            var MDVP_Jitter = document.getElementById("mdvp:jitter");
            var MDVP_Shimmer = document.getElementById("mdvp:shimmer");
            var HNR = document.getElementById("hnr");
            var RPDE = document.getElementById("rpde");
            var DFA = document.getElementById("dfa");
            var SPREAD2 = document.getElementById("spread2");
            var D2 = document.getElementById("d2");
            var PPE = document.getElementById("ppe");

			var url = "http://127.0.0.1:5000/predict_disease";
			$.post(url, {
				
				MDVP_Fo : parseFloat(MDVP_Fo.value),
                MDVP_Fhi : parseFloat(MDVP_Fhi.value),
                MDVP_Flo : parseFloat(MDVP_Flo.value),
                MDVP_Jitter : parseFloat(MDVP_Jitter.value),
                MDVP_Shimmer : parseFloat(MDVP_Shimmer.value),
                HNR : parseFloat(HNR.value),
                RPDE : parseFloat(RPDE.value),
                DFA : parseFloat(DFA.value),
                SPREAD2 : parseFloat(SPREAD2.value),
                D2 : parseFloat(D2.value),
                PPE: parseFloat(PPE.value)
                   
				
			},function(data, status) {
				var num =  data.HealthStatus*1;
                var healthstatus;
                if (num=='1') {
                    healthstatus = "You seem safe"
                } else {
                    healthstatus = "You are infected please visit doctor123."
  
                }
				
				document.getElementById("result").innerHTML = healthstatus;
				//console.log(status);
                console.log(num)
			});
			
} 