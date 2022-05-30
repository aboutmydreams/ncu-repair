import requests,base64,random
# see here http://bx.houqinbao.com/wechat/studentManage?universityId=gh_ec0a68e01670&openid=ozqQ153zsEByV5cN3G44VqBJpvhss
# 不同的openid进入即可（可以看成是不同的用户）


repair_site = {
	'b1':'d0eded70a0c4be215bd46bbb1d940d6d',#前湖北院学生公寓
	'y1':'b4a0cc38077d9cd70625880b11095302',#医学院学生公寓
	'b2':'847ea021440945dd9a5145001fbaf692',#前湖北院其他楼栋
	'y2':'8e555fa2e76eb227a1609632925259e7'#医学院其他楼栋
}

b1_site = {
	1:'2291',
	2:'2292',
	3:'2293',
	4:'2294',
	5:'2295',
	7:'2296',
	8:'2297',
	9:'2298',
	10:'2299',
	11:'2300',
	12:'2301',
	13:'2302',
	14:'2303',
	15:'2304',
	16:'2305',
	17:'2306',
	18:'2307',
	19:'2308',
	20:'2309',
	21:'2310',
	22:'2311',
	23:'2312',
	24:'2313',
	25:'2314',
	26:'2315',
	27:'2316',
	28:'2317',
	29:'2318',
	30:'2319'

}

y1_site = {
	3:"2320",
	4:"2321",
	6:"2322",
	7:"2323",
	8:"2324",
	9:"2325",
	10:"2326",
	11:"2327",

}

b2_site ={
	'综合楼':"2342",
	'校医院':"2355",
	'网络中心':"2356",
	'室内体育馆':"2357",
	'室外体育馆':"2358",
	'建工楼':"2359",
	'汽车电子楼':"2360",
	'空间大楼':"2361",
	'艺术楼A区':"2362",
	'艺术楼B区':"2363",
	'外经楼A区':"2364",
	'文法楼B区':"2354",
	'文法楼A区':"2353",
	'图书馆':"2343",
	'研究生院':"2344",
	'环材楼A区':"2345",
	'环材楼B区':"2346",
	'信工楼A区':"2347",
	'信工楼B区':"2348",
	'信工楼C区':"2349",
	'机电楼D区':"2350",
	'信工楼E区':"2351",
	'音乐厅':"2352",
	'外经楼B区':"2365",
	'基础实验大楼A1区':"2366",
	'理生楼E区':"2387",
	'理生楼F区':"2533",
	'游泳馆':"2600",
	'昌海楼':"2601",
	'环境楼C区':"2844",
	'安保楼':"7619",
	'水电楼':"7620",
	'理生楼D区':"2386",
	'理生楼C区':"2385",
	'基础实验大楼A2区':"2367",
	'基础实验大楼B1区':"2368",
	'基础实验大楼B2区':"2369",
	'基础实验大楼C区':"2378",
	'基础实验大楼D1区':"2379",
	'基础实验大楼D2区':"2380",
	'基础实验大楼D3区':"2381",
	'基础实验大楼D4区':"2382",
	'理生楼A区':"2383",
	'理生楼B区':"2384",
}

y2_site = {
	'5栋青年教师公寓':"2330",
	'单身公寓':"2331",
	'第一实验大楼':"2332",
	'第二实验大楼':"2333",
	'第三实验大楼':"2334",
	'第四实验大楼':"2335",
	'第五实验大楼':"2336",
	'第六实验大楼':"2337",
	'第一教学楼':"2338",
	'第二教学楼':"2339",
}

repair_cd1 = {
	'public':"11499",#公共过道设施
	'outside':"11512",#室外设施
	'others':"16390",#其他（非后勤服务集团服务范围）
	'pubwc': "5257" ,#公共卫生间设施
	'shower':"5256" ,#淋浴设施（含公共电热开水器）
	'inside': "5255"#室内设施（寝室、教室、办公室等）

}

public_data = {
	'门':"11511",
	'电铃':"11510",
	'地面瓷砖':"11509",
	'日光灯':"11500",
	'吸顶灯':"11501",
	'楼梯灯':"11502",
	'开关':"11503",
	'窗户玻璃':"11504",
	'窗扣':"11505",
	'消防栓玻璃':"11506",
	'天花板':"11507",
	'墙面瓷砖':"11508",
	'地脚':"6f7bd8280899d39968048f83eae8bc5c",
	'护栏':"8355c005e13d14aedf449085207bb309",

}

outside_data = {
	'窨井盖':"11513",
	'下水道':"11514",
	'水管':"11515",
	'地砖':"11516",
	'外围路面':"11517",
	'护栏':"11518",

}

others_data = {
	'门锁':"16391",
	'网络':"16392",
	'空调':"16393",
	'洗衣机':"16394",
	'智能售电机':"16395",
	'电梯':"16396",
	'饮水机':"16397",
	'门禁':"16398",
	'吹风机':"16399",
	'微波炉':"16400",
	'中央空调':"16401",

}

pubwc_data = {
	'拖把池':"5293",
	'水管':"5307",
	'窗户玻璃':"5309",
	'窗扣':"5310",
	'天花板':"5311",
	'地面瓷砖':"5428",
	'开关':"5306",
	'照明灯':"5305",
	'下水管':"5304",
	'脚踏阀':"5296",
	'卫生间门':"5297",
	'小便池':"5298",
	'大便池':"5299",
	'蹲位门':"5300",
	'蹲位门栓':"5301",
	'地漏':"5302",
	'洗手池':"5303",
	'墙面瓷砖':"5429",
	'冲水阀（延时阀）':"2089ddc92240b07702f365bb864c9901",
	'水龙头':"c7afb74bc9fa98bc4265faae01455bdc",
	'地脚线':"1ee3f8e31703ef4c987288f9317bb6b4",
}

shower_data = {
	'淋浴管':"5283",
	'淋浴喷头':"5284",
	'淋浴支架':"5285",
	'淋浴帘':"5286",
	'冷水阀':"5287",
	'热水阀':"5288",
	'刷卡机':"5289",
	'电热开水器（楼栋公用）':"5290",


}

inside_data = {
	'总阀':"5268",
	'门':"5281",
	'天花板':"5282",
	'风扇调速器':"5280",
	'窗扣':"5279",
	'窗户玻璃':"5278",
	'床':"5269",
	'衣柜':"5270",
	'桌椅':"5271",
	'上床踏板':"5272",
	'键盘抽屉':"5273",
	'阳台晾衣杆':"5274",
	'衣柜晾衣杆':"5275",
	'纱窗':"5276",
	'窗帘':"5277",
	'厕所冲水阀（医学院）':"5292",
	'黑板':"5324",
	'IC卡表':"5325",
	'毛巾架':"5326",
	'翻盖落水头':"5427",
	'洗漱池':"5295",
	'日光灯':"5259",
	'阳台吸顶灯':"5260",
	'室内卫生间灯':"5261",
	'开关':"5262",
	'电风扇':"5263",
	'水龙头':"5264",
	'插座':"5265",
	'下水软管':"5266",
	'地漏':"5267",
	'地面瓷砖':"3cdf751ab4e9335de7df7fe50063fa2e",
	'墙面瓷砖':"f64ff3ecaed1eb9ddb4fc5814b8918a2",
	'地脚线':"be9953102bfcbbecdc6f06c9715a626e",

}








#获取cookie数据
def get_coki(openid=None):
	# url = 'http://bx.houqinbao.com/wechat/studentManage?universityId=gh_d65169064330&openid=21321232'
	url = f'http://bx.houqinbao.com/wechat/studentManage?universityId=gh_ec0a68e01670&openid={openid}'
	bd_session = requests.Session()
	what = bd_session.get(url)
	return requests.utils.dict_from_cookiejar(what.cookies)
header = get_coki()
#上传图片
def post_img(base64code):
	header = get_coki()
	url = 'http://bx.houqinbao.com/aliyuntest/updateImg'
	imgdata = {'image': f'data:image/jpeg;base64,{str(base64code)[2:-1]}'}
	strlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'r', 's', 't', 'w', 'x', 'y', 'z', '2', '3', '4', '5', '6', '7', '8']
	random_name = random.sample(strlist,32)
	name = ''.join(random_name)+'.png'
	imgdata['name'] = name
	response = requests.post(url,data=imgdata)
	# print(imgdata)
	if '成功' in response.text:
		return response.text
	elif '上传失败' in response.text:
		return 2#'文件过大或类型有误，上传失败'
	else:
		return 3#'网络异常，稍后再试'

#报修 成功 返回1 ,失败 返回2
def post_repair(openid,area1,area2,area3,pj1,pj2,detail,myname,myphone,base64code):#报修
	set_img = (post_img(base64code))
	img_re_dic = eval(set_img)
	picURL = img_re_dic['data']
	data = {
	    'openid': f'{openid}',
	    'subOpenid': '',
	    'universityId': 'gh_ec0a68e01670',
	    'repairArea': f'{area1},{area2}',
	    'repairAddress': f'{area3}',
	    'repairProject': f'{pj1},{pj2}',
	    'repairContent': f'{detail}',
	    'appointmentTime': '',
	    'repairMan': f'{myname}',
	    'repairManPhone': f'{myphone}',
	    'picURL': picURL,
	}
	url = 'http://bx.houqinbao.com/bxForm/addBx'
	header = get_coki(openid)
	response = requests.post(url,headers=header,data=data)
	if '"msg":"成功"' in response.text:
		print(response.text)
		return 1

#获取报修状况
def see_data(openid):
	url = 'http://bx.houqinbao.com/bxUser/wxRepairList'
	header1 = get_coki()
	data = {
	    'openid': f'{openid}',
	    'universityId': 'gh_ec0a68e01670',
	    'currentPage': '1',
	    'pageSize': '10',
	}
	what = requests.post(url,headers=header1,data=data)
	lists = eval(what.text)
	id_list = []
	tittle_list = []
	content_list = []
	for i in range(len(lists['data']['list'])):
		id_list.append(str(lists['data']['list'][i]['id']))
		address = str(lists['data']['list'][i]['repairAddress'])
		project = str(lists['data']['list'][i]['repairProjectName'])
		content = str(lists['data']['list'][i]['repairContent'])
		tittle = address[address.index('-')+1:].replace('-','·')+'·'+project[project.index('-')+1:].replace('-','·')
		if len(tittle)>13:
			tittle = address[address.index('-')+1:][address.index('-')+1:]+'·'+project[project.index('-')+1:].replace('-','·')
		tittle_list.append(tittle)
		if len(content)>27:
			content = f'{content[:26]}…'
		content_list.append(content)
	#print(all_list)
	return [id_list, tittle_list, content_list]

#取消报修
def cancel(openid,repairid):
	url1 = 'http://bx.houqinbao.com/bxUser/updateToCancel'
	url2 = 'http://bx.houqinbao.com/bxFormStatus/wxFind'

	data1 = {
	    'universityId': 'gh_ec0a68e01670',
	    'openid': f'{openid}',
	    'id': f'{repairid}',
	}
	data2 = {
	    'universityId': 'gh_ec0a68e01670',
	    'repairId': f'{repairid}',
	    'openid': f'{openid}',
	}
	res1 = requests.post(url1,headers=header,data=data1)
	res2 = requests.post(url2,headers=header,data=data2)
	print(res1.text)#{"code":100000,"msg":"成功"}就算撤回成功了
	print(res2.text)


#test
file=open('1.png','rb')
image= file.read()
file.close()
imgcode = base64.b64encode(image)

post_repair('ozqQ153zsEByV5cN3G44VqBJpvhss','20ac8882e667dbb22b5eaa24d6d3d040','11084','999','16441','16442','testdetial','我我','11156549888',imgcode)
idd = see_data('ozqQ153zsEByV5cN3G44VqBJpvhss')[0][0] #最近的一个工单
cancel('ozqQ153zsEByV5cN3G44VqBJpvhss',idd)#取消最近一个工单


# 好叭 确切的说应该是这里看 http://bx.houqinbao.com/wechat/studentManage?universityId=gh_ec0a68e01670&openid=ozqQ153zsEByV5cN3G44VqBJpvhss

'''
前端提交的表单
{'repairTime': '2018-07-26 20:13:30',
 'repairAddress': '前湖南院其他楼栋（医）-第一实验大楼-1111', 
 'repairMan': '1111',
  'id': '5c90fc4ddb20a7ab648c42789100ee34', 
 'repairContent': '1111', 
'repairProjectName': '公共过道设施-门', 
'repairStateName': '已取消',
 'hasEval': 0, 
 'repairCode': 'Bx5514201807261488'}


openid:ozqQ153zsEByV5cN3G44VqBJpvhss
subOpenid:
universityId:gh_ec0a68e01670
repairArea:847ea021440945dd9a5145001fbaf692,2342
repairAddress:1111
repairProject:11499,11511
repairContent:1111
appointmentTime:201800-01-01T00:00
repairMan:1111
repairManPhone:1111
picURL:newbaoxiu/XCa2KyJ2dczkwBEpneEekapijzxJrRcQ.png
'''