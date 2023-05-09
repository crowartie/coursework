function show_modal_window_for_new_question(){
    $('.window').css('overflow','hidden');
    $('.window').append(`
        <div class="container-modal-window" id="modal_window_for_new_question">
            <div class="inner-modal-window">
                <div class="container-header-modal-window">
                    <div class="question-modal-window">
                        <span>${$('#input-create-question').val()}</span>
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
        </div>`
    );
    $('#input-create-question').parent().html(`
        <span>${$('#input-create-question').val()}</span>
        <div class="action-buttons-in-item">
            <button type="button" class="edit"><img src="/static/img/edit-img.svg" alt=""></button>
            <button type="button" class="del"><img src="/static/img/del-img.svg" alt=""></button>
        </div>`
    );
        $('#modal_window_for_new_question .inner-modal-window .container-header-modal-window .label-modal-window  button').on('click',create_answer_option_in_new_question);
        $('#modal_window_for_new_question .inner-modal-window .container-button .save').on('click',save_answer_options_and_question_in_new_question);
        $('#modal_window_for_new_question .inner-modal-window .container-button .cancel').on('click',cancel_window_new_question);

}