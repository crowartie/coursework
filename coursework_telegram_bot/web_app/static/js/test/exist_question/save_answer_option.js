function save_answer_options_in_exist_question(question_id){
    if($('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option').length==0){
        var text="Отсутствуют варианты ответа.";
        show_toast("Прерывание",text);
        return;
    }
    if(!$('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option label input[name='+question_id.data+']').is(':checked')){
        var text="Отсутствует правильный вариант ответа.";
        show_toast("Прерывание",text);
        return;
    }
    if($('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option').length<2){
        var text="Слишком мало вариантов ответа.";
        show_toast("Прерывание",text);
        return;
    }
    var arrUpdateAnswers=[];
    $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option').each(function(){
        var answer_option_id;
        var answer;
        if($(this).attr('id')){
            answer_option_id=$(this).attr('id');
        }
        else{
            answer_option_id=0;
        }
        if($(this).find('label input[type="radio"]').is(':checked')){
            answer=1;
        }
        else{
            answer=0;
        }
        arrUpdateAnswers.push({
            'question_id': question_id.data,
            'answer_option_id': answer_option_id,
            'answer_name': $(this).children('span').text(),
            'answer': answer
        });
    });
    update_answer_options_in_exist_question(arrUpdateAnswers,question_id.data).done(function(){
        var text="Варианты ответов вопроса успешно редактированны.";
        show_toast("Успех",text);
        $('#modal_window_for_exist_question').remove();
        $('.window').css('overflow','');
        return;
    });
}