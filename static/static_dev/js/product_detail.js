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
    
    //ajax
    var csrf_token = $('#purchase-form [name="csrfmiddlewaretoken"]').val();
    var data = {
        product_id : productId,
        quantity : quantity,
        csrfmiddlewaretoken : csrf_token
    };
    var url = form.attr("action");

    console.log(data);
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            console.log("OK");
            console.log(data);
            // console.log(data.products_total_nmb);
            // if (data.products_total_nmb || data.products_total_nmb == 0){
            //    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
            //     console.log(data.products);
            //     $('.basket-items ul').html("");
            //     $.each(data.products, function(k, v){
            //        $('.basket-items ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'грн  ' +
            //            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
            //            '</li>');
            //     });
            // }

        },
        error: function(){
            console.log("error");
        }
});

    // ajax


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
