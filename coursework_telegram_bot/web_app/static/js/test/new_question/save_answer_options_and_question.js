function save_answer_options_and_question_in_new_question(){
    if($('#modal_window_for_new_question .inner-modal-window .container-answer-option .item-answer-option').length==0){
        var text="Отсутствуют варианты ответа.";
        show_toast("Прерывание",text);
        return;
    }
    if(!$('#modal_window_for_new_question .inner-modal-window .container-answer-option .item-answer-option label input[name="new_question"]').is(':checked')){
        var text="Отсутствует правильный вариант ответа.";
        show_toast("Прерывание",text);
        return;
    }
    if($('#modal_window_for_new_question .inner-modal-window .container-answer-option .item-answer-option').length<2){
        var text="Слишком мало вариантов ответа.";
        show_toast("Прерывание",text);
        return;
    }
    create_new_question($('.window .container .container-content .box-content .item-in-box-content span').last().text()).done(function(response){


        var text="Создан новый вопрос.";
        show_toast("Успех",text);
        $('.window .container .container-content .box-content .item-in-box-content').last().attr('id',response.id_question);
        var arrNewAnswers=[];
        $('#modal_window_for_new_question .inner-modal-window .container-answer-option .item-answer-option label input[type="radio"]').each(function(){
            var answer;
            if($(this).is(':checked')){
                answer=1;
            }
            else{
                answer=0;
            }
            arrNewAnswers.push({
                'id_question': $('.window .container .container-content .box-content .item-in-box-content').last().attr('id'),
                'answerOption': $(this).parent().parent().parent().children('span').text(),
                'answer': answer
            });
        });
        console.log(arrNewAnswers);
        create_new_answer_in_new_question(arrNewAnswers).done(function(response){
            var text="Созданы варианты ответа для созданного вопроса.";
            show_toast("Успех",text);
            $('#modal_window_for_new_question').remove();
            $('.window').css('overflow','');
            return;
        });
    });
}