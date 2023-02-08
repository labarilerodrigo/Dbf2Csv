#!/usr/bin/python3.6
"""
lbdeclient

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

Example usage:


1. Run simple http request

-sh-4.2$ python3.6 lbdeclient -u "https://postman-echo.com/headers" -m get request
2021-03-18 23:31:42,030 [PID 128487] [DEBUG] - connectionpool - 813  Starting new HTTPS connection (1): postman-echo.com:443
2021-03-18 23:31:42,100 [PID 128487] [DEBUG] - connectionpool - 393  https://postman-echo.com:443 "GET /headers HTTP/1.1" 200 240
2021-03-18 23:31:42,101 [PID 128487] [INFO ] - lbdeclient - 428  {"headers":{"x-forwarded-proto":"https","x-forwarded-port":"443","host":"postman-echo.com","x-amzn-trace-id":"Root=1-60541b1e-60ea03d429143f8343ec30d1","user-agent":"python-requests/2.21.0","accept-encoding":"gzip, deflate","accept":"*/*"}}

2. Run simple http request with multiple header args

[br9dusr@cdts99hdbe07d alejandro]$ python3.6 lbdeclient -u "https://postman-echo.com/headers" -m get  -H 'Cache-Control: no-cache' -H 'Content-Type: application/json' request
2021-03-19 10:35:15,091 [PID 55676] [DEBUG] - connectionpool - 813  Starting new HTTPS connection (1): postman-echo.com:443
2021-03-19 10:35:15,139 [PID 55676] [DEBUG] - connectionpool - 393  https://postman-echo.com:443 "GET /headers HTTP/1.1" 200 301
2021-03-19 10:35:15,140 [PID 55676] [INFO ] - lbdeclient - 489  {"headers":{"x-forwarded-proto":"https","x-forwarded-port":"443","host":"postman-echo.com","x-amzn-trace-id":"Root=1-6054b6a3-798e41ba42f3928354775001","user-agent":"python-requests/2.21.0","accept-encoding":"gzip, deflate","accept":"*/*","cache-control":"no-cache","content-type":"application/json"}}


4. Run http request with data from file
[br9dusr@cdts99hdbe07d alejandro]$ python3.6 lbdeclient -u "https://postman-echo.com/post" -m post -H 'Cache-Control: no-cache' -H 'Content-Type: application/json' request -f template_body.json
2021-03-19 13:10:30,735 [PID 60875] [INFO ] - lbdeclient - 429  parsing file template_body.json
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

3. Run Advanced bde request, update request payload with query

python3.6 lbdeclient -u "https://postman-echo.com/post" -m post \
-H 'Cache-Control: no-cache' -H 'Content-Type: application/json' \
request -f template_body.json \
query -i usdhdpimpala.rxcorp.com:21050 -d devl_br9 \
-q "SELECT client_cd, chnl_fltr_lst_desc, pd_typ_fltr_cd, caatg_ntile_lvl_cd, tiling_meas_cd FROM devl_br9.vw_pbs_dm_doc_tiling_param_value_list" \
--update-request "{\"filter\":{\"name\":\"ICE\"}, \"key\":\"values\", \"field\":\"parameters\"}"


"""
from contextlib import closing
from impala.dbapi import connect
import argparse
import json
import logging
import pathlib
import logging.config
import sys
from types import SimpleNamespace
from typing import Any, Dict, Optional, Union
from typing import List, cast, Type
from typing import NamedTuple
from itertools import chain

import requests
from requests.auth import HTTPBasicAuth


class LatamHttpBasicLogin(NamedTuple):
    username: str
    password: str


class LatamHttpRequestsOptions:
    stream: bool = False
    verify: bool = True
    proxies: dict = {}
    cert: str = None
    timeout: int = None
    allow_redirects: bool = True


class LbdeClientLogger:
    def __init__(self):
        frmt = "%(asctime)s [PID %(process)5s] [%(levelname)-5.5s] - %(module)s - %(lineno)s  %(message)s"
        logging.basicConfig(level=logging.DEBUG, format=frmt, handlers=[logging.StreamHandler()])
        self.logger = logging.getLogger(self.__class__.__name__)
        self.level = logging.DEBUG
        self.format = logging.Formatter(frmt)


class AbstractLbdeClientLoadCommand:
    @classmethod
    def arguments(cls, sub_parser: argparse.ArgumentParser) -> None:
        pass

    def __init__(self) -> None:
        pass

    def execute(self, options: argparse.Namespace) -> None:
        pass


class LbdeClientCommand(AbstractLbdeClientLoadCommand):
    @classmethod
    def arguments(cls, bdeclient_parser: argparse.ArgumentParser) -> None:
        bdeclient_parser.add_argument("-f", "--file", dest="file", type=str, required=False,
                                      help='The template JSON file to use as a base for the payload', )
        subparsers = bdeclient_parser.add_subparsers()
        impala_parser = subparsers.add_parser("query")
        LbdeClientImpalaCommand.arguments(impala_parser)
        bdeclient_parser.set_defaults(command=cls)


class LbdeClientImpalaCommand(AbstractLbdeClientLoadCommand):
    @classmethod
    def arguments(cls, impala_parser: argparse.ArgumentParser) -> None:
        impala_parser.add_argument('-i', '--impalad', dest='impala_conn',
                                   help='<host:port> of impalad to connect to', type=str, required=True)

        impala_parser.add_argument('-d', '--database', dest='database',
                                   help='Impala Database', type=str, required=True
                                   )

        impala_parser.add_argument("-u", "--update-request", dest="params", type=str, required=False,
                                   help='Update template params key'
                                        'Example: {"filter":{"name:"ICE"}, "key":"values", "field":"parameters"}', )

        impala_parser.add_argument('-q', '--query', dest='sql',
                                   help='SQL Query', type=str, required=True
                                   )

        impala_parser.add_argument('-ssl', '--ssl', dest='ssl', default=True,
                                   help='Connect to Impala via SSL-secured connection', type=bool, required=False)

        impala_parser.add_argument('-auth', '--auth_mechanism', dest='auth', default='GSSAPI',
                                   help="{\'NOSASL\', \'PLAIN\', \'GSSAPI\', \'LDAP\'} Specify the authentication mechanism. \'NOSASL\' for unsecured Impala."
                                        "\'PLAIN\' for unsecured Hive (because Hive requires the SASL"
                                        "transport). \'GSSAPI\' for Kerberos and \'LDAP\' for Kerberos with"
                                        "LDAP.", type=str, required=False)
        impala_parser.set_defaults(command=cls)


class BaseLbdeClientLoadCommand(object):
    @property
    def base_parser(self) -> argparse.ArgumentParser:
        return self.base_parser

    @base_parser.getter
    def base_parser(self) -> argparse.ArgumentParser:
        sub_parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="LbdeClient")
        sub_parser.add_argument('-u',
                                '--url',
                                dest='base_url',
                                help='The host to submit the request',
                                type=str,
                                required=False)
        sub_parser.add_argument('-H',
                                '--header',
                                dest='header',
                                help='The HTTP headers to be added to the GET/POST request',
                                type=str,
                                required=False,
                                nargs=1,
                                action='append'
                                )
        sub_parser.add_argument('-m',
                                '--method',
                                dest='method',
                                default='POST',
                                help='The HTTP method to use',
                                type=str,
                                required=False)
        return sub_parser


class LbdeClientCLI():
    def __init__(self, *args, **kwargs):
        self.args = self.get_parser()

    def get_parser(self, argv: List[str] = sys.argv[1:]) -> argparse.Namespace:
        parser = BaseLbdeClientLoadCommand().base_parser
        subparsers = parser.add_subparsers()
        bdeclient_parser = subparsers.add_parser("request")
        LbdeClientCommand.arguments(bdeclient_parser)
        options = parser.parse_args(argv)
        if "command" not in options:
            parser.error("No command selected")
        return options


class LatamHttpClient(LbdeClientLogger):
    def __init__(self, url: str, method: str = 'POST', auth_type: Any = HTTPBasicAuth,
                 login: LatamHttpBasicLogin = None, headers: Optional[Dict[Any, Any]] = None,
                 data: Optional[Union[Dict[str, Any], str]] = None, request_options: LatamHttpRequestsOptions = None) -> None:
        super().__init__()
        self.method = method.upper()
        self.auth_type: Any = auth_type
        self.base_url = url
        self.login = login
        self.headers = headers
        self.data = data
        self.request_options = request_options if request_options else LatamHttpRequestsOptions()

    def get_http_session(self) -> requests.Session:
        session = requests.Session()
        if self.login:
            session.auth = self.auth_type(self.login.username, self.login.password)
        if self.headers:
            session.headers.update(self.headers)
        return session

    def run(self) -> Any:
        session = self.get_http_session()
        self.logger.debug(f"\n"
                          f"METHOD: \t {self.method}\n"
                          f"AUTH_TYPE: \t {self.auth_type}\n"
                          f"URL: \t {self.base_url}\n"
                          f"LOGIN: \t {self.login}\n"
                          f"HEADERS: \t {self.headers}\n"
                          f"DATA: \t {self.data}\n"
                          f"REQ-OPTS: \t {self.request_options}\n")
        if isinstance(self.data, dict):
            if self.method == 'GET':
                # GET uses params
                req = requests.Request(self.method, self.base_url, params=json.dumps(self.data), headers=self.headers)
            elif self.method == 'HEAD':
                # HEAD doesn't use params
                req = requests.Request(self.method, self.base_url, headers=self.headers)
            else:
                # Others use data
                req = requests.Request(self.method, self.base_url, data=json.dumps(self.data), headers=self.headers)
        else:
            if self.method == 'GET':
                # GET uses params
                req = requests.Request(self.method, self.base_url, params=self.data, headers=self.headers)
            elif self.method == 'HEAD':
                # HEAD doesn't use params
                req = requests.Request(self.method, self.base_url, headers=self.headers)
            else:
                # Others use data
                req = requests.Request(self.method, self.base_url, data=self.data, headers=self.headers)

        prepped_request = session.prepare_request(req)
        try:
            response = session.send(
                prepped_request,
                stream=self.request_options.stream,
                verify=self.request_options.verify,
                proxies=self.request_options.proxies,
                cert=self.request_options.cert,
                timeout=self.request_options.timeout,
                allow_redirects=self.request_options.allow_redirects,
            )

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print("HTTP error: %s", response.reason)
                prepped_request(response.text)
                raise Exception(str(response.status_code) + ":" + response.reason)

            return response

        except requests.exceptions.ConnectionError as e:
            raise e


class LatamBdeClientBody():
    def __init__(self, body):
        self.raw_body = body
        self.body = self.parse_json()

    def parse_json(self) -> SimpleNamespace:
        """
        Parse JSON into an object with attributes corresponding to dict keys.
        :return:
        """
        if isinstance(self.raw_body, str):
            return json.loads(self.raw_body, object_hook=lambda d: SimpleNamespace(**d))
        elif isinstance(self.raw_body, dict):
            body = json.dumps(self.raw_body)
            return json.loads(body, object_hook=lambda d: SimpleNamespace(**d))

    def get_attr(self, key, index=None, obj=None):
        obj = obj if obj else self.body
        if isinstance(getattr(obj, key), (list, tuple)):
            if index is not None:
                return getattr(obj, key)[index]
            else:
                return getattr(obj, key)
        else:
            return getattr(obj, key)

    def set_attr(self, key, value, obj=None):
        obj = obj if obj else self.body
        setattr(obj, key, value)

    def print_body(self):
        """
        Print self-mapped attrs as a dict
        :return:
        """
        print(self.to_dict())

    def update_requests_values(self, key, value, field="parameters", match=None):
        """
        Updates field level k,v in body template
        :param key:
        :param value:
        :param field:
        :param match:
        :return:
        """
        try:
            requests = self.get_attr("requests", index=0)
            params = self.get_attr(field, obj=requests)
            if match:
                k, v = match.split(":")
                results = list(filter(lambda params: getattr(params, k) == v, params))
                for result in results:
                    self.set_attr(key, value, result)
        except Exception as e:
            raise e

    def to_dict(self, obj=None) -> dict:
        """
        Recursively converts Nested NameSpace object to dict
        :param obj:
        :return:
        """
        obj = obj if obj else self.body
        if isinstance(obj, SimpleNamespace):
            obj = vars(obj)
            self.to_dict(obj)
        elif isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, SimpleNamespace):
                    obj[key] = vars(obj[key])
                elif isinstance(value, list):
                    for index in range(len(value)):
                        if isinstance(obj[key][index], SimpleNamespace):
                            obj[key][index] = vars(obj[key][index])
                            self.to_dict(obj[key][index])
        elif isinstance(obj, list):
            for index in range(len(obj)):
                if isinstance(obj[index], SimpleNamespace):
                    obj[index] = vars(obj[index])
                    self.to_dict(obj[index])
        return obj


class LatamImpalaClient(LbdeClientLogger):
    def __init__(self, host, database, port=21050, use_ssl=1, auth_mechanism="GSSAPI", *args, **kwargs):
        super().__init__()
        self.host = host
        self.database = database
        self.port = port
        self.use_ssl = use_ssl
        self.auth_mechanism = auth_mechanism

    def get_conn(self):
        """
        Returns HiveServer2 connection
        :return:
        """
        try:
            conn = connect(host=self.host, port=int(self.port), database=self.database, use_ssl=self.use_ssl,
                           auth_mechanism=self.auth_mechanism)
            return conn
        except Exception as e:
            self.logger.exception(e)

    def get_cursor(self):
        """
        Returns a cursor
        """
        try:
            return self.get_conn().cursor()
        except Exception as e:
            self.logger.exception(e)

    def get_records(self, sql, parameters=None):
        """
        Executes given sql statement, return records as a flattened list
        :param sql:
        :param parameters:
        :return:
        """
        try:
            with closing(self.get_conn()) as conn:
                with closing(conn.cursor()) as cur:
                    if parameters is not None:
                        cur.execute(sql, parameters)
                    else:
                        cur.execute(sql)
                    records = cur.fetchall()
                    return list(chain(*records))
        except Exception as e:
            self.logger.exception(e)


class LbdeClientApp(LbdeClientLogger):
    def __init__(self, cli: LbdeClientCLI):
        super().__init__()
        self.attrs = vars(cli.args)
        self.file: str = self.attrs.get("file", None)
        self.url: str = self.attrs.get("base_url", None)
        self.header_args: list = self.attrs.get("header", [])

        self.header: dict = {key.strip(): value.strip()
                             for key, value in (value.split(":") for value in list(chain(*self.header_args)))} \
            if self.header_args else {}

        self.method: str = self.attrs.get("method", "POST")
        self.params: dict = self.attrs.get("params", None)

        self.impala_conn: str = self.attrs.get("impala_conn", None)
        self.impala_database: str = self.attrs.get("database", None)
        self.impala_sql: str = self.attrs.get("sql", None)
        self.impala_usel_ssl: int = self.attrs.get("ssl", 1)
        self.auth: str = self.attrs.get("auth", "GSSAPI")
        self.impala: bool = True if self.impala_conn else False
        self.update_requests_values: dict = json.loads(self.attrs.get("params", "{ }"))

    def parse_file(self, file=None):
        try:
            file = file if file else self.file
            data = None
            if file:
                file = pathlib.Path(self.file)
                if file.exists():
                    self.logger.info(f"parsing file {file.name}")
                    with open(file.name, 'r+') as body_file:
                        data = json.load(body_file)
                else:
                    self.logger.exception(f"File {file} not exist")
            else:
                self.logger.exception("No file to parse")
            return data
        except Exception as e:
            self.logger.exception(e)

    def run_impala(self):
        if self.impala_conn and self.impala_database:
            host, port = self.impala_conn.split(":")
            impala = LatamImpalaClient(host=host,
                                       port=port,
                                       use_ssl=self.impala_usel_ssl,
                                       auth_mechanism=self.auth,
                                       database=self.impala_database)
            if self.impala_sql:
                records = impala.get_records(sql=self.impala_sql)
                self.logger.info(records)
                return records

    def request(self, data=None, request_options: LatamHttpRequestsOptions = None,
                http_login: LatamHttpBasicLogin = None):
        self.http_client: LatamHttpClient = LatamHttpClient(url=self.url,
                                                            method=self.method,
                                                            headers=self.header,
                                                            request_options=request_options,
                                                            login=http_login,
                                                            data=data)

    def update_body_template(self, body: LatamBdeClientBody, file=None):
        try:
            self.logger.info(body)
            raw_json = body.to_dict()
            self.logger.info(f"Raw JSON: {raw_json}")
            file = file if file else self.file
            data = None
            if file:
                file = pathlib.Path(self.file)
                if file.exists():
                    self.logger.info(f"parsing file {file.name}")
                    with open(file.name, 'w+') as body_file:
                        data = json.dump(raw_json, body_file)
                else:
                    self.logger.exception(f"File {file} not exist")
            else:
                self.logger.exception("No file to parse")
            return data
        except Exception as e:
            self.logger.exception(e)

    def run(self):
        try:
            self.data = None
            self.template_body = None
            if self.file:
                self.data = self.parse_file()
                self.template_body = LatamBdeClientBody(body=self.data)
            if self.impala:
                self.records = self.run_impala()
            if self.update_requests_values and self.records:
                self.logger.info(f"Updating body payload with values: {self.records}")
                name = self.update_requests_values.get("filter").get("name")
                key = self.update_requests_values.get("key")
                field = self.update_requests_values.get("field")
                self.template_body.update_requests_values(key=key, value=self.records,
                                                          field=field, match=f"name:{name}")
                self.logger.info(self.template_body.to_dict())
                self.update_body_template(self.template_body)
            if self.template_body:
                self.template_body.print_body()

            if self.method and self.url:
                if self.file:
                    http_client = LatamHttpClient(url=self.url, method=self.method,
                                                  headers=self.header, data=self.parse_file())
                else:
                    http_client = LatamHttpClient(url=self.url, method=self.method,
                                                  headers=self.header)
                response = http_client.run()
                self.logger.info(response.text)
        except Exception as e:
            self.logger.exception(e)


if __name__ == '__main__':
    try:
        cli = LbdeClientCLI()
        options = cli.get_parser(sys.argv[1:])
        command = cast(Type[AbstractLbdeClientLoadCommand], options.command)()
        LbdeClientApp(cli).run()

    except Exception as e:
        raise SystemExit(f"Application failed {e}, exiting...")
