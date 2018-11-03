import requests
from bs4 import BeautifulSoup

# def get_coki():#获取cookie数据
# pass
# # url = 'http://bx.houqinbao.com/wechat/studentManage?universityId=gh_d65169064330&openid=21321232'
# url = 'http://bx.houqinbao.com/wechat/studentManage?universityId=gh_ec0a68e01670&openid=98f7s9fs3246'
# bd_session = requests.Session()
# what = bd_session.get(url)
# # response = requests.get(url)
# cookii = requests.utils.dict_from_cookiejar(what.cookies)
# return cookii


# url = 'http://bx.houqinbao.com/wechat/studentManage?universityId=gh_ec0a68e01670&openid=ozqQ153zsEByV5cN3G44VqBJpvhss'
# response = requests.get(url,headers=get_coki())
# soup = BeautifulSoup(response.text,'lxml')
# dic = soup.select('#listArea , div:nth-of-type(5)')
# # for i in dic:
# # data = {
# # 'dic':list(i.stripped_strings)
# # }
# # print(data)
# print(dic)
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

g_object_name = '';
key = '';
var global_file = "";
function random_string(len) {
	len = len||32;
	var chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
	var maxPos = chars.length;
	var pwd = '';
	for (i = 0; i < len; i++) {
		pwd += chars.charAt(Math.floor(Math.random() * maxPos));
	}
    return pwd;
}

function get_suffix(filename) {
    pos = filename.lastIndexOf('.')
    suffix = ''
    if (pos != -1) {
        suffix = filename.substring(pos)
    }
    return suffix;
}

function calculate_object_name(filename)
{
    suffix = get_suffix(filename);
    g_object_name = key + random_string(32) + suffix;
    return '';
}

//上传照片
function load(){

	
			$('.weui-gallery__del').on('click',function(){
	            if(null==previewImgIndex) return;
	            $('#uploaderFiles li').eq(previewImgIndex).unbind( "click" );
	            $('#uploaderFiles li').eq(previewImgIndex).remove();
	            previewImgIndex = null;
				$('.repair-input-uploader').show();
		    })
		    $uploaderFiles.on("click", "li", function(){
		        if(null!==previewImgIndex) return;
		        previewImgIndex = $('#uploaderFiles li').index($(this));
		        $galleryImg.attr("style", this.getAttribute("style"));
		        $gallery.css('display','block').css('opacity','1');
		//            $gallery.fadeIn(100);
		    });
		    $gallery.on("click", function(){
		        previewImgIndex = null;
		        $gallery.css('display','none').css('opacity','0');
		    });
	    });
	});
}

function upload(file,$preview,base64){
	lrz(file, {width: 1024}).then(function (rst) {
		//alert("新上传中..."+rst.origin.name);
		var filename = file.name;
		var ossData = new FormData();
		// 先请求授权，然后回调
		calculate_object_name(rst.origin.name)
		//调用服务器进行上传
		try {
		 $.ajax({
			 url: global.url+'/aliyuntest/updateImg',
			 data:{'image':rst.base64,'name':g_object_name},
			 dataType:'json',
		     type: 'POST',
		     async:false,
		     success:function(data){
		    	 //alert(data.code);
		    	 if (data.code == "100000") {
		    		$preview.attr('data-value',data.data);
					$preview.find('.weui_uploader_status_content').text('100%');
	                $preview.removeClass('weui_uploader_status').find('.weui_uploader_status_content').remove();
		    	 }
		     },
		     error:function(data){
		     	$preview.remove();
		        alert("上传失败请重试");
		     }
		 });
		}catch(err){
			alert("发生异常："+err.name+"==>"+err.message);
		}
	}).
}
