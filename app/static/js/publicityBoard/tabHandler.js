function changeTab(tab, embedId) {
    if (tab != document.getElementById('selected')) {
        document.getElementById('selected').id = '';
        tab.id = 'selected';
        for(element of document.getElementsByTagName('embed')) {
            element.style.display = 'none';
        }
        document.getElementById(embedId).style.display = 'initial';
    }
    
}