// Listens to checkboxes and runs specific code
$(function() {
    // bind a button to the calculate tag
    console.log("Filter pressed")
    $('#filterDiv :checkbox').bind('click', function() {
        updateCourseList();
    });
});


function updateCourseList() {
    let queryParamsObject = {}
    let cart = [];
    // add key value pairs to the javascript object using the key names specified by 
    // html value attribute
    $.each($('#filterDiv :checkbox'), function(index) {
        console.log($(this).val())
        queryParamsObject[$(this).val()] = $(this).is(":checked");
        cart.push(queryParamsObject)
    })
    
    console.log(queryParamsObject)
    $.getJSON($SCRIPT_ROOT + '/_update_course_list', queryParamsObject, function(data) {
        console.log(data.result)
    });
    return false;
};