function save_course_in_new_course(name_course){
    $('#textarea').val($.trim($('#textarea').val()))
    if($('#textarea').val()==""){
        var text="Текст отсутствует";
        show_toast("Прерывание",text);
        return;
    }
    else{
        create_course_ajax(name_course.data).done(function(response){
            id=response.id;
            save_text_in_course(response.file_path,$('textarea').val()).done(function(){
                $('.window .container .container-content .box-content .item-in-box-content').attr('id',id);
                $('#modal_window_for_new_course').remove();

            });

        });
    }

}