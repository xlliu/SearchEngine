/**
 * Created by xlliu on 15-5-21.
 */

function pageUp(){
    var screen = document.getElementById('screenHidden').value
    var taskId = document.getElementById('taskIdHidden').value
    num = parseInt(document.getElementById('currentPageHidden').value)
    if(num ==1){
        $('#zero').hide();
        $('#pageUp').hide();
        num-=1
        pageRun(taskId,num,screen);
        $('#currentPageHidden').val(num);
        document.getElementById('showCurrentPage').innerText=num+1;
        $('#last').show();
        $('#pageDown').show();
    }
    else{
        num-=1
        pageRun(taskId,num,screen);
        $('#currentPageHidden').val(num);
        document.getElementById('showCurrentPage').innerText=num+1;
        $('#last').show();
        $('#pageDown').show();
    }
}

function pageDown(){
    var screen = document.getElementById('screenHidden').value
    var taskId = document.getElementById('taskIdHidden').value
    var totalPage = parseInt(document.getElementById('totalPage').innerText)
    var num = parseInt(document.getElementById('currentPageHidden').value)
    if(num ==totalPage-2){
        $('#last').hide();
        $('#pageDown').hide();
        num+=1
        pageRun(taskId,num,screen)
        $('#currentPageHidden').val(num);
        document.getElementById('showCurrentPage').innerHTML=num+1;
        $('#zero').show()
        $('#pageUp').show()
    }
    else{
        num+=1
        pageRun(taskId,num,screen)
        $('#currentPageHidden').val(num);
        document.getElementById('showCurrentPage').innerHTML=num+1;
        $('#zero').show()
        $('#pageUp').show()
    }
}

function first(){
    var screen = document.getElementById('screenHidden').value
    var taskId = document.getElementById('taskIdHidden').value
    pageRun(taskId,0,screen)
    $('#currentPageHidden').val(0);
    if(document.getElementById('showCurrentPage')){
        document.getElementById('showCurrentPage').innerHTML=1;
        $('#zero').hide();
        $('#pageUp').hide();
        $('#last').show();
        $('#pageDown').show();
    }else{
        $('#last').hide();
        $('#pageDown').hide();
    }
}

function last(){
    var screen = document.getElementById('screenHidden').value
    var taskId = document.getElementById('taskIdHidden').value
    var totalPage = parseInt(document.getElementById('totalPage').innerText)
    pageRun(taskId,totalPage-1,screen)
    $('#currentPageHidden').val(totalPage-1);
    document.getElementById('showCurrentPage').innerHTML=totalPage;
    $('#zero').show()
    $('#pageUp').show()
    $('#last').hide();
    $('#pageDown').hide();
}


function pageRun(taskId,num,screen){
    $.ajax({
        url:'/pageHandler',
        type:'post',
        data:{'taskId':taskId,'currentPage':num, 'screen':screen},
        dataType:'json',
        success: function(data){
            var result = data;
            var conHtml = "";
            if(result != ""){
                for (var n=0;n<result.length;n++){
                    conHtml += "<div class=\"con\"";
                    n%2==0?conHtml += "style=\"background: #f9f9f9;\">":conHtml += "style=\"background: #cbf5ff;\">";
                    if (result[n].head_url.length == 1) {
                        conHtml += "<div><img src=\""+result[n].head_url[0]+"\" class=\"img_1\"></div>";
                    }else{
                        conHtml += "<div class=\"img_1\">" +
                            "<div><img src=\""+result[n].head_url[0]+"\" class=\"img_1_1\"></div>" +
                            "<div><img src=\""+result[n].head_url[1]+"\" class=\"img_1_2\"></div>" +
                            "<div><img src=\""+result[n].head_url[2]+"\" class=\"img_1_3\"></div>" +
                            "<div><img src=\""+result[n].head_url[3]+"\" class=\"img_1_4\"></div>" +
                            "</div>";
                    }

                    conHtml += "<div class=\"con_1\"><div><span><a  class=\"title_1\" href=\""+result[n].visit_url+"\">"+result[n].title+"</a></span>" +
                        "<span class=\"type_1\">"+result[n].type+"</span></div>" +
                        "<div class=\"con_2\" >";

                    for (var i=0;i<result[n].description.length;i++){
                        conHtml += result[n].description[i];
                    }

                    conHtml += "</div><div class=\"visit_1\"><a class=\"visit_a\" href=\""+result[n].visit_url+"\">"+result[n].visit_url+"</a></div></div>" +
                        "<div class=\"btu_1\"><a class=\"btn_1_1\" href=\"#2\" onclick=\"goCollect(\'"+result[n].fbid+"\',100004,\'"+result[n].title+"\',1)\">API采集</a>" +
                        "<a class=\"btn_1_2\" href=\"#2\" onclick=\"goCollect(\'"+result[n].fbid+"\',100003,\'"+result[n].title+"\',0)\">网页采集</a></div></div>";
                }
            }else{
                conHtml +="<div style=\"height:200px\"></div><div style=\"width:500px;text-align:center\">对不起！没有您需要的数据</div>"
            }
            $(".con").remove()
            document.getElementById('for_con').innerHTML=conHtml
        }
    })
}
$(function(){
    setTimeout(first,10)
})
