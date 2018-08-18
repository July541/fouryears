//一般直接写在一个js文件中
layui.use(['layer','jquery', 'form','laydate'], function(){
  var layer = layui.layer
  ,form = layui.form
  ,$ = layui.jquery,
  laydate = layui.laydate;
  console.log(editor)
  $("#send").bind("click",function(){
  	if(editor.txt.text() == ""){
  		layer.msg("不能发送内容为空的信件");
  	}else{
  		layer.open({
  			title:"填写信息",
  			type:2,
  			area: ['500px', '250px'],
  			content:"./sendMail.html"
  		});
  	}
  })

  function postMail(content) {
  	$.ajax({
  		url:"url",
  		type:POST,
  		data:{
  			// mailContent:
  			// mailAddress:
  			// sendTime:
  		},
  		success:function(data,stauts,jqXHR){
  			layer.msg("信件已在发送队列中");
  		},
  		error:function(xhr,textStatus){
			layer.msg("请重试");
    	}
  	})
  }


});