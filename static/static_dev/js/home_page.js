function JewelryAccessoriesFadeIn(){
    $("h2.home").fadeIn(5000);
};
        
/*function imgAnimation(){
    $("img.main-pic").fadeIn(5000);
};*/

//setTimeout(followUs, 5000);
//setTimeout(imgAnimation, 500);



function changeCrowColor() {
    $('i.fa-crow').css('color', 'skyblue'); // Change colour
    setTimeout(function() {
        $('i.fa-crow').css('color', 'lightsalmon'); // Change back
            setTimeout(function() {
                $('i.fa-crow').css('color', 'white'); // Change back
            }, 5000);}, 5000);
        };
 


function followUs(){
    $("i.fa-crow").addClass("animated jello");
    $("a.follow-us-a").addClass("animated headShake");
    setTimeout(function(){
        $("i.fa-crow").removeClass("animated jello");
        $("a.follow-us-a").removeClass("animated headShake");
        }, 500);
    };

function followUsBtn(){
    $("div.follow-us-btn").addClass("animated headShake");

    setTimeout(function(){
        $("div.follow-us-btn").removeClass("animated headShake");
        }, 500);
    };

    $(function(){
        $(".carousel").mouseover(function(){
            $(this).carousel('cycle');
        });
    });

    $(function(){
        $(".carousel").mouseout(function(){
            $(".carousel").carousel('pause');
        });
    });

    $(function(){
        $("div.product-item").mouseover(function(){
            $(this).css('border','1px solid lightsalmon');
        });
    });

    $(function(){
        $("div.product-item").mouseout(function(){
            $(this).css('border','1px solid lightgray');
        });
    });
    
        
      
setTimeout(JewelryAccessoriesFadeIn, 500);
setTimeout(followUsBtn,5000);
setTimeout(followUs,5000);
setInterval(changeCrowColor, 15000); // Every 15 seconds
setInterval(followUsBtn, 20000);
setInterval(followUs, 20000); // Every 15 seconds
 // Every 15 seconds