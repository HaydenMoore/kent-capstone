for (var i = 0; i < 4; i++){
    var numString = i.toString();
    var thisCourse = "course-" + numString;
    var thisTutor = "tutor" + numString;
    var thisDay = "day" + numString;
    var thisTime = "time" + numString;
    var thisNote = "note" + numString;
    var thisInput = "input" + numString;

    var course = courses[i];
    var tutor = tutors[i];
    var day = days[i];
    var time = times[i];
    var note = notes[i];
    var course_number = course_numbers[i];

    document.getElementById(thisCourse).innerHTML = course;
    document.getElementById(thisTutor).innerHTML = tutor;
    document.getElementById(thisDay).innerHTML = day;
    document.getElementById(thisTime).innerHTML = time;
    document.getElementById(thisNote).innerHTML = note;
    document.getElementById(thisInput).value = course_number;

};

document.getElementById('username-comments').innerHTML = localStorage.getItem("username");