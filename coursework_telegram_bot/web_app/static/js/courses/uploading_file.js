function uploading_file(e){
    file=e.target.files[0];
    if(file){
        if(file.type!="text/plain"){
            var text="У файла некорректный формат.\nДолжен быть .txt или типа text/plain";
            show_toast("Прерывание",text);
            return;
        }
        var reader = new FileReader();
        reader.onload = function(e){
            upload_file_ajax(e.target.result).done(function(response){
                if(response.text.length==0){
                    var text="Файл пустой";
                    show_toast("Прерывание",text);
                    return;
                }
                else{
                    $('.container-course-text textarea').val(response.text);
                    var text="Файл успешно загружен";
                    show_toast("Прерывание",text);
                    return;
                }
            });
        };
        reader.readAsText(file);
    }
}