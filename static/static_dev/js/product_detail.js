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
    var productDiscount = parseFloat(submitBtn.data('discount'));
    var discount = 0;
    var oldPrice = document.getElementById("product-discount");

    if (!isNaN(productDiscount) && productDiscount) {
        discount = productDiscount;
        }


        
function cost( num ) {
        var cost = new Number( parseFloat( num ) * productPrice);
        
        if ( !isNaN(cost) ) {
            //var precision = cost.toString().length === 3 ? 3 : 4;
            //return cost.toPrecision( precision );
            return cost;
        } else {
            return 0;
        }
}

if (discount) {
    totalPrice.innerHTML = cost( quantityInput.val() ) - cost( quantityInput.val() )*discount/100;
    oldPrice.innerHTML = cost( quantityInput.val() );
    } else {
        totalPrice.innerHTML = cost( quantityInput.val() );
    }

quantityInput[0].addEventListener('input', function( event ) {
    var value = event.target.value;
    if ( isNaN( value ) ) {
    totalPrice.innerHTML = cost( 0 );
    } else if (discount) {
        totalPrice.innerHTML = cost( value ) - cost( value )*discount/100;
        oldPrice.innerHTML = cost( value );
        } else {
            totalPrice.innerHTML = cost( value );
        }
});

console.log(productPrice);
console.log(discount);
});

function JewelryAccessoriesFadeIn(){
    $("h2.home").fadeIn(5000);
};

/*function displayOwnInput(){
    $( "#product-own-size-input").css('display', 'inline');
}*/

setTimeout(JewelryAccessoriesFadeIn, 500);
