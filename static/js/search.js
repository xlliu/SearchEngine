function goSearch(){
    var content =document.getElementById('content').value;
    if (''!=content.replace(/(^\s*)|(\s*$)/g,'')){
        $('#search_engine').submit();
        popDiv();
    }
}

function EnterPress(even){
    var e = even || window.event;
    if(e.keyCode == 13){
        var content =document.getElementById('content').value;
        if (''!=content.replace(/(^\s*)|(\s*$)/g,'')){
            $('#search_engine').submit();
            popDiv();
        }
    }
}

function popDiv(){
    $("#mask").show(1000)
    $(".spinner").show(2000)
}

