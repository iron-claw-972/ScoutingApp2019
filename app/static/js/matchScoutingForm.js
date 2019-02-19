inputid = ['cargo0', 'cargo1', 'cargo2', 'cargo3', 'hatch0', 'hatch1', 'hatch2', 'hatch3']
labelid = ['c0', 'c1', 'c2', 'c3', 'h0', 'h1', 'h2', 'h3']
buttonfix = ['hatch0', 'hatch1', 'hatch2', 'hatch3', 'cargo0', 'cargo1', 'cargo2', 'cargo3']
var element
for (var i = 0; i < inputid.length; i++) {
    element = document.getElementById(inputid[i])
    element.idnum = i;
    element.addEventListener("click", function () {
        var increase = document.getElementById(labelid[this.idnum]);
        increase.textContent = Number(increase.textContent) + 1
    });
}
for (var f = 0; f < buttonfix.length; f++) {
    document.querySelector('#' + buttonfix[f]).style = "width:17.5vw"
}
$("#form").submit(function (eventObj) {
    var values = [];
    for (var i = 0; i < inputid.length; i++) {
        val = document.getElementById(inputid[i]).textContent;
        values.push(val);
    }
    $('<input />').attr('type', 'hidden')
        .attr('cargo0', val[0])
        .attr('cargo1', val[1])
        .attr('cargo2', val[2])
        .attr('cargo3', val[3])
        .attr('hatch0', val[4])
        .attr('hatch1', val[5])
        .attr('hatch2', val[6])
        .attr('hatch3', val[7])
        .appendTo(this);
    return true;
});