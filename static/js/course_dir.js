// Listens to checkboxes and runs specific code
$(function() {
    // bind a button to the calculate tag
    console.log("Filter pressed")
    $('#filterDiv :checkbox').bind('click', function() {console.log("checkbox clicked")});
  });