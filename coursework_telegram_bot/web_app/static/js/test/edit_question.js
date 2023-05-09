function edit_question(){
    var question_id = $(this).parent().parent().attr('id');
    var oldNameQuestion=$(this).parent().parent().children('span').text();
    $(this).parent().parent().children('span').replaceWith(`
            <input type="text" id="input-edit-question">`);
    $('#input-edit-question').val(oldNameQuestion);
    $('#input-edit-question').focus();
    $('#input-edit-question').on('blur keyup',function(e){
        if(e.type=="blur" || e.which == 13){
            if($('#input-edit-question').val().length<1){
                $('#input-edit-question').replaceWith(`<span>${oldNameQuestion}</span>`);
                var text="Редактированное название вопроса является пустым.";
                show_toast("Прерывание",text);
                return;
            }
            if($('#input-edit-question').val()==oldNameQuestion){
                $('#input-edit-question').replaceWith(`<span>${oldNameQuestion}</span>`);
                return;
            }
            if($('.window .container .container-content .box-content .item-in-box-content span').length>0){
                var identicalAnswerOption=0;
                $('.window .container .container-content .box-content .item-in-box-content span').each(function(){
                    if($('#input-edit-question').val()==$(this).text()){
                        identicalAnswerOption=1;
                        return;
                    }
                });
                if (identicalAnswerOption==1){
                    identicalAnswerOption=0;
                    var text="Вопрос с таким названием уже существует в данном тесте.";
                    show_toast("Прерывание",text);
                    $('#input-edit-question').replaceWith(`<span>${oldNameQuestion}</span>`);
                    return;
                }
            }
            edit_question_ajax(question_id,$('#input-edit-question').val()).done(function(){
                var text="Название вопроса успешно изменено.";
                show_toast("Успех",text);
                $('#input-edit-question').replaceWith(`<span>${$('#input-edit-question').val()}</span>`);
            });
        }
        else if(e.which==27){
            $('#input-edit-question').replaceWith(`<span>${oldNameQuestion}</span>`);
            return;
        }
    });
}