import requests


#### define ip of wae controller and port to connect on
# wae = "198.18.134.26"
# port = "7777"
# url = "http://" + wae + ":" + port + "/wae/network/collected/entities/tunnel/pcep/get-all-tunnels"



def listpaths(wae, port):
    url = "http://" + wae + ":" + port + "/wae/network/collected/entities/tunnel/pcep/get-all-tunnels"

    ##### set headers
    headers = {
        'cache-control': "no-cache",
        }


    #### send as get request
    response = requests.request("GET", url, headers=headers)

    ####return tunnel paths
    print(response.text)
