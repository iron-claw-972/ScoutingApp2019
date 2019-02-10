function adjustEmbedDivTop() {
    document.getElementById("embedDiv").style.top = document.getElementById("tabs").getBoundingClientRect().bottom - 1 + "px";
}

adjustEmbedDivTop();
window.onresize = adjustEmbedDivTop;