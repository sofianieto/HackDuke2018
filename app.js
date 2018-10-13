// $("button").click(function(){
//     $.get("demo_test.asp", function(data, status){
//         alert("Data: " + data + "\nStatus: " + status);
//     });
// });


var userq = $('#question').val();

$.post( "test.php", { question: userq } );