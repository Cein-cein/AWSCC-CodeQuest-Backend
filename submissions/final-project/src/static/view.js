function showChestTxt(){
    document.getElementById("chest-title").style.display = "inline";
    document.getElementById("sparkle1").style.display = "none";
    document.getElementById("sparkle2").style.display = "none";
    document.getElementById("chest").style.display = "none";
}

function hideChestTxt(){
    document.getElementById("chest-title").style.display = "none";
    document.getElementById("sparkle1").style.display = "inline";
    document.getElementById("sparkle2").style.display = "inline";
    document.getElementById("chest").style.display = "inline";
}

function goToIndex(){
    window.location.href="/";
}