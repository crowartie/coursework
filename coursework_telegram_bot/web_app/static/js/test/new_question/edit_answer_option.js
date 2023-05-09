function edit_answer_option_new_question(){
    var oldNameAnswer=$(this).parent().parent().children('span').text();
    $(this).parent().parent().children('span').replaceWith(`<input type="text" id="input-edit-answer"/>`);
    $('#input-edit-answer').val(oldNameAnswer);
    $('#input-edit-answer').focus();
    $('#input-edit-answer').on('blur keyup',function(e){
        if(e.type=="blur" || e.which == 13){
            $('#input-edit-answer').val($.trim($('#input-edit-answer').val()));
            if($('#input-edit-answer').val().length<1){
                $('#input-edit-answer').replaceWith(`<span>${oldNameAnswer}</span>`);
                var text="Название изменённого варианта ответа являлется пустым.";
                show_toast("Прерывание",text);
                return;
            }
            if($('#input-edit-answer').val()==oldNameAnswer){
                $('#input-edit-answer').replaceWith(`<span>${oldNameAnswer}</span>`);
                return;
            }
            if($('#modal_window_for_new_question .inner-modal-window .container-answer-option .item-answer-option').length>0){
                var identicalAnswerOption=0;
                $('#modal_window_for_new_question .inner-modal-window .container-answer-option .item-answer-option').children('span').each(function(){
                    if($('#input-edit-answer').val()==$(this).text()){
                        identicalAnswerOption=1;
                        return;
                    }
                });
                if (identicalAnswerOption==1){
                    $('#input-edit-answer').replaceWith(`<span>${oldNameAnswer}</span>`);
                    identicalAnswerOption=0;
                    var text="Название изменённого варианта ответа уже существует в данном вопросе.";
                    show_toast("Прерывание",text);
                    return;
                }
            }
            $('#input-edit-answer').replaceWith(`<span>${$('#input-edit-answer').val()}</span>`);
            var text="Вариант ответа успешно изменён.";
            show_toast("Успех",text);
            return;
        }
        else if(e.which==27){
            $('#input-edit-answer').replaceWith(`<span>${oldNameAnswer}</span>`);
            return
        }

    });

}