// populate with all courses

// Listens to checkboxes and runs specific code
$(function() {
    // bind a button to the checkboxes
    console.log("Filter pressed")
    $('#filterDiv :checkbox').bind('click', function() {
        updateCourseList();
    });
});

function populate(jsonCourseList) {
    /**
     * This function dynamically populates the webpage with new content courses
     * @param {JSON} jsonCourseList populates html elements with the JSON data
     */
    $('#courseList').empty();
    for (var key in jsonCourseList) {
        
        courseName = jsonCourseList[key].Name;
        instructor = jsonCourseList[key].Instructor;
        courseCode = jsonCourseList[key]["Course Code"];
        startTime = jsonCourseList[key]["end_time"];
        endTime = jsonCourseList[key]["start_time"];
        console.log(jsonCourseList[key])
        $('#courseList').append(`
            <div class="accordion" id="accordionExample${key}">
                <div class="card">
                    <div class="card-header" id=headingOne${key}>
                        <h2 class="mb-0">
                            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapse${key}"  aria-expanded="false" aria-controls="collapse${key}">
                                ${courseCode} --- ${courseName}
                            </button>
                        </h2>
                        <p>Instructor: ${instructor}</p>
                    </div>

                    <div id="collapse${key}" class="collapse" aria-labelledby="heading${key}" data-parent="#accordionExample${key}">
                        <div class="card-body">
                        <strong>Course Description</strong>
                        <br></br>
                        <strong>Course Code</strong>
                        <li>${courseCode}</li>
                        <strong>Instructor</strong>
                        <li>${instructor}</li>
                        <strong>Start Time</strong>
                        <li>${startTime}</li>
                        <strong>End Time</strong>
                        <li>${endTime}</li>
                        <button id="button_${key}" type="button" class="btn btn-primary">Add Course</button>
                        
                        <!-- Currently putting this here just to get the site working. 
                        // Will not assign a click listener for every element.
                        // FIXME: Only make onclick listeners for open course boxes.
                        -->
        
                        <script type=text/javascript> 
                        document.getElementById("button_${key}").onclick = function() {
                            console.log("${key} button was clicked")
                            addCourseToTable("${key}")
                        }
                        </script>
                    </div>
                </div>
            </div>
        `);

        
    }
    
};

function addCourseToTable(courseCodeString) {
    /**
     * adds courseCode to a list on the server
     * @param {String} courseCode: the code for the course the user wishes to add to the schedule
     */
    courseCodeJSON = {courseCode: courseCodeString}
    $.getJSON($SCRIPT_ROOT + '/_addCourseById', courseCodeJSON, function(data) {
        console.log(data)
    })

}

function updateCourseList() {
    let queryParamsObject = {}
    let cart = [];
    // add key value pairs to the javascript object using the key names specified by 
    // html value attribute
    $.each($('#filterDiv :checkbox'), function(index) {
        queryParamsObject[$(this).val()] = $(this).is(":checked");
        cart.push(queryParamsObject)
    })
    
    console.log(queryParamsObject)
    $.getJSON($SCRIPT_ROOT + '/_update_course_list', queryParamsObject, function(data) {
        queryResult = data.result
        var queryResultJSON = JSON.parse(queryResult)
        populate(queryResultJSON);

        // Trying out search, but doesn't currently work. Need to fix the input format.
        // Has to be a list of json objects
        var options = {
            shouldSort: true,
            threshold: 0.6,
            location: 0,
            distance: 100,
            maxPatternLength: 32,
            minMatchCharLength: 1,
            keys: [
              "Name",
              "Instructor"
            ]
          };
          var fuse = new Fuse([queryResultJSON], options); // "list" is the item array
          var result = fuse.search("Dabby");
          console.log(result);
    });
    
    return false;
};