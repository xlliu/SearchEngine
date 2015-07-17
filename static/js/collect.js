/**
 * Created by xlliu on 15-5-29.
 */

function goCollect(tdid,collectType,titleName,n){
    $.ajax({
        url:'/collect',
        type:'post',
        data:{'tdId':tdid,'collectType':collectType,'titleName':titleName,'ty':n},
        dataType:'json',
        success:function(data){
            alert('任务已发送，等待处理中……')
        }
    })
}