import requests

# #### define ip of wae controller and port to connect on
# wae= "198.18.134.26"
# port= "7777"

# ####define tunnel path you want to edit and what node you want the changes to be placed on
# tname= "tunnel-1"
# node= "node-1"

# #### set options for tunnel bandwidth hold and set priorities 
# bw = "5"
# holdpri = "3"
# setupri = "3"

def modifyLSP(wae, port, tname, node, bw, holdpri, setupri):
	
	url = "http://" + wae + ":"  + port + "/wae/network/modeled/entities/tunnel/modify"

	#### form Json
	payload = "{  \n  \"lspKey\" : {  \n    \"name\" : \"%s\",  \n    \"node\" : {  \n      \"name\" : \"%s\"  \n    }  \n  },  \n  \"lspModifiableFields\" : {  \n    \"setupBW\" : %s,  \n    \"holdPri\" : %s,  \n    \"setupPri\" : %s  \n  }  \n}" %(tname, node, bw, holdpri, setupri)
	#### set headers
	headers = {
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    }
	#### create post and send
	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)



