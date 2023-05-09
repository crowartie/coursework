function delete_test(){
    var id=$(this).parent().parent().attr('id');
    var item=$(this);
    check_status_test(id).done(function(response){
        if(response.status==0){
            delete_ajax(id).done(function(response){
                item.parent().parent().remove();
                var text="тест успешно удалён.";
                show_toast("Успех",text);
            });
        }
        else{
            var text="Тест активный, отключите его и повторите попытку.";
            show_toast("Прерывание",text);
            return;
        }
    });
}

