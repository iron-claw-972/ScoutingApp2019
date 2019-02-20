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
document.querySelector('#inputForm > input[type="submit"]').onclick = function (eventObj) {
    var values = [];
    inputid = ['c0', 'c1', 'c2', 'c3', 'h0', 'h1', 'h2', 'h3']

    for (var i = 0; i < inputid.length; i++) {
        val = document.getElementById(inputid[i]).textContent;
        values.push(val);
    }
    alert(values)
    $('<input />').attr('type', 'hidden')
        .attr('name', 'cargo')
        .attr('value', values[0] + ',' + values[1] + ',' + values[2] + ',' + values[3] + ',')
        .appendTo(this);
    $('<input />').attr('type', 'hidden')
        .attr('name', 'hatch')
        .attr('value', values[4] + ',' + values[5] + ',' + values[6] + ',' + values[7] + ',')
        .appendTo(this);
    return true;
}