$(document).on('click','.window .container .container-content .box-content .item-in-box-content .del',delete_test);
$(document).on('change','.window .container .container-content .box-content .item-in-box-content input[type="checkbox"]',edit_status);
$(document).on('click','.window .container .container-content .box-content .item-in-box-content .edit',edit_name);
$('.window .container .container-header-content .container-button button').click(add_test);
