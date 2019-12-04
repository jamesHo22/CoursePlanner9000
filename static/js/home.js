// This JS code is used in home.html 
$(function() {
  // bind a button to the calculate tag
  console.log("Link pressed")
  $('a#calculate').bind('click', function() {addNumbers()});
});

function addNumbers() {
  // $.getJSON(url, data, func) sends a GET request to url and will send the contents of the data object as query parameters. 
  // Once the data arrived, it will call the given function with the return value as argument. 
  // Note that we can use the $SCRIPT_ROOT variable here that we set earlier.
  console.log("addNumbers called");
  $.getJSON($SCRIPT_ROOT + '/_add_numbers', {a: $('input[name="a"]').val(), b: $('input[name="b"]').val()}, function(data) {
    elementSetText($("#result"), data.result)
    updateCourseList()
  });  
  return false;
};

/**
 * @param elementID a jQuery selector
 * @param {String} text the text you want to set the element to
 */
function elementSetText(jQueryelementID, text) {
  // this function takes an elementID and changes its text to whatever is passed into it
  jQueryelementID.text(text);
  
};

function updateCourseList() {
  $.getJSON($SCRIPT_ROOT + '/_update_course_list', {a: "Hello"});
  return false;
};