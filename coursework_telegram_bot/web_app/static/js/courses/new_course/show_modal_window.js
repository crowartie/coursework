function show_modal_window_for_new_course(){
    $('.window').css('overflow','hidden');
    $('.window').append(`
        <div class="container-modal-window" id="modal_window_for_new_course">
		    <div class="inner-modal-window">
			    <div class="container-header-modal-window">
				    <div class="question-modal-window">
					    <span>${$('#input-create-course').val()}</span>
				    </div>
				    <div class="label-modal-window">
                        <span class="heading-file">Файл:</span>
					    <div class="container-label">
						    <span>Новый файл</span>
					    </div>
					    <label>
					    <span><img src="/static/img/add(plus).svg">Загрузить файл</span>

						<input id="uploadFile" type="file"></input>
						</label>
				    </div>
			    </div>
			    <div class="container-course-text">
			        <textarea id="textarea"></textarea>
		        </div>
		        <div class="container-button">
                    <button type="button" class="save">Сохранить</button>
                    <button type="button" class="cancel">Отмена</button>
                </div>
		    </div>
	    </div>
    `);
    var name_course=$('#input-create-course').val();
    $('#input-create-course').parent().html(`
        <span>${name_course}</span>
        <div class="action-buttons-in-item">
            <label style="color: red;"><span>Не активный</span><input type="checkbox"/></label>
            <button type="button" class="edit"><img src="/static/img/edit-img.svg" alt=""></button>
            <button type="button" class="del"><img src="/static/img/del-img.svg" alt=""></button>
        </div>`
    );
    $('#uploadFile').on('change',uploading_file);
    $('#modal_window_for_new_course .inner-modal-window .container-button').on('click','.save',name_course,save_course_in_new_course);
    $('#modal_window_for_new_course .inner-modal-window .container-button').on('click','.cancel',cancel_window_for_new_course);
}