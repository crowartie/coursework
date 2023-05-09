function edit_status(){
    var id=$(this).parent().parent().parent().attr('id');
    var span=$(this).parent().parent().parent().children('span');
    var label=$(this).parent().children('span');
    var checkbox=$(this);
    if($(this).is(':checked')){
        get_path_exist_course(id).done(function(response){
            get_count_symbols_file_path(response.file_path).done(function(response){
                if(response.count==0){
                    var text="Текст курса пустой.";
                    show_toast("Прерывание",text);
                    return;
                }
                reset_data_users_in_courses(response.count,id).done(function(){
                    edit_status_ajax(id,1).done(function(){
                        span.css('cursor','auto');
                        label.text("Активный");
                        label.css('color','green');
                        var text="Тест успешно включен.";
                        show_toast("Успех",text);
                    });
                });
            });
        });
    }
    else{
        edit_status_ajax(id,0);
        label.text("не активный");
        span.css('cursor','pointer');
        label.css('color','red');
        var text="Тест успешно отключен для дальнейших изменений.";
        show_toast("Успех",text);
    }
}