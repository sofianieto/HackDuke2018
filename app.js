$("button").click(function(){
    var userq = $('#question').val();
    $.post( "http://127.0.0.1:5000/questionData", { question: userq } );
    });


