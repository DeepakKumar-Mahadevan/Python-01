var table = document.getElementById('ManUtdPlayers');
//var tbody = table.getElementsByTagName('tbody')[0];
//var cells = tbody.getElementsByTagName('td');
//for (var i=0, len=cells.length; i<len; i++){
//    if (cells[i].innerHTML == "England"){
//        cells[i].style.backgroundColor = 'red';
//    }
//    else {
//        cells[i].style.backgroundColor = 'green';
//    }
//}

for (i = 1; i < table.rows.length; i++) {

    // GET THE CELLS COLLECTION OF THE CURRENT ROW.
    var objCells = table.rows.item(i).cells;

    // LOOP THROUGH EACH CELL OF THE CURRENT ROW TO READ CELL VALUES.
    for (var j = 0; j < objCells.length; j++) {
        if (j == 2) { //Change the Font color only for 3rd column
            if (objCells.item(j).innerHTML == "England"){
//                objCells.item(j).style.backgroundColor = 'darkred'; //Background Color
                objCells.item(j).style.color = 'red'; //Font Color
            }
//            else {
//                objCells.item(j).style.backgroundColor = 'green';
//            }
        }
    }
}

