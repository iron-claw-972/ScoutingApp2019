function adjustEmbedDivTop() {
    document.getElementById("embedDiv").style.top = document.getElementById("tabs").getBoundingClientRect().bottom + "px";
}

adjustEmbedDivTop();
window.onresize = adjustEmbedDivTop;