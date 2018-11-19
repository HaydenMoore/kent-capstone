document.getElementById('username-comments').innerHTML = localStorage.getItem("username");

function myProfile() {
    var data = localStorage.getItem("username");
    $.post( "/profile", {
        javascript_data: data
    });
}