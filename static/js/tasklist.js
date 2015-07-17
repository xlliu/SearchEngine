/**
 * Created by xlliu on 15-6-1.
 */


//解析时间
function showTime(num){
    if(num){
        var data = new Date(num)
        var yy = data.getUTCFullYear();
        var mm = data.getUTCMonth();
        var dd = data.getUTCDate();
        var hh = data.getUTCHours();
        var mmm = data.getUTCMinutes();
        var ss = data.getUTCSeconds();
        if(mm<10){
            mm = '0'+(data.getUTCMonth()+1);
        }
        if(dd<10){
            dd = '0'+(data.getUTCDate());
        }
        if(hh<10){
            hh = '0'+data.getUTCHours();
        }
        if(mmm<10){
            mmm = '0'+data.getUTCMinutes();
        }
        if(ss<10){
            ss = '0'+data.getUTCSeconds();
        }

        var result = yy+'-'+mm+'-'+dd+' '+hh+':'+mmm+':'+ss;
        return result;
    }
    return "——"
}


function statusSwitch(sta){
    if(sta == 0){
        return "排队中"
    }else if(sta ==1){
        return "处理中"
    }else if(sta ==2){
        return "完成"
    }else{
        return "错误"
    }
}


var logL= null;
function setLog(log_value){
    logL=log_value
}

var sorclog = "a";
var currentPageLog = 0;
var typeContentLog = null;
var num = 0;
var t = -1;
var t_1 = null;
var t_2 = null;
var typeContent = null;

function sortTask(typeContent,currentPage){
    if (t_2){
        clearTimeout(t_2)
    }
    if (t_1){
        clearTimeout(t_1)
    }
    $.ajax({
        url:'/tasklist',
        type:'post',
        data:{'typeContent':typeContent,'b':t = (num%2==0)?-1:1,'sc':sorclog,'currentPage':currentPage},
        dataType:'json',
        beforeSend:function(){
            setLog(typeContent)
        },
        success:function(data){
            var htm = "<tr>" +
                "<th onclick=\"showTaskList(\'name\')\"><label>任务名称</label></th>" +
                "<th onclick=\"showTaskList(\'status\')\"><label>任务状态</label></th>" +
                "<th onclick=\"showTaskList(\'current_progress\')\"><label>当前进度</label></th>" +
                "<th onclick=\"showTaskList(\'create_time\')\"><label>开始时间</label></th>" +
                "<th onclick=\"showTaskList(\'complete_time\')\"><label>完成时间</label></th>" +
                "<th><label>备注</label></th></tr>";
            for(var i=0;i<data.length;i++){
                htm += "<tr><td>";
                htm += data[i].name;
                htm += "</td><td>";
                htm += statusSwitch(data[i].status);
                htm += "</td><td>";
                htm += data[i].current_progress;
                htm += "</td><td>";
                htm += showTime(data[i].create_time?data[i].create_time.$date:null);
                htm += "</td><td>";
                htm += showTime(data[i].complete_time?data[i].complete_time.$date:null);
                htm += "</td><td>";
                htm += data[i].comment;
                htm += "</td>";
            }
            document.getElementById('tab').innerHTML = '';
            document.getElementById('tab').innerHTML = htm
        }
    });
    t_1 =setTimeout('showTaskList(logL,true,sorclog)',3000);
}

//自动刷新记录位置
function autoFlush(screen1,currentPage){
    if(screen1){
        if (t_2){
            clearTimeout(t_2)
        }
        if (t_1){
            clearTimeout(t_1)
        }
        $.ajax({
            url:'/tasklist',
            type:'post',
            data:{'sc':screen1,'currentPage':currentPage},
            dataType:'json',
            success:function(data){
                var htm = "<tr>" +
                    "<th onclick=\"showTaskList(\'name\')\"><label>任务名称</label>" +
                    "</th><th onclick=\"showTaskList(\'status\')\"><label>任务状态</label>" +
                    "</th><th onclick=\"showTaskList(\'current_progress\')\"><label>当前进度</label>" +
                    "</th><th onclick=\"showTaskList(\'create_time\')\"><label>开始时间</label>" +
                    "</th><th onclick=\"showTaskList(\'complete_time\')\"><label>完成时间</label>" +
                    "</th><th><label>备注</label></th></tr>";
                for(var i=0;i<data.length;i++){
                    htm += "<tr><td>";
                    htm += data[i].name;
                    htm += "</td><td>";
                    htm += statusSwitch(data[i].status);
                    htm += "</td><td>";
                    htm += data[i].current_progress;
                    htm += "</td><td>";
                    htm += showTime(data[i].create_time?data[i].create_time.$date:null);
                    htm += "</td><td>";
                    htm += showTime(data[i].complete_time?data[i].complete_time.$date:null);
                    htm += "</td><td>";
                    htm += data[i].comment;
                    htm += "</td>";
                }
                document.getElementById('tab').innerHTML = '';
                document.getElementById('tab').innerHTML = htm
            }
        });
    }else{
        $.ajax({
            url:'/tasklist',
            type:'post',
            data:{'currentPage':currentPage},
            dataType:'json',
            success:function(data){
                var htm = "<tr>" +
                    "<th onclick=\"showTaskList(\'name\')\"><label>任务名称</label>" +
                    "</th><th onclick=\"showTaskList(\'status\')\"><label>任务状态</label>" +
                    "</th><th onclick=\"showTaskList(\'current_progress\')\"><label>当前进度</label>" +
                    "</th><th onclick=\"showTaskList(\'create_time\')\"><label>开始时间</label>" +
                    "</th><th onclick=\"showTaskList(\'complete_time\')\"><label>完成时间</label>" +
                    "</th><th><label>备注</label></th></tr>";
                for(var i=0;i<data.length;i++){
                    htm += "<tr><td>";
                    htm += data[i].name;
                    htm += "</td><td>";
                    htm += statusSwitch(data[i].status);
                    htm += "</td><td>";
                    htm += data[i].current_progress;
                    htm += "</td><td>";
                    htm += showTime(data[i].create_time?data[i].create_time.$date:null);
                    htm += "</td><td>";
                    htm += showTime(data[i].complete_time?data[i].complete_time.$date:null);
                    htm += "</td><td>";
                    htm += data[i].comment;
                    htm += "</td>";
                }
                document.getElementById('tab').innerHTML = '';
                document.getElementById('tab').innerHTML = htm
            }
        });
    }
}

//分类层级30
function screen(sorc){
    zeropage();
    currentPageLog = $("#currentPage").val(0);
    if (sorc){
        sorclog = sorc;
    }
    if(sorc == "a"){
        $("#screen").val("a")
        showTaskList(null,null,sorc)

    }else if(sorc == "s"){
        $("#screen").val("s")
        showTaskList(null,null,sorc)
    }else if(sorc == "c"){
        $("#screen").val("c")
        showTaskList(null,null,sorc)
    }
    lastPageFlush(sorc)
}

function lastPageFlush(screen){
    $.ajax({
        url:"/totalpagenum",
        type:"post",
        data:{"sc":screen},
        dataType:"json",
        success:function(data){
            $("#totalCounts").val(data)
            if (data =='0'){

                $('#pagedown').hide()
                $('#pagelast').hide()
            }
        }
    })
}

// 排序层级10
// 排序自动刷新处理
// typeContent排序, judge:true  自动刷新,false  手动单击
// screen1 分类显示
function showTaskList(typeContent,judge,screen1,currentPage){
    currentPageLog = $("#currentPage").val();

    $("#curSortWay").val(typeContent);

    if (typeContent&&!judge){
        $("#currentPage").val(0);
        zeropage();
        currentPageLog = 0;
        num+=1;
        sortTask(typeContent,currentPageLog);
    }else if(typeContent&&judge){
        sortTask(typeContent,currentPageLog);
    }else if(screen1){
        autoFlush(screen1,currentPageLog);
        t_2 =setTimeout('showTaskList(null,null,sorclog)',3000);
    }else{
        autoFlush(null,currentPageLog);
        t_2 =setTimeout('showTaskList()',3000);
    }
}


//分页层级20
function pagetop(first){
    typeContent = $("#curSortWay").val();
    if(first==0){
        zeropage();
        $("#currentPage").val(0);
        currentPageLog = $("#currentPage").val();
        showTaskList(typeContent,true,sorclog,0);
    }else{
        if(currentPageLog == "1"){
            $("#pagetop").hide();
            $("#pagefirst").hide();
        }
        $("#pagedown").show();
        $("#pagelast").show();
        $("#currentPage").val(parseInt(currentPageLog)-1);
        currentPageLog = $("#currentPage").val();
        showTaskList(typeContent,true,sorclog,currentPageLog);
    }
}

function pagedown(last){

    typeContent = $("#curSortWay").val();

    if(last){
        $("#currentPage").val(last);
        currentPageLog = $("#currentPage").val();
        showTaskList(typeContent,true,sorclog,last);
        lastpage();
    }else{
        if(currentPageLog == $("#totalCounts").val()-1){
            $("#pagedown").hide();
            $("#pagelast").hide();
        }
        $("#pagetop").show();
        $("#pagefirst").show();

        $("#currentPage").val(parseInt(currentPageLog)+1);
        currentPageLog = $("#currentPage").val();
        showTaskList(typeContent,true,sorclog,currentPageLog);
    }

}


function zeropage(){
    $("#pagetop").hide();
    $("#pagefirst").hide();
    $("#pagedown").show();
    $("#pagelast").show();
}
function lastpage(){
    $("#pagedown").hide();
    $("#pagelast").hide();
    $("#pagetop").show();
    $("#pagefirst").show();
}

$(function(){
    showTaskList();
});
