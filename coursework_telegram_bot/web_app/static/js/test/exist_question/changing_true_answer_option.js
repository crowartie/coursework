function changing_true_answer_exist_question(){
    $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option label span').text("Не правильный ответ");
    $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option label span').css('color','red');
    $(this).parent().find('span').text("Правильный ответ")
    $(this).parent().find('span').css('color','green');
}