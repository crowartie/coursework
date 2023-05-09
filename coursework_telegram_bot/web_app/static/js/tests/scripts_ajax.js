function edit_name_ajax(id,newName){
    return $.ajax({
        url: '/_edit_test',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id, 'name': newName})
    });
}
function delete_ajax(id){
    return $.ajax({
        url: '/_del_test',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id})
    });
}
function check_identical_in_tests_ajax(id,newName){
    return $.ajax({
        url: '/_check_identical_in_tests',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id, 'name': newName})
    });
}

function add_test_ajax(nameNewTest){
    return $.ajax({
        url: '/_add_test',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'name': nameNewTest})
    });
}

function edit_status_ajax(id,status){
    return $.ajax({
        url: '/_edit_status_test',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id,'status': status})
     });
}

function reset_data_users_enabling_test(id){
    return $.ajax({
        url: '/_reset_data_users_enabling_test',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id})
    });
}

function get_count_questions(id){
    return $.ajax({
        url: '/_get_count_questions',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id}),
    });
}

function check_status_test(id){
    return $.ajax({
        url: '/_check_status_test',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id': id}),
    });
}