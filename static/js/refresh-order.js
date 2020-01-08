console.log("refresh-order.js load");

django.jQuery(document).ready(function(){
    setInterval( periodicallyRequest , 9000);
});

var audio = new Audio('/static/sources/breakbeat_2.mp3');
function periodicallyRequest(  ){
    console.log("Start ajax request");
    
    django.jQuery.ajax({
        url: '/refresh-orders',
        success: function(result){
            console.log("success");
            console.log(result);
            if(result.thereOrders){
                audio.play();
            }
        }        
    });    
}