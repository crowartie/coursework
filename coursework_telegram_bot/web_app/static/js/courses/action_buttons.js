$(document).find('.window .container .container-content .box-content .item-in-box-content').children('span').on('click',show_modal_window_for_exist_course);
$(document).on('change','.window .container .container-content .box-content .item-in-box-content .action-buttons-in-item label input[type="checkbox"]',edit_status);
$('.window .container .container-header-content .container-button button').click(create_course);
$(document).on('click','.window .container .container-content .box-content .item-in-box-content .action-buttons-in-item .edit',edit_course);
$(document).on('click','.window .container .container-content .box-content .item-in-box-content .action-buttons-in-item .del',delete_course);

