$(function() {
    var form = $('#purchase-form');
    form.on('submit', function(e){
        e.preventDefault();
    //ajax
    var csrf_token = $('#purchase-form [name="csrfmiddlewaretoken"]').val();
    var data = {
        csrfmiddlewaretoken : csrf_token
    };
    var url = form.attr("action");

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        dataType: 'json',
        cache: true,
        success: function (data) {
            console.log("OK");
            console.log(data);
            console.log(url);
        },
        error: function(){
            console.log("error");
        }
});

    // ajax


    });
});

