function create_question(){
    $('.window .container .container-content .box-content').append(`
        <div class="item-in-box-content">
            <input type="text" id="input-create-question">
        </div>`
    );
    $('#input-create-question').focus();
    $('#input-create-question').on('blur keyup',function(e){
        if(e.type=="blur" || e.which == 13){
            $('#input-create-question').val($.trim($('#input-create-question').val()));
            if($('#input-create-question').val().length<1){
                $('#input-create-question').parent().remove();
                var text="Название нового вопроса явялется пустым.";
                show_toast("Прерывание",text);
                return;
            }
            if($('.window .container .container-content .box-content .item-in-box-content').children('span').length>0){
                var identicalAnswerOption=0;
                $('.window .container .container-content .box-content .item-in-box-content').children('span').each(function(){
                    if($('#input-create-question').val()==$(this).text()){
                        identicalAnswerOption=1;
                        return;
                    }
                });
                if(identicalAnswerOption==1){
                    $('#input-create-question').parent().remove();
                    var text="Название нового вопроса совпадает с другим вопросом в данном тесте.";
                    show_toast("Прерывание",text);
                    return;
                }
            }
            show_modal_window_for_new_question();
        }
        else if(e.which==27){
            $(this).parent().remove();
            return
        }
    });
}