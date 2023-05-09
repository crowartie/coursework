function save_course_in_exist_course(course_id){
    $('.window .container-modal-window .inner-modal-window .container-course-text textarea').val($.trim($('.window .container-modal-window .inner-modal-window .container-course-text textarea').val()))
    if($('.window .container-modal-window .inner-modal-window .container-course-text textarea').val()==""){
        var text="Текст отсутствует";
        show_toast("Прерывание",text);
        return;
    }
    else{
        get_path_exist_course(course_id.data).done(function(response){
            text=$('.window .container-modal-window .inner-modal-window .container-course-text textarea').val();
            save_text_in_course(response.file_path,text).done(function(){
                $('.window .container-modal-window').remove();
                var text="Текст курса обновлён";
                show_toast("Успех",text);
                return;
            });
        });
    }
}