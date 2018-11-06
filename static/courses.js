for (var i = 0; i < 4; i++){
    var numString = i.toString();
    var thisCourse = "course" + numString;
    var thisCourseDay = "course-day" + numString;
    course = courses[i];
    day = days[i];
    document.getElementById(thisCourse).innerHTML = course;
    document.getElementById(thisCourseDay).innerHTML = day;
};