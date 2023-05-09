function edit_course(){
    var course_id = $(this).parent().parent().attr('id');
    var oldNameCourse=$(this).parent().parent().children('span').text();
    $(this).parent().parent().children('span').replaceWith(`
            <input type="text" id="input-edit-course">`);
    $('#input-edit-course').val(oldNameCourse);
    $('#input-edit-course').focus();
    $('#input-edit-course').on('blur keyup',function(e){
        if(e.type=="blur" || e.which == 13){
            if($('#input-edit-course').val().length<1){
                $('#input-edit-course').replaceWith(`<span>${oldNameCourse}</span>`);
                var text="Редактированное название курса является пустым.";
                show_toast("Прерывание",text);
                return;
            }
            if($('#input-edit-course').val()==oldNameCourse){
                $('#input-edit-course').replaceWith(`<span>${oldNameCourse}</span>`);
                return;
            }
            if($('.window .container .container-content .box-content .item-in-box-content').children('span').length>0){
                var identicalAnswerOption=0;
                $('.window .container .container-content .box-content .item-in-box-content').children('span').each(function(){
                    if($('#input-edit-course').val()==$(this).text()){
                        identicalAnswerOption=1;
                        return;
                    }
                });
                if (identicalAnswerOption==1){
                    identicalAnswerOption=0;
                    var text="Курс с таким названием уже существует в данном тесте.";
                    show_toast("Прерывание",text);
                    $('#input-edit-course').replaceWith(`<span>${oldNameCourse}</span>`);
                    return;
                }
            }
            edit_course_ajax(course_id,$('#input-edit-course').val()).done(function(){
                var text="Название курса успешно изменено.";
                show_toast("Успех",text);
                $('#input-edit-course').replaceWith(`<span>${$('#input-edit-course').val()}</span>`);
            });
        }
        else if(e.which==27){
            $('#input-edit-course').replaceWith(`<span>${oldNameCourse}</span>`);
            return;
        }

        });
}