import requests

class WAEWrapper():

	def createLSP(self, wae, port, tname, tsource, tdest):
		url = "http://" + wae + ":" + port + "/wae/network/modeled/entities/tunnel/new/admit/basic"
		payload = "{\r\n  \"teTunnel\" : {\r\n    \"name\" : \"%s\",\r\n    \"source\" : \"%s\",\r\n    \"destination\" : \"%s\",\r\n    \"pcep\" : false\r\n  }\r\n}"%(tname, tsource,tdest)
		headers = {
		    'content-type': "application/json",
		    'cache-control': "no-cache",
		    }
		response = requests.request("POST", url, data=payload, headers=headers)
		print(response.text)


	def listPaths(self, wae, port):
		url = "http://" + wae + ":" + port + "/wae/network/collected/entities/tunnel/pcep/get-all-tunnels"
		headers = {
		    'cache-control': "no-cache",
		    }
		response = requests.request("GET", url, headers=headers)
		print(response.text)


	def modifyLSP(self, wae, port, tname, node, bw, holdpri, setupri):
		url = "http://" + wae + ":"  + port + "/wae/network/modeled/entities/tunnel/modify"
		payload = "{  \n  \"lspKey\" : {  \n    \"name\" : \"%s\",  \n    \"node\" : {  \n      \"name\" : \"%s\"  \n    }  \n  },  \n  \"lspModifiableFields\" : {  \n    \"setupBW\" : %s,  \n    \"holdPri\" : %s,  \n    \"setupPri\" : %s  \n  }  \n}" %(tname, node, bw, holdpri, setupri)
		headers = {
		    'content-type': "application/json",
		    'cache-control': "no-cache",
		    }
		response = requests.request("POST", url, data=payload, headers=headers)
		print(response.text)
