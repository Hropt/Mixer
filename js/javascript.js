var position = 0;
var onLoad = 1;
var curPos = 0;
var prevPos = null;

chosen_drink = {
    drink: 0,
    size: 0,
}

drink_menu = {
    "1": "Gin & Tonic",
    "2": "Jack & Coke",
    "3": "Jaegerbomb",
    "11": "Small",
    "12": "Medium",
    "13": "large",
}

function init() {
    setDot();
    document.getElementById("box1button").disabled = true;
    document.getElementById("box2button").disabled = true;
    document.getElementById("box1button").style.color = "#858585";
    document.getElementById("box2button").style.color = "#858585";
}


function selectDrink(id) {
    console.log("clicked drink" + id);
    chosen_drink.drink = id;
    document.getElementById("1").style.color = "#858585";
    document.getElementById("1").style.borderLeft = "10px solid #858585";
    document.getElementById("2").style.color = "#858585";
    document.getElementById("2").style.borderLeft = "10px solid #858585";
    document.getElementById("3").style.color = "#858585";
    document.getElementById("3").style.borderLeft = "10px solid #858585";
    document.getElementById(id).style.color = "#F50057";
    document.getElementById(id).style.borderLeft = "10px solid #F50057";

    document.getElementById("box1button").disabled = false;
    document.getElementById("box1button").style.color = "#F50057";
    document.getElementById("selectedDrink").textContent = "Drink: " + drink_menu[chosen_drink.drink];

}

function selectSize(id) {
    console.log("clicked size" + id);
    chosen_drink.size = id;
    document.getElementById("11").style.color = "#858585";
    document.getElementById("11").style.borderLeft = "10px solid #858585";
    document.getElementById("12").style.color = "#858585";
    document.getElementById("12").style.borderLeft = "10px solid #858585";
    document.getElementById("13").style.color = "#858585";
    document.getElementById("13").style.borderLeft = "10px solid #858585";
    document.getElementById(id).style.color = "#F50057";
    document.getElementById(id).style.borderLeft = "10px solid #F50057";

    document.getElementById("box2button").disabled = false;
    document.getElementById("box2button").style.color = "#F50057";
    document.getElementById("selectedSize").textContent = "Size: " + drink_menu[chosen_drink.size];
}


function slideLeft() {
  var speed = 1100,
  direction = 1,
  boxElement = document.getElementById('hscroll-wrap');

    if (position > 0) {
      var boxLeftPos = boxElement.offsetLeft,
          boxRightPos = boxLeftPos + boxElement.offsetWidth;

          // sets new position
      boxElement.style.left = (boxLeftPos + speed * direction) + 'px';
      prevPos = position;
      position = position - 1;
      curPos = position;
      setDot();
    }

}

//Needs to disable fast clicking (sync up with animation)
function slideRight() {


  var speed = 1100, //Sets how far the div moves
  direction = -1,  //Sets direction
  boxElement = document.getElementById('hscroll-wrap');

    if (position < 3 ) {
    var boxLeftPos = boxElement.offsetLeft,
        boxRightPos = boxLeftPos + boxElement.offsetWidth;

    // Recalculates position:
    boxElement.style.left = (boxLeftPos + speed * direction) + 'px';

    prevPos = position;
    position = position + 1;
    curPos = position;

    setDot();
  }

}


//Sets the dot indicating which textbox you are viewing
function setDot() {
    var dot1 = document.getElementById("dot1");
    var dot2 = document.getElementById("dot2");
    var dot3 = document.getElementById("dot3");
    var dot4 = document.getElementById("dot4");
    var dot5 = document.getElementById("dot5");
    var dots = [dot1, dot2, dot3, dot4, dot5];

    var activate = dots[curPos];
    var deactivate = dots[prevPos];

    if (onLoad == 1) {
      activate.classList.toggle("is-active");
      onLoad = 0;
    } else {
      deactivate.classList.toggle("is-active");
      activate.classList.toggle("is-active");
    }
}
