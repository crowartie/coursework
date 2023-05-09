function edit_name(){
    var id=$(this).parent().parent().attr('id');
    var oldName=$(this).parent().parent().find('a span').text();
    var groupOldTagsName=`<a href="/page-tests/${id}"><span>${oldName}</span></a>`;
    $(this).parent().parent().find('a').replaceWith('<input type="text" id="input-edit">');
    $('#input-edit').val(oldName);
    $('#input-edit').focus();
    $('#input-edit').on('blur keyup',function(e){
        if(e.type=="blur" || e.which == 13){
            $('#input-edit').val($.trim($('#input-edit').val()));
            if($('#input-edit').val().length<1){
                $('#input-edit').replaceWith(groupOldTagsName);
                var text="Новое название является пустым, введите корректное название.";
                show_toast("Прерывание",text);
                return;
            }
            if(oldName == $('#input-edit').val()){
                $('#input-edit').replaceWith(groupOldTagsName);
                return
            }
            if($('.window .container .container-content .box-content .item-in-box-content a span').length>0){
                var identicalAnswerOption=0;
                $('.window .container .container-content .box-content .item-in-box-content a span').each(function(){
                    if($('#input-edit').val()==$(this).text()){
                        identicalAnswerOption=1;
                        return;
                    }
                });
                if(identicalAnswerOption==1){
                    $('#input-edit').replaceWith(groupOldTagsName);
                    var text="Тест с таким названием уже существует.";
                    show_toast("Прерывание",text);
                    return;
                }
            }
            edit_name_ajax(id,$('#input-edit').val()).done(function(){
                $('#input-edit').replaceWith(`
                    <a href="/page-tests/${id}">
                        <span>${$('#input-edit').val()}</span>
                    </a>`
                );
                var text="Название теста успешно изменено.";
                show_toast("Успех",text);
            });
        }
        else if(e.which==27){
            $('#input-edit').replaceWith(groupOldTagsName);
        }
    });
}