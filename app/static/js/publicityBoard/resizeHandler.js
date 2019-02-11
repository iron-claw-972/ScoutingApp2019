function adjustElements() {
    document.getElementById("embedDiv").style.top = document.getElementById("tabs").getBoundingClientRect().bottom - 1 + "px";
}

adjustElements();
window.onresize = adjustElements;