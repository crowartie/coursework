function edit_status(){
    var id=$(this).parent().parent().parent().attr('id');
    var a=$(this).parent().parent().parent().find('a');
    var label=$(this).parent().children('span');
    var checkbox=$(this);
    if($(this).prop('checked')==true){
        get_count_questions(id).done(function(response){
            if(response.count==0){
               checkbox.prop('checked',false);
               a.css('pointer-events','auto');
               var text="У теста отсутствуют вопросы, добавьте вопросы и повторите попытку.";
               show_toast("Прерывание",text);
               return;
            }
            else{
                edit_status_ajax(id,1).done(function(){
                    reset_data_users_enabling_test(id).done(function(){
                        label.text("Активный");
                        label.css('color','green');
                        a.css('pointer-events','none');
                        checkbox.prop('checked',true);
                        var text="Тест успешно включен.";
                        show_toast("Успех",text);
                    });
                });
            }
        });
    }
    else{
        edit_status_ajax(id,0);
        label.text("не активный");
        a.css('pointer-events','auto');
        label.css('color','red');
        var text="Тест успешно отключен для дальнейших изменений.";
        show_toast("Успех",text);
    }
}