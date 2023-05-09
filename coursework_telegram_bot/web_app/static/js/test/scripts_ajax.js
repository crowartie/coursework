
function create_new_question(nameNewQuestion){
    return $.ajax({
        url: '/_create_new_question',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'id_test': id_test, 'question':nameNewQuestion})
    });
}

function create_new_answer_in_new_question(arrNewAnswers){
    return $.ajax({
        url: '/_create_new_answer_in_new_question',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(arrNewAnswers)}
    );
}
function get_answer_option(question_id){
    return $.ajax({
        url: '/_get_answer_option',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'question_id': question_id})
   });
}

function update_answer_options_in_exist_question(arrUpdateAnswers,question_id){
    return $.ajax({
        url: '/_update_answer_options_in_exist_question',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'answer_options': arrUpdateAnswers,'question_id': question_id})
    });
}

function delete_question_ajax(question_id){
    return $.ajax({
        url: '/_delete_question',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'question_id': question_id})
    });
}
function edit_question_ajax(question_id,question_name){
    return $.ajax({
        url: '/_edit_question',
        method: 'post',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'question_id': question_id,'question_name':question_name})
    });
}