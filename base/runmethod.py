import requests
import json

class RunMethod():


    #POST请求
	def post_main(self,url,data,header= None):
		response = requests.post(url=url,data=data.encode("utf-8"),headers=header).json()
		return response

    #GET请求
	def get_main(self,url,data=None,header= None):
		response = requests.get(url=url,data=data,headers=header,verify=False).json()
		return response

	def run_main(self,method,url,data=None,header=None):
		response = None
		if method == 'POST':
			response = self.post_main(url,data,header)
		else:
			response = self.get_main(url,data,header)
		return json.dumps(response,ensure_ascii=False)

if __name__ == '__main__':
	url = 'http://fts2-uata.crfchina.com/lendservice/lend'
	headers = {'Content-Type': 'application/json'}
	data1 = {
        "requestRefNo":"CRF011037541702199943998",
        "applyDate":"2018-09-06 11:23:18",
        "systemNo":"rcs",
        "crfUid":"1d0161fdbea86f451f76522bf2982e6b",
        "loanAmount":30000,
        "ledgerAmount":10000,
        "realLoanAmount":0,
        "loanedTimes":17,
        "loanProductNo":"P9999999",
        "loanerRiskLevel":'null',
        "loanType":"installment",
        "loanDays":92,
        "loanTerm":3,
        "lendStartDate":"2018-09-06 11:23:10",
        "lendEndDate":"2018-10-06 00:00:00",
        "notifyUrl":"http://rcs.crfchina.com/rcs-agent/crfRcs/p_notify",
        "loanContractNo":"CRF011037541702199943998",
        "loanerSource":"rcs",
        "remark":'null',
        "loanPurpose":"生活开销",
        "loanDayRate":"0.000410960000",
        "loanYearRate":"0.15000040",
        "industry":'null',
        "income":'null',
        "isOverDue":'null',
        "riskScore":'null',
        "merchantNo":"",
        "loanFundsSourceType":"p2p",
        "signAddresponses":'null',
      "loanNotarization":True
    }

	run = RunMethod()
	data = json.dumps(data1)
	print(run.run_main('POST',url,data,headers))
