import urllib, sys
import urllib.request
import ssl
import ipdb

# client_id 为官网获取的AK， client_secret 为官网获取的SK

def getAccess_token():
	host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=8ay8dSQQVDtVavznhUqFHGt3&client_secret=YGMLxOAlitnXVS5TTo72RyOXbfVByTdg'
	request = urllib.request.Request(host)
	request.add_header('Content-Type', 'application/json; charset=UTF-8')
	response = urllib.request.urlopen(request)
	content = response.read()
	
	keyDict = eval(content)
	access_token = keyDict['access_token']
	return access_token

if __name__ == '__main__':
	print(getAccess_token())