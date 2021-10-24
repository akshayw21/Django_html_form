function selects() {
    var all = document.getElementById('all')
    var select = document.getElementsByName('hb');
    if (all.checked == true) {
        for (var i = 0; i < select.length; i++) {

            select[i].checked = true;
        }
    } else {
        for (var i = 0; i < select.length; i++) {

            select[i].checked = false;

        }
    }

}




//function deselects() {
//   var select = document.getElementsByName('hb');