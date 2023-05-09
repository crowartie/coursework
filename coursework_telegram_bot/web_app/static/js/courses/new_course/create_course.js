function create_course(){
    $('.window .container .container-content .box-content').append(`
        <div class="item-in-box-content">
            <input type="text" id="input-create-course">
        </div>`
    );
    $('#input-create-course').focus();
    $('#input-create-course').on('blur keyup',function(e){
        if(e.type=="blur" || e.which == 13){
            $('#input-create-course').val($.trim($('#input-create-course').val()));
            if($('#input-create-course').val().length<1){
                $('#input-create-course').parent().remove();
                var text="Название нового курса явялется пустым.";
                show_toast("Прерывание",text);
                return;
            }
            if($('.window .container .container-content .box-content .item-in-box-content').children('span').length>0){
                var identicalAnswerOption=0;
                $('.window .container .container-content .box-content .item-in-box-content').children('span').each(function(){
                    if($('#input-create-course').val()==$(this).text()){
                        identicalAnswerOption=1;
                        return;
                    }
                });
                if(identicalAnswerOption==1){
                    $('#input-create-course').parent().remove();
                    var text="Название нового вопроса совпадает с другим вопросом в данном тесте.";
                    show_toast("Прерывание",text);
                    return;
                }
            }
            show_modal_window_for_new_course();
        }
        else if(e.which==27){
            $(this).parent().remove();
            return
        }

        });

}