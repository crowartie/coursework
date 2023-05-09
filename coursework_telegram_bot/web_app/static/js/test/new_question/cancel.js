function cancel_window_new_question(){
    $('#modal_window_for_new_question').remove();
    $('.window .container .container-content .box-content .item-in-box-content').last().remove();
    $('.window').css('overflow','');
}