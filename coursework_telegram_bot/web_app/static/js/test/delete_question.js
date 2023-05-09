function delete_question(){
    var question_id = $(this).parent().parent().attr('id');
    var question = $(this);
    delete_question_ajax(question_id).done(function(){
        question.parent().parent().remove();
        var text="Вопрос успешно удалён.";
        show_toast("Успех",text);
    });
}
