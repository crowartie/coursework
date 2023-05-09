



function get_path_exist_course(id){
    return $.ajax({
        url: '/_get_path_exist_course',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id})
    });
}

function get_text_exist_course(file){
    return $.ajax({
        url: '/_get_text_exist_course',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'file': file})
    });
}
function upload_file_ajax(file){
    return $.ajax({
        url: '/_upload_file',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'file': file})
    });
}
function save_text_in_course(file,text){
     return $.ajax({
        url: '/_save_text_in_course',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'file': file,'text': text})
    });
}
function edit_status_ajax(id,status){
     return $.ajax({
        url: '/_edit_status_course',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id,'status':status})
    });
}


function get_count_symbols_file_path(file){
     return $.ajax({
        url: '/_get_count_symbols_file_path',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'file': file})
    });
}
function reset_data_users_in_courses(count_symbols,course_id){
    return $.ajax({
        url: '/_reset_data_in_exist_course',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'count_symbols': count_symbols,'course_id':course_id})
    });
}

function create_course_ajax(course_name){
    return $.ajax({
        url: '/_create_course',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'course_name': course_name})
    });
}
function edit_course_ajax(id,course_name){
    return $.ajax({
        url: '/_edit_course',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id':id,'course_name': course_name})
    });
}
function delete_course_ajax(id){
    return $.ajax({
        url: '/_delete_course',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id':id})
    });
}