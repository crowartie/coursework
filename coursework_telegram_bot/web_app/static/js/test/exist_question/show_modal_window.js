function show_modal_window_for_exist_question(){
    $('.window').css('overflow','hidden');
    var question=$(this).text();
    var question_id=$(this).parent().attr('id');
    $('.window').append(`
        <div class="container-modal-window" id="modal_window_for_exist_question">
		    <div class="inner-modal-window">
			    <div class="container-header-modal-window">
				    <div class="question-modal-window">
					    <span>${question}</span>
				    </div>
				    <div class="label-modal-window">
					    <div class="container-label">
						    <span>Варианты ответов:</span>
					    </div>
						<button><img src="/static/img/add(plus).svg">Добавить ответ</button>
				    </div>
			    </div>
			    <div class="container-answer-option">
		        </div>
		        <div class="container-button">
                    <button type="button" class="save">Сохранить</button>
                    <button type="button" class="cancel">Отмена</button>
                </div>
		    </div>
	    </div>`);
	get_answer_option(question_id).done(function(response){
	    for(var i=0;i<response.length;i++){
            if(response[i].answer==1){
                var answer=(
                `<label style="color: green;">
                     <span>Правильный ответ</span>
                     <input name=${response[i].question_id} value=${response[i].id} type="radio" checked/>
                 </label>`);
            }
            else if(response[i].answer==0){
                var answer=(
                `<label style="color: red;">
                     <span>Не правильный ответ</span>
                     <input name=${response[i].question_id} value=${response[i].id} type="radio"/>
                 </label>`);
            }
            $('.window .container-modal-window .inner-modal-window .container-answer-option').append(`
            <div class="item-answer-option" id=${response[i].id}>
                <span>${response[i].answer_option}</span>
                <div class="action-buttons-in-item">
                    ${answer}
                    <button type="button" class="edit"><img src="/static/img/edit-img.svg" alt=""> </button>
                    <button type="button" class="del"><img src="/static/img/del-img.svg" alt=""> </button>
                </div>
            </div>`);
        }
        $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option .action-buttons-in-item').on("click",'.del',delete_answer_option_exist_question);
        $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option .action-buttons-in-item').on("click",'.edit',edit_answer_option_exist_question);
	    $('#modal_window_for_exist_question .inner-modal-window .container-answer-option .item-answer-option label').on('click','input',changing_true_answer_exist_question);
	});

	    $('#modal_window_for_exist_question .inner-modal-window .container-header-modal-window .label-modal-window ').on('click','button',question_id,create_answer_option_in_exist_question);
        $('#modal_window_for_exist_question .inner-modal-window .container-button').on('click','.save',question_id,save_answer_options_in_exist_question);
        $('#modal_window_for_exist_question .inner-modal-window .container-button .cancel').on('click',cancel_window_exist_question);
}
