var sparkle = document.getElementById("sparkle"); //Get id of image
var scale = "scale(0)"; //Set value for variable scale
var id = setInterval(animate, 500); //Execute function animate() every 500ms

function animate(){
    //Loop scale image
    //If image scale is 0 then set scale to 1 otherwise set scale to 0
    if(sparkle.style.transform == "scale(0)"){
        sparkle.style.transform = "scale(1)";
    }else{
        sparkle.style.transform = "scale(0)";
    }
}

var red = document.getElementById("redkey-title"); //Get id of text
var redkey = document.getElementById("redkey");
//Text display is already set to none in css file
function showRed(){
    red.style.display = "block"; //Text display value will be set to block when cursor enters div
    redkey.style.display = "none";
}
function hideRed(){
    red.style.display = "none"; //Text display value will be set to none when cursor exits div
    redkey.style.display = "inline";
}
            
var blue = document.getElementById("bluekey-title");
var bluekey = document.getElementById("bluekey");
//Text display is already set to none in css file
function showBlue(){
    blue.style.display = "block"; //Text display value will be set to block when cursor enters div
    bluekey.style.display = "none";
}
function hideBlue(){
    blue.style.display = "none"; //Text display value will be set to none when cursor exits div
    bluekey.style.display = "inline";
}

//Navigates window to manage.html
function goToManage(){
    window.location.href = "/dataMng"
}

//Navigates window to view.html
function goToView(){
    window.location.href = "/dataView"
}