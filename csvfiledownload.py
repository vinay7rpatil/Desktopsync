import requests
import wget
import ssl, os

ssl._create_default_https_context = ssl._create_unverified_context

sat_url = "https://collrhnsatp01.jcpenney.com/pub/reports/jcp_sat6_ops_team_errata_report.csv"

myfile= requests.get(sat_url)

open ("C:\\python projects\\OSfiledetail\\sat.csv" , 'wb').write(myfile.content)








