// $("button").click(function(){
//     var userq = $('#question').val();
//     console.log(userq);
//     $.post( "http://127.0.0.1:5000/questionData", { question: userq } );
//     });

// var xhttp = new XMLHttpRequest();
// xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//        // Typical action to be performed when the document is ready:
//        document.getElementById("demo").innerHTML = xhttp.responseText;
//     }
// };
// xhttp.open("GET", "filename", true);
// xhttp.send();
function postquestion(){
    var userq = document.getElementById("#question").val;
    var body = { question: userq };
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:5000/questionData', true);

    xhr.onload = function () {
    return;
        // Request finished. Do processing here.
    };

    
    xhr.send(body);
// xhr.send('string');
// xhr.send(new Blob());
// xhr.send(new Int8Array());
// xhr.send(document);
};