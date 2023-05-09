function show_modal_window_for_exist_course(){
    if($(this).parent().find('.action-buttons-in-item label input[type="checkbox"]').is(':checked')){
        return;
    }
    $('.window').css('overflow','hidden');
    var course_name=$(this).text();
    var course_id=$(this).parent().attr('id');
    $('.window').append(`
        <div class="container-modal-window" id="modal_window_for_exist_course">
		    <div class="inner-modal-window">
			    <div class="container-header-modal-window">
				    <div class="question-modal-window">
					    <span>${course_name}</span>
				    </div>
				    <div class="label-modal-window">
                        <span class="heading-file">Файл:</span>
					    <div class="container-label">
						    <span></span>
					    </div>
					    <label>
					    <span><img src="/static/img/add(plus).svg">Загрузить файл</span>

						<input id="uploadFile" type="file"></input>
						</label>
				    </div>
			    </div>
			    <div class="container-course-text">
			        <textarea></textarea>
		        </div>
		        <div class="container-button">
                    <button type="button" class="save">Сохранить</button>
                    <button type="button" class="cancel">Отмена</button>
                </div>
		    </div>
	    </div>
    `);
    get_path_exist_course(course_id).done(function(response){

        var file_name=response.file_path;
        get_text_exist_course(response.file_path).done(function(response){
            $('#modal_window_for_exist_course .inner-modal-window .container-header-modal-window .label-modal-window .container-label span').last().text(file_name.slice(8,file_name.length));
            $('.container-course-text textarea').val(response.text);
        });
    });
    $('#uploadFile').on('change',uploading_file);
    $('#modal_window_for_exist_course .inner-modal-window .container-button').on('click','.save',course_id,save_course_in_exist_course);
    $('#modal_window_for_exist_course .inner-modal-window .container-button').on('click','.cancel',course_id,cancel_window_for_exist_course);
}