function create_answer_option_in_exist_question(question_id){
    $('#modal_window_for_exist_question .inner-modal-window .container-answer-option').append(`
        <div class="item-answer-option">
            <input type="text" id="input-create-answer"/>
        </div>`);
    $('#input-create-answer').focus();
    $('#input-create-answer').on('blur keyup',function(e){
        if(e.type=="blur" || e.which == 13){
            $('#input-create-answer').val($.trim($('#input-create-answer').val()));
            if($('#input-create-answer').val().length<1){
                $('#input-create-answer').parent().remove();
                var text="Название нового варианта ответа является пустым.";
                show_toast("Прерывание",text);
                return;
            }
            if($('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option').length>0){
                var identicalAnswerOption=0;
                $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option').children('span').each(function(){
                    if($('#input-create-answer').val()==$(this).text()){
                        identicalAnswerOption=1;
                        return;
                    }
                });
                if (identicalAnswerOption==1){
                    $('#input-create-answer').parent().remove();
                    identicalAnswerOption=0;
                    var text="Название нового варианта ответа уже есть у данного вопроса.";
                    show_toast("Прерывание",text);
                    return;
                }
            }
            $('#input-create-answer').parent().html(`
                <span>${$('#input-create-answer').val()}</span>
                <div class="action-buttons-in-item">
                    <label style="color: red;">
                        <span>Не правильный ответ</span>
                        <input name=${question_id.data} type="radio"/>
                    </label>
                    <button type="button" class="edit"><img src="/static/img/edit-img.svg" alt=""> </button>
                    <button type="button" class="del"><img src="/static/img/del-img.svg" alt=""> </button>
                </div>`);
            $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option .action-buttons-in-item').last().on("click",'.del',delete_answer_option_exist_question);
            $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option .action-buttons-in-item').last().on("click",'.edit',edit_answer_option_exist_question);
	        $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option label').last().on('click','input',changing_true_answer_exist_question);
        }
        else if(e.which==27){
            $('#input-create-answer').parent().remove();
            return;
        }
    });
}
