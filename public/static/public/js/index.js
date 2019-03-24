window.ClothingItems = window.ClothingItems || {};

$.ajax({
  url: "/get_clothing/"
}).done(function(data) {
  window.ClothingItems = {
    tops: data.tops,
    bottoms: data.bottoms,
    shoes: data.shoes
  }
}).fail(function() {
  console.error("Error getting ClothingItems")
});

$('.carousel').carousel({
    interval: false
});

document.querySelectorAll(".arrow-right").forEach(function (element) {
    element.addEventListener("click", function (event) {
        console.log(this.dataset.target);
        var carousel = document.getElementById(this.dataset.target);
        $(carousel).carousel('next');
    })
});

document.querySelectorAll(".arrow-left").forEach(function (element) {
    element.addEventListener("click", function (event) {
        console.log(this.dataset.target);
        var carousel = document.getElementById(this.dataset.target);
        $(carousel).carousel('prev');
    })
});

document.querySelectorAll(".swipeable").forEach(function (element) {
    element.addEventListener("touchstart", function (event) {
        this.touchStart = (event.touches[0].pageX);
    })
});


document.querySelectorAll(".swipeable").forEach(function (element) {
    element.addEventListener("touchend", function (event) {
        var moved = this.touchStart - event.changedTouches[0].pageX;
        if (moved < 0) { //swipe left to right
            $(this.querySelector(".carousel")).carousel("prev");
        }
        else if (moved > 0) { //swipe right to left
            $(this.querySelector(".carousel")).carousel("next");
        }
    })
});
