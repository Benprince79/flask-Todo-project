function myFunction() {
    var x = document.getElementById("myTable").rows.length;
    if (x == 1) {
        document.getElementById("info").innerHTML = "Please Add Items to your List!";
    }
}