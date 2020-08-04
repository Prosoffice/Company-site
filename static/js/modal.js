function validate(val) {
v1 = document.getElementById("sub");
v2 = document.getElementById("msg");

flag = true;

if(val>=1 || val==0) {
if(v1.value == "") {
v1.style.borderColor = "red";
flag = false;
}
else {
v1.style.borderColor = "green";
flag = true;
}
}

if(val>=2 || val==0) {
if(v2.value == "") {
v2.style.borderColor = "red";
flag = false;
}
else {
v2.style.borderColor = "green";
flag = true;
}
}

return flag;
}

$(document).ready(function(){

var current_fs, next_fs, previous_fs;

$(".next").click(function(){

str1 = "next1";
str2 = "next2";
str3 = "next3";

if(!str1.localeCompare($(this).attr('id')) && document.getElementById("customCheck1").checked == 1) {
val1 = true;
}
else {
val1 = false;
}

if(!str2.localeCompare($(this).attr('id')) && document.getElementById("sub").value != "") {
val21 = true;
}
else {
val21 = false;
}

if(!str2.localeCompare($(this).attr('id')) && document.getElementById("msg").value != "") {
val22 = true;
}
else {
val22 = false;
}

if((!str1.localeCompare($(this).attr('id')) && val1 == true) || (!str2.localeCompare($(this).attr('id')) && val21 == true && val22 == true) || !str3.localeCompare($(this).attr('id'))) {
current_fs = $(this).parent().parent();
next_fs = $(this).parent().parent().next();

$(current_fs).removeClass("show");
$(next_fs).addClass("show");

current_fs.animate({}, {
step: function() {

current_fs.css({
'display': 'none',
'position': 'relative'
});

next_fs.css({
'display': 'block'
});
}
});
}
});

$(".prev").click(function(){

current_fs = $(this).parent().parent();
previous_fs = $(this).parent().parent().prev();

$(current_fs).removeClass("show");
$(previous_fs).addClass("show");

current_fs.animate({}, {
step: function() {

current_fs.css({
'display': 'none',
'position': 'relative'
});

previous_fs.css({
'display': 'block'
});
}
});
});

});