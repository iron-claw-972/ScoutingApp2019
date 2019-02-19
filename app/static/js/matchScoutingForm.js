inputid = ['cargo0', 'cargo1', 'cargo2', 'cargo3', 'hatch0', 'hatch1', 'hatch2', 'hatch3']
labelid = ['c0', 'c1', 'c2', 'c3', 'h0', 'h1', 'h2', 'h3']
var element
for (var i = 0; i < inputid.length; i++) {
    element = document.getElementById(inputid[i])
    element.idnum = i;
    element.addEventListener("click", function () {
        var increase = document.getElementById(labelid[this.idnum]);
        increase.textContent = Number(increase.textContent) + 1
    });
}