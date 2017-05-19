import requests

#### define ip of wae controller and port to connect on
# wae="198.18.134.26"
# port="7777"

### set tunnel name source and dest
# tname="tunnel-1"
# tsource="sjc"
# tdest="rtp"

def createLSP(wae, port, tname, tsource, tdest):



    #### form request url
    url = "http://" + wae + ":" + port + "/wae/network/modeled/entities/tunnel/new/admit/basic"

    #### set json post
    payload = "{\r\n  \"teTunnel\" : {\r\n    \"name\" : \"%s\",\r\n    \"source\" : \"%s\",\r\n    \"destination\" : \"%s\",\r\n    \"pcep\" : false\r\n  }\r\n}"%(tname, tsource,tdest)

    ### set headers
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        }

    #### send post
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
