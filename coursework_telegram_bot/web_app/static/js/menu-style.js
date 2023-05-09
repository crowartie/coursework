$('.container-burger-menu').click( function() {
    if ($('.window .left-menu').css('display') == 'none'){
        $('.window .shadow-menu').css('display','block');
        $('.window .left-menu').css('display','block');
        $('.window .left-menu').css('z-index','3');
    }
    else{
        $('.window .shadow-menu').css('display','none');
        $('.window .left-menu').css('display','none');
    }
});

$('.window .shadow-menu').on('click',function(e) {
    if($('.window .shadow-menu').css('display')=='block' && $('.left-menu').css('display') == 'block'){
        if (!$(e.target).is('.left-menu *') && !$(e.target).is('.container-burger-menu')){
            $('.window .shadow-menu').css('display','none');
            $('.window .left-menu').css('display','none');
        }
    }
    });






