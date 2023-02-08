# lbdeclient

## Usage
```
-sh-4.2$ python3.6 lbdeclient --help
usage: LbdeClient [-h] [-u BASE_URL] [-H HEADER] [-m METHOD] {request} ...

positional arguments:
  {request}

optional arguments:
  -h, --help            show this help message and exit
  -u BASE_URL, --url BASE_URL
                        The host to submit the request
  -H HEADER, --header HEADER
                        The HTTP headers to be added to the GET/POST request
  -m METHOD, --method METHOD
                        The HTTP method to use
```

### Examples:


#### 1. Run simple http request

+ Command
```
-sh-4.2$ python3.6 lbdeclient -u "https://postman-echo.com/headers" -m get request
```

+ Output
```
2021-03-18 23:31:42,030 [PID 128487] [DEBUG] - connectionpool - 813  Starting new HTTPS connection (1): postman-echo.com:443
2021-03-18 23:31:42,100 [PID 128487] [DEBUG] - connectionpool - 393  https://postman-echo.com:443 "GET /headers HTTP/1.1" 200 240
2021-03-18 23:31:42,101 [PID 128487] [INFO ] - lbdeclient - 428  {"headers":{"x-forwarded-proto":"https","x-forwarded-port":"443","host":"postman-echo.com","x-amzn-trace-id":"Root=1-60541b1e-60ea03d429143f8343ec30d1","user-agent":"python-requests/2.21.0","accept-encoding":"gzip, deflate","accept":"*/*"}}
```


#### 2. Run simple http request with multiple header args

+ Command
```
[br9dusr@cdts99hdbe07d alejandro]$ python3.6 lbdeclient -u "https://postman-echo.com/headers" -m get  -H 'Cache-Control: no-cache' -H 'Content-Type: application/json' request
```
+ Output:
```
2021-03-19 10:35:15,091 [PID 55676] [DEBUG] - connectionpool - 813  Starting new HTTPS connection (1): postman-echo.com:443
2021-03-19 10:35:15,139 [PID 55676] [DEBUG] - connectionpool - 393  https://postman-echo.com:443 "GET /headers HTTP/1.1" 200 301
2021-03-19 10:35:15,140 [PID 55676] [INFO ] - lbdeclient - 489  {"headers":{"x-forwarded-proto":"https","x-forwarded-port":"443","host":"postman-echo.com","x-amzn-trace-id":"Root=1-6054b6a3-798e41ba42f3928354775001","user-agent":"python-requests/2.21.0","accept-encoding":"gzip, deflate","accept":"*/*","cache-control":"no-cache","content-type":"application/json"}}
```
#### 3. Run Advanced bde request, update request payload with query

+ Command

```
python3.6 lbdeclient -u "https://postman-echo.com/post" -m post \
-H 'Cache-Control: no-cache' -H 'Content-Type: application/json' \
request -f template_body.json \
query -i usdhdpimpala.rxcorp.com:21050 -d devl_br9 \
-q "SELECT client_cd, chnl_fltr_lst_desc, pd_typ_fltr_cd, caatg_ntile_lvl_cd, tiling_meas_cd FROM devl_br9.vw_pbs_dm_doc_tiling_param_value_list" \
--update-request "{\"filter\":{\"name\":\"ICE\"}, \"key\":\"values\", \"field\":\"parameters\"}"
```

#### 4. Run http request with data from file

+ Command
```
[br9dusr@cdts99hdbe07d alejandro]$ python3.6 lbdeclient -u "https://postman-echo.com/post" -m post -H 'Cache-Control: no-cache' -H 'Content-Type: application/json' request -f template_body.json
2021-03-19 13:10:30,735 [PID 60875] [INFO ] - lbdeclient - 429  parsing file template_body.json
```

+ Output:
```
{'batch': {'sourceSystem': 'LATAMBDF', 'sourceBatchId': '1'}, 'requests': [{'modelId': 125, 'countryCode': 'BR', 'assetCode': 'Rx', 'applicationCode': 'BR-BDF-RX', 'requestId': 'filtered_Test_sschere_1', 'clientId': '1', 'clientName': 'IMS Health', 'priority': '50', 'successEmails': ['sschere@ar.imshealth.com'], 'failureEmails': ['sschere@ar.imshealth.com'], 'queries': [{'queryId': 'Dim_File_1', 'queryDescription': None, 'fields': [], 'filters': [{'typ': 'ATTRIBUTE', 'entityName': 'v_pbs_bde_fact_gps', 'attributeName': 'client_cd', 'operator': 'IN', 'datatype': 'String', 'values': ['944'], 'value': None}]}], 'parameters': [{'name': 'ICE_FY_YEAR', 'code': 'ICE_FY_YEAR', 'dataType': 'String', 'values': [''], 'description': 'Fiscal Year'}, {'name': 'ICE_FY_START', 'code': 'ICE_FY_START', 'dataType': 'Date', 'values': ['256', '!=0', 'mat', 5, 'rx_itm_cnt', '256', '!=0', 'mat', 5, 'dspnsd_qty', '901', '!=0', 'mat', 5, 'rx_itm_cnt', '901', '!=0', 'mat', 5, 'dspnsd_qty', '907', '!=0', 'mat', 5, 'rx_itm_cnt', '907', '!=0', 'mat', 5, 'dspnsd_qty', '908', '!=0', 'sem', 5, 'rx_itm_cnt', '908', '!=0', 'sem', 5, 'dspnsd_qty', '909', '!=0', 'mat', 5, 'rx_itm_cnt', '909', '!=0', 'mat', 5, 'dspnsd_qty', '913', 'in (1,4)', 'mat', 5, 'rx_itm_cnt', '913', 'in (1,4)', 'mat', 5, 'dspnsd_qty', '921', '!=0', 'mat', 5, 'rx_itm_cnt', '921', '!=0', 'mat', 5, 'dspnsd_qty', '922', 'in (1)', 'mat', 5, 'rx_itm_cnt', '922', 'in (1)', 'mat', 5, 'dspnsd_qty', '926', '!=0', 'sem', 5, 'rx_itm_cnt', '926', '!=0', 'sem', 5, 'dspnsd_qty', '931', '!=0', 'mat', 8, 'rx_itm_cnt', '931', '!=0', 'mat', 8, 'dspnsd_qty', '938', '!=0', 'mat', 5, 'rx_itm_cnt', '938', '!=0', 'mat', 5, 'dspnsd_qty', '939', '!=0', 'mat', 8, 'rx_itm_cnt', '939', '!=0', 'mat', 8, 'dspnsd_qty', '941', '!=0', 'mat', 5, 'rx_itm_cnt', '941', '!=0', 'mat', 5, 'dspnsd_qty', '942', 'in (1,4)', 'mat', 5, 'rx_itm_cnt', '942', 'in (1,4)', 'mat', 5, 'dspnsd_qty', '944', 'in (1,4)', 'mat', 8, 'rx_itm_cnt', '944', 'in (1,4)', 'mat', 8, 'dspnsd_qty', '945', 'in (1,4)', 'mat', 5, 'rx_itm_cnt', '945', 'in (1,4)', 'mat', 5, 'dspnsd_qty', '949', 'in (1,4)', 'mat', 5, 'rx_itm_cnt', '949', 'in (1,4)', 'mat', 5, 'dspnsd_qty', '961', 'in (1)', 'mat', 5, 'rx_itm_cnt', '961', 'in (1)', 'mat', 5, 'dspnsd_qty', '968', 'in (1,4)', 'sem', 5, 'rx_itm_cnt', '968', 'in (1,4)', 'sem', 5, 'dspnsd_qty', '972', '!=0', 'mat', 5, 'rx_itm_cnt', '972', '!=0', 'mat', 5, 'dspnsd_qty', '979', 'in (4,1)', 'mat', 5, 'rx_itm_cnt', '979', 'in (4,1)', 'mat', 5, 'dspnsd_qty', '999', '!=0', 'mat', 5, 'rx_itm_cnt', '999', '!=0', 'mat', 5, 'dspnsd_qty'], 'description': 'Fiscal Start Year'}, {'name': 'ICE_PD_COUNT', 'code': 'ICE_PD_COUNT', 'dataType': 'Number', 'values': ['1'], 'description': 'Period count'}, {'name': 'ICE_PD_END_CURRENT', 'code': 'ICE_PD_END_CURRENT', 'dataType': 'Boolean', 'values': ['true'], 'description': 'Period end current flag'}, {'name': 'ICE_PD_TYPE', 'code': 'ICE_PD_TYPE', 'dataType': 'String', 'values': ['Monthly'], 'description': 'Period type'}], 'templateCode': 'API_Testing_Tiny_Template'}]}
2021-03-19 13:10:30,736 [PID 60875] [INFO ] - lbdeclient - 429  parsing file template_body.json
2021-03-19 13:10:30,736 [PID 60875] [DEBUG] - lbdeclient - 212
METHOD:          POST
AUTH_TYPE:       <class 'requests.auth.HTTPBasicAuth'>
URL:     https://postman-echo.com/post
LOGIN:   None
HEADERS:         {'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}
DATA:    {'batch': {'sourceSystem': 'LATAMBDF', 'sourceBatchId': '1'}, 'requests': [{'modelId': 125, 'countryCode': 'BR', 'assetCode': 'Rx', 'applicationCode': 'BR-BDF-RX', 'requestId': 'filtered_Test_sschere_1', 'clientId': '1', 'clientName': 'IMS Health', 'priority': '50', 'successEmails': ['sschere@ar.imshealth.com'], 'failureEmails': ['sschere@ar.imshealth.com'], 'queries': [{'queryId': 'Dim_File_1', 'queryDescription': None, 'fields': [], 'filters': [{'typ': 'ATTRIBUTE', 'entityName': 'v_pbs_bde_fact_gps', 'attributeName': 'client_cd', 'operator': 'IN', 'datatype': 'String', 'values': ['944'], 'value': None}]}], 'parameters': [{'name': 'ICE_FY_YEAR', 'code': 'ICE_FY_YEAR', 'dataType': 'String', 'values': [''], 'description': 'Fiscal Year'}, {'name': 'ICE_FY_START', 'code': 'ICE_FY_START', 'dataType': 'Date', 'values': ['256', '!=0', 'mat', 5, 'rx_itm_cnt', '256', '!=0', 'mat', 5, 'dspnsd_qty', '901', '!=0', 'mat', 5, 'rx_itm_cnt', '901', '!=0', 'mat', 5, 'dspnsd_qty', '907', '!=0', 'mat', 5, 'rx_itm_cnt', '907', '!=0', 'mat', 5, 'dspnsd_qty', '908', '!=0', 'sem', 5, 'rx_itm_cnt', '908', '!=0', 'sem', 5, 'dspnsd_qty', '909', '!=0', 'mat', 5, 'rx_itm_cnt', '909', '!=0', 'mat', 5, 'dspnsd_qty', '913', 'in (1,4)', 'mat', 5, 'rx_itm_cnt', '913', 'in (1,4)', 'mat', 5, 'dspnsd_qty', '921', '!=0', 'mat', 5, 'rx_itm_cnt', '921', '!=0', 'mat', 5, 'dspnsd_qty', '922', 'in (1)', 'mat', 5, 'rx_itm_cnt', '922', 'in (1)', 'mat', 5, 'dspnsd_qty', '926', '!=0', 'sem', 5, 'rx_itm_cnt', '926', '!=0', 'sem', 5, 'dspnsd_qty', '931', '!=0', 'mat', 8, 'rx_itm_cnt', '931', '!=0', 'mat', 8, 'dspnsd_qty', '938', '!=0', 'mat', 5, 'rx_itm_cnt', '938', '!=0', 'mat', 5, 'dspnsd_qty', '939', '!=0', 'mat', 8, 'rx_itm_cnt', '939', '!=0', 'mat', 8, 'dspnsd_qty', '941', '!=0', 'mat', 5, 'rx_itm_cnt', '941', '!=0', 'mat', 5, 'dspnsd_qty', '942', 'in (1,4)', 'mat', 5, 'rx_itm_cnt', '942', 'in (1,4)', 'mat', 5, 'dspnsd_qty', '944', 'in (1,4)', 'mat', 8, 'rx_itm_cnt', '944', 'in (1,4)', 'mat', 8, 'dspnsd_qty', '945', 'in (1,4)', 'mat', 5, 'rx_itm_cnt', '945', 'in (1,4)', 'mat', 5, 'dspnsd_qty', '949', 'in (1,4)', 'mat', 5, 'rx_itm_cnt', '949', 'in (1,4)', 'mat', 5, 'dspnsd_qty', '961', 'in (1)', 'mat', 5, 'rx_itm_cnt', '961', 'in (1)', 'mat', 5, 'dspnsd_qty', '968', 'in (1,4)', 'sem', 5, 'rx_itm_cnt', '968', 'in (1,4)', 'sem', 5, 'dspnsd_qty', '972', '!=0', 'mat', 5, 'rx_itm_cnt', '972', '!=0', 'mat', 5, 'dspnsd_qty', '979', 'in (4,1)', 'mat', 5, 'rx_itm_cnt', '979', 'in (4,1)', 'mat', 5, 'dspnsd_qty', '999', '!=0', 'mat', 5, 'rx_itm_cnt', '999', '!=0', 'mat', 5, 'dspnsd_qty'], 'description': 'Fiscal Start Year'}, {'name': 'ICE_PD_COUNT', 'code': 'ICE_PD_COUNT', 'dataType': 'Number', 'values': ['1'], 'description': 'Period count'}, {'name': 'ICE_PD_END_CURRENT', 'code': 'ICE_PD_END_CURRENT', 'dataType': 'Boolean', 'values': ['true'], 'description': 'Period end current flag'}, {'name': 'ICE_PD_TYPE', 'code': 'ICE_PD_TYPE', 'dataType': 'String', 'values': ['Monthly'], 'description': 'Period type'}], 'templateCode': 'API_Testing_Tiny_Template'}]}
REQ-OPTS:        <__main__.LatamHttpRequestsOptions object at 0x7fdab3385940>

2021-03-19 13:10:30,738 [PID 60875] [DEBUG] - connectionpool - 813  Starting new HTTPS connection (1): postman-echo.com:443
2021-03-19 13:10:30,794 [PID 60875] [DEBUG] - connectionpool - 393  https://postman-echo.com:443 "POST /post HTTP/1.1" 200 None
2021-03-19 13:10:30,795 [PID 60875] [INFO ] - lbdeclient - 512  {"args":{},"data":{"batch":{"sourceSystem":"LATAMBDF","sourceBatchId":"1"},"requests":[{"modelId":125,"countryCode":"BR","assetCode":"Rx","applicationCode":"BR-BDF-RX","requestId":"filtered_Test_sschere_1","clientId":"1","clientName":"IMS Health","priority":"50","successEmails":["sschere@ar.imshealth.com"],"failureEmails":["sschere@ar.imshealth.com"],"queries":[{"queryId":"Dim_File_1","queryDescription":null,"fields":[],"filters":[{"typ":"ATTRIBUTE","entityName":"v_pbs_bde_fact_gps","attributeName":"client_cd","operator":"IN","datatype":"String","values":["944"],"value":null}]}],"parameters":[{"name":"ICE_FY_YEAR","code":"ICE_FY_YEAR","dataType":"String","values":[""],"description":"Fiscal Year"},{"name":"ICE_FY_START","code":"ICE_FY_START","dataType":"Date","values":["256","!=0","mat",5,"rx_itm_cnt","256","!=0","mat",5,"dspnsd_qty","901","!=0","mat",5,"rx_itm_cnt","901","!=0","mat",5,"dspnsd_qty","907","!=0","mat",5,"rx_itm_cnt","907","!=0","mat",5,"dspnsd_qty","908","!=0","sem",5,"rx_itm_cnt","908","!=0","sem",5,"dspnsd_qty","909","!=0","mat",5,"rx_itm_cnt","909","!=0","mat",5,"dspnsd_qty","913","in (1,4)","mat",5,"rx_itm_cnt","913","in (1,4)","mat",5,"dspnsd_qty","921","!=0","mat",5,"rx_itm_cnt","921","!=0","mat",5,"dspnsd_qty","922","in (1)","mat",5,"rx_itm_cnt","922","in (1)","mat",5,"dspnsd_qty","926","!=0","sem",5,"rx_itm_cnt","926","!=0","sem",5,"dspnsd_qty","931","!=0","mat",8,"rx_itm_cnt","931","!=0","mat",8,"dspnsd_qty","938","!=0","mat",5,"rx_itm_cnt","938","!=0","mat",5,"dspnsd_qty","939","!=0","mat",8,"rx_itm_cnt","939","!=0","mat",8,"dspnsd_qty","941","!=0","mat",5,"rx_itm_cnt","941","!=0","mat",5,"dspnsd_qty","942","in (1,4)","mat",5,"rx_itm_cnt","942","in (1,4)","mat",5,"dspnsd_qty","944","in (1,4)","mat",8,"rx_itm_cnt","944","in (1,4)","mat",8,"dspnsd_qty","945","in (1,4)","mat",5,"rx_itm_cnt","945","in (1,4)","mat",5,"dspnsd_qty","949","in (1,4)","mat",5,"rx_itm_cnt","949","in (1,4)","mat",5,"dspnsd_qty","961","in (1)","mat",5,"rx_itm_cnt","961","in (1)","mat",5,"dspnsd_qty","968","in (1,4)","sem",5,"rx_itm_cnt","968","in (1,4)","sem",5,"dspnsd_qty","972","!=0","mat",5,"rx_itm_cnt","972","!=0","mat",5,"dspnsd_qty","979","in (4,1)","mat",5,"rx_itm_cnt","979","in (4,1)","mat",5,"dspnsd_qty","999","!=0","mat",5,"rx_itm_cnt","999","!=0","mat",5,"dspnsd_qty"],"description":"Fiscal Start Year"},{"name":"ICE_PD_COUNT","code":"ICE_PD_COUNT","dataType":"Number","values":["1"],"description":"Period count"},{"name":"ICE_PD_END_CURRENT","code":"ICE_PD_END_CURRENT","dataType":"Boolean","values":["true"],"description":"Period end current flag"},{"name":"ICE_PD_TYPE","code":"ICE_PD_TYPE","dataType":"String","values":["Monthly"],"description":"Period type"}],"templateCode":"API_Testing_Tiny_Template"}]},"files":{},"form":{},"headers":{"x-forwarded-proto":"https","x-forwarded-port":"443","host":"postman-echo.com","x-amzn-trace-id":"Root=1-6054db06-1b3e75986ecda89f7e0be45f","content-length":"3056","user-agent":"python-requests/2.21.0","accept-encoding":"gzip, deflate","accept":"*/*","cache-control":"no-cache","content-type":"application/json"},"json":{"batch":{"sourceSystem":"LATAMBDF","sourceBatchId":"1"},"requests":[{"modelId":125,"countryCode":"BR","assetCode":"Rx","applicationCode":"BR-BDF-RX","requestId":"filtered_Test_sschere_1","clientId":"1","clientName":"IMS Health","priority":"50","successEmails":["sschere@ar.imshealth.com"],"failureEmails":["sschere@ar.imshealth.com"],"queries":[{"queryId":"Dim_File_1","queryDescription":null,"fields":[],"filters":[{"typ":"ATTRIBUTE","entityName":"v_pbs_bde_fact_gps","attributeName":"client_cd","operator":"IN","datatype":"String","values":["944"],"value":null}]}],"parameters":[{"name":"ICE_FY_YEAR","code":"ICE_FY_YEAR","dataType":"String","values":[""],"description":"Fiscal Year"},{"name":"ICE_FY_START","code":"ICE_FY_START","dataType":"Date","values":["256","!=0","mat",5,"rx_itm_cnt","256","!=0","mat",5,"dspnsd_qty","901","!=0","mat",5,"rx_itm_cnt","901","!=0","mat",5,"dspnsd_qty","907","!=0","mat",5,"rx_itm_cnt","907","!=0","mat",5,"dspnsd_qty","908","!=0","sem",5,"rx_itm_cnt","908","!=0","sem",5,"dspnsd_qty","909","!=0","mat",5,"rx_itm_cnt","909","!=0","mat",5,"dspnsd_qty","913","in (1,4)","mat",5,"rx_itm_cnt","913","in (1,4)","mat",5,"dspnsd_qty","921","!=0","mat",5,"rx_itm_cnt","921","!=0","mat",5,"dspnsd_qty","922","in (1)","mat",5,"rx_itm_cnt","922","in (1)","mat",5,"dspnsd_qty","926","!=0","sem",5,"rx_itm_cnt","926","!=0","sem",5,"dspnsd_qty","931","!=0","mat",8,"rx_itm_cnt","931","!=0","mat",8,"dspnsd_qty","938","!=0","mat",5,"rx_itm_cnt","938","!=0","mat",5,"dspnsd_qty","939","!=0","mat",8,"rx_itm_cnt","939","!=0","mat",8,"dspnsd_qty","941","!=0","mat",5,"rx_itm_cnt","941","!=0","mat",5,"dspnsd_qty","942","in (1,4)","mat",5,"rx_itm_cnt","942","in (1,4)","mat",5,"dspnsd_qty","944","in (1,4)","mat",8,"rx_itm_cnt","944","in (1,4)","mat",8,"dspnsd_qty","945","in (1,4)","mat",5,"rx_itm_cnt","945","in (1,4)","mat",5,"dspnsd_qty","949","in (1,4)","mat",5,"rx_itm_cnt","949","in (1,4)","mat",5,"dspnsd_qty","961","in (1)","mat",5,"rx_itm_cnt","961","in (1)","mat",5,"dspnsd_qty","968","in (1,4)","sem",5,"rx_itm_cnt","968","in (1,4)","sem",5,"dspnsd_qty","972","!=0","mat",5,"rx_itm_cnt","972","!=0","mat",5,"dspnsd_qty","979","in (4,1)","mat",5,"rx_itm_cnt","979","in (4,1)","mat",5,"dspnsd_qty","999","!=0","mat",5,"rx_itm_cnt","999","!=0","mat",5,"dspnsd_qty"],"description":"Fiscal Start Year"},{"name":"ICE_PD_COUNT","code":"ICE_PD_COUNT","dataType":"Number","values":["1"],"description":"Period count"},{"name":"ICE_PD_END_CURRENT","code":"ICE_PD_END_CURRENT","dataType":"Boolean","values":["true"],"description":"Period end current flag"},{"name":"ICE_PD_TYPE","code":"ICE_PD_TYPE","dataType":"String","values":["Monthly"],"description":"Period type"}],"templateCode":"API_Testing_Tiny_Template"}]},"url":"https://postman-echo.com/post"}
```