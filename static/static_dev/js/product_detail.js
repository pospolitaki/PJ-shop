$(function() {
    var form = $('#purchase-form');
    form.on('submit', function(e){
        e.preventDefault();
        var quantity = $("#amount input").val();
        var submitBtn = $('#purchase-submit-btn');
        var productId = submitBtn.data('product_id');
        var productPrice = submitBtn.data('price');
        var productName = submitBtn.data('name');

        console.log(quantity, productId, productPrice, productName);
    });

    var submitBtn = $('#purchase-submit-btn');
    var productPrice = parseFloat(submitBtn.data('price'));
    var quantityInput = $("#quantity-input");
    var totalPrice = document.getElementById("totalPrice");

    
// Handle the precision up to >= $100
function changeCost( num ) {
    var cost = new Number( parseFloat( num ) * productPrice );
    
    if ( !isNaN(cost) ) {
        //var precision = cost.toString().length === 3 ? 3 : 4;
        //return cost.toPrecision( precision );
        return cost;
    } else {
        return 0;
    }
}
totalPrice.innerHTML = changeCost( quantityInput.val() );    
quantityInput[0].addEventListener('input', function( event ) {
    var value = event.target.value;
    if ( isNaN( value ) ) {
    totalPrice.innerHTML = changeCost( 0 );
    } else {
        totalPrice.innerHTML = changeCost( value );
        } 
});

console.log(productPrice);


});






function JewelryAccessoriesFadeIn(){
    $("h2.home").fadeIn(5000);
};

/*function displayOwnInput(){
    $( "#product-own-size-input").css('display', 'inline');
}*/

setTimeout(JewelryAccessoriesFadeIn, 500);
