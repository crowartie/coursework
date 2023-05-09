
const mediaQuery = window.matchMedia('(max-width: 1080px)')



function view(e){
if (e.matches) {
    $('.window .left-menu').css('display','none');
    $('.window .container').css('margin-left','0');
    $('.window .container-burger-menu').css('display','block');
    $('.window .left-menu .left-menu-inner .menu-header .container-burger-menu').addClass('open-menu');
    $('.window .left-menu .left-menu-inner .menu-header .open-menu').css('right','0');
    $('.window .container .container-header .container-burger-menu').addClass('close-menu');
    $('.window .container .container-header .close-menu').css('left',0);
  }
  else{
    $('.window .left-menu').css('display','block');
    $('.window .container').css('margin-left','250px');
    $('.container-burger-menu').css('display','none');
            $('.window .left-menu').css('z-index','2');
    if($('.window .shadow-menu').css('display')=='block'){
        $('.window .shadow-menu').css('display','none');
    }
  }
}

mediaQuery.addListener(view)
view(mediaQuery)