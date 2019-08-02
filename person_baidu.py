# -*- coding:utf-8 -*-
import base64
import urllib
import os
import json
import cv2
import time
import yaml
import ipdb
import glob
from key import getAccess_token
from comprehend import log
'''
人体检测和属性识别
'''
def personAnalyze(imgPath, access_token):
	request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
	f = open(imgPath, 'rb')
	img = base64.b64encode(f.read())
	params = {"image":img}
	params = urllib.parse.urlencode(params).encode(encoding='UTF8')
	# access_token = 'zheshiduoyude24.qqqw1fb4c0d856c07e573c9447aaadcc13ec5.2592000.1564566064.282335-16687297'
	# access_token = '24.fb4c0d856c07e573c9447aaadcc13ec5.2592000.1564566064.282335-16687297'
	request_url_merge = request_url + "?access_token=" + access_token
	request = urllib.request.Request(url=request_url_merge, data=params)
	request.add_header('Content-Type', 'application/x-www-form-urlencoded')
	response = urllib.request.urlopen(request)
	print (response)
	content = response.read().decode('utf-8')#by utf-8解码
	content = eval(content) # string transf into dict
	if "error_code" in content.keys():#在这里防止如果没有及时按照计划，今天更新一次acess_token 这里在更新让程序能继续跑下去
		if content["error_code"] == 110:
			log.e('access_token is invalid!!')
			access_token = getAccess_token()
			request_url_merge = request_url + "?access_token=" + access_token
			request = urllib.request.Request(url=request_url_merge, data=params)
			request.add_header('Content-Type', 'application/x-www-form-urlencoded')
			response = urllib.request.urlopen(request)
			content = response.read().decode('utf-8')#by utf-8解码
			content = eval(content) # string transf into dict
		else:
			log.i('baiduapi is failed')
	Persons = []
	for i in range(content["person_num"]):
		height = content["person_info"][i]["location"]["height"]
		width = content["person_info"][i]["location"]["width"]
		y1 = content["person_info"][i]["location"]["top"]
		x1 = content["person_info"][i]["location"]["left"]
		information = content["person_info"][i]["attributes"]
		global count
		count +=1
		print(count)
		# cropped img by person bounding box
		img = cv2.imread(imgPath)
		cropped = img[y1:y1+height, x1:x1+width]  # 裁剪坐标为[y0:y1, x0:x1]
		imageName = str(count) + '.jpg'
		cv2.imwrite(("./results/" + imageName), cropped)
		Aperson = {"imageName":imageName, "attributes":information}
		print(Aperson)

		result = json.dumps(Aperson, ensure_ascii=False, indent=4)

		with open(os.path.join('./results', str(count)+'.json'), 'w') as json_file:
			json_file.write(result)
		# return {personInfo, imageNameList}

if __name__ =="__main__":
	with open('./config.yml', 'r') as f:
		config = yaml.load(f)
	log.enableFileLog(config['log_path'])
	log.setLevel("t")
	allImagesPath = sorted(glob.glob('./images/*.jpg'))
	access_token = '24.fb4c0d856c07e573c9447aaadcc13ec5.2592000.1564566064.282335-16687297'
	count = 0
	for imagePath in allImagesPath:
		personAnalyze(imagePath, access_token)