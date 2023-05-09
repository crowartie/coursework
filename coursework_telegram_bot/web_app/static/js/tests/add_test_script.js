function add_test(){
    $('.window .container .container-content .box-content')
    .append($(`<div class="item-in-box-content">
                  <input type="text" id="input-create"/>
              </div>`));
    $('#input-create').focus();
    $('#input-create').on('blur keyup',function(e){
        if(e.type=="blur" || e.which == 13){
            $('#input-create').val($.trim($('#input-create').val()));
            if($('#input-create').val().length<1){
                $('#input-create').parent().remove();
                var text="Название нового теста является пустым, введите корректное название.";
                show_toast("Прерывание",text);
                return;
            }
            if($('.window .container .container-content .box-content .item-in-box-content a span').length>0){
                var identicalAnswerOption=0;
                $('.window .container .container-content .box-content .item-in-box-content a span').each(function(){
                    if($('#input-create').val()==$(this).text()){
                        identicalAnswerOption=1;
                        return;
                    }
                });
                if(identicalAnswerOption==1){
                    $('#input-create').parent().remove();
                    var text="Тест с таким названием уже существует.";
                    show_toast("Прерывание",text);
                    return;
                }
            }
            add_test_ajax($('#input-create').val()).done(function(response){
                $('#input-create').parent().attr('id',response.id);
                $('#input-create').parent().html(`
                    <a style="pointer-events: auto;" href="/tests/${response.id}">
                        <span>${response.name}</span>
                    </a>
                    <div class="action-buttons-in-item">
                        <label style="color: red;">
                            <span>Не активный</span>
                            <input type="checkbox"/>
                        </label>
                        <button type="button" class="edit"><img src="static/img/edit-img.svg" alt=""> </button>
                        <button type="button" class="del"><img src="static/img/del-img.svg" alt=""> </button>
                    </div>`
                );
                var text="Тест успешно создан.";
                show_toast("Успех",text);
            });
        }
        else if(e.which==27){
            $('#input-create').parent().remove();
        }
    });
}