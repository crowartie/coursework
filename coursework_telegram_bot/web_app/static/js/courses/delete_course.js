function delete_course(){
    var course_id = $(this).parent().parent().attr('id');
    var course=$(this);
    delete_course_ajax(course_id).done(function(){
        course.parent().parent().remove();
        var text="Вопрос успешно удалён.";
        show_toast("Успех",text);
    });
}