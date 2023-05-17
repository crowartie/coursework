$('.window .container .container-header-content .container-button button').on('click',create_question);
$(document).on('click','.window .container .container-content .box-content .item-in-box-content span',show_modal_window_for_exist_question);

$(document).on('click','.window .container .container-content .box-content .item-in-box-content .action-buttons-in-item .del',delete_question);
$(document).on('click','.window .container .container-content .box-content .item-in-box-content .action-buttons-in-item .edit',edit_question);