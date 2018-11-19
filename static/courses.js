for (var i = 0; i < 4; i++){
    var numString = i.toString();
    var thisCourse = "course" + numString;
    var thisCourseLink = "course-link" + numString;
    var thisCourseInput = "course-input" + numString;
    var course = courses[i];
    var day = days[i];
    var time = times[i];
    document.getElementById(thisCourse).innerHTML = course;
    document.getElementById(thisCourseLink).href = "/comments";
  
};



if (username) {
    //storing local variables
    localStorage.setItem("username", username);
    try {
    document.getElementById('username').innerHTML = username;
    }
    catch(error) {
        console.log(error);
    }
}



//Creating on click events for each course
document.getElementById("course-link0").onclick = function fun() {
        var myCourse = document.getElementById("course0").innerHTML;
        localStorage.setItem("course", myCourse);
}