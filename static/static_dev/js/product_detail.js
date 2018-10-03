$(function() {
    var form = $('#purchase-form');
    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $("#amount input").val();
        var submitBtn = $('#purchase-submit-btn');
        var productId = submitBtn.data('product_id');
        var productPrice = submitBtn.data('price');
        var productName = submitBtn.data('name');

        console.log(nmb, productId, productPrice, productName);
    })
});

function JewelryAccessoriesFadeIn(){
    $("h2.home").fadeIn(5000);
};

/*function displayOwnInput(){
    $( "#product-own-size-input").css('display', 'inline');
}*/

setTimeout(JewelryAccessoriesFadeIn, 500);
