    /*function followUs(){
        $("i.fa-crow").addClass("animated bounce");
        $("a.follow-us").addClass("animated jello");
    };*/

    function followUsBtn(){
        $("i.fa-crow").addClass("animated bounce");
        $("div.follow-us-btn").addClass("animated jello");
    };
    //function joinUs(){
        //    $("h2").addClass("animated headShake");
        //};  
function JewelryAccessories(){
    $("h2.welcome").addClass("animated fadeInLeft");
};
function JewelryAccessoriesHide(){
    $("h2.welcome").css('opacity','0');
};
function JewelryAccessoriesShow(){
    $("h2.welcome").css('opacity','1');
};

function JewelryAccessoriesFadeIn(){
    $("h2.home").fadeIn(1000);
};
        
function imgAnimation(){
    $("img.main-pic-welcome").fadeIn(5000);
};


function registerTextFadeIn(){
    $("h2.register").addClass("animated fadeInLeft");
};
function registerTextHide(){
    $("h2.register").css('opacity','0');
};

$(JewelryAccessoriesHide());
setTimeout(followUsBtn, 5000);
setTimeout(JewelryAccessoriesShow, 3000);
setTimeout(JewelryAccessories, 3000);
setTimeout(imgAnimation, 500);
setTimeout(JewelryAccessoriesFadeIn, 500);

$(registerTextHide());
setTimeout(registerTextFadeIn, 200);






setInterval(changeCrowColor, 15000); // Every two seconds

function changeCrowColor() {
    $('i.fa-crow').css('color', 'skyblue'); // Change colour
    setTimeout(function() {
        $('i.fa-crow').css('color', 'lightsalmon'); // Change back
            setTimeout(function() {
                $('i.fa-crow').css('color', 'white'); // Change back
            }, 5000);}, 5000);
        };
  