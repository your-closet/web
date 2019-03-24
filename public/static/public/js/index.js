window.ClothingItems = window.ClothingItems || {};

$.ajax({
    url: "/get_clothing/"
}).done(function (data) {
    window.ClothingItems = {
        tops: data.tops,
        bottoms: data.bottoms,
        shoes: data.shoes
    }
    const shirtDiv = document.querySelector("#shirtCarousel .carousel-inner");
    const pantsDiv = document.querySelector("#pantsCarousel .carousel-inner")
    window.ClothingItems.tops.forEach(function (clothing) {
        var cImg = document.createElement("img");
        cImg.src = "/media/" + clothing.image;
        cImg.style.margin = "auto";
        var cImgHolder = document.createElement("div")
        cImgHolder.appendChild(cImg);
        cImgHolder.classList.add("carousel-item","text-center");
        shirtDiv.appendChild(cImgHolder);
    });
    window.ClothingItems.bottoms.forEach(function (clothing) {
        var cImg = document.createElement("img");
        cImg.src = "/media/" + clothing.image;
        cImg.style.margin = "auto";
        var cImgHolder = document.createElement("div")
        cImgHolder.appendChild(cImg);
        cImgHolder.classList.add("carousel-item","text-center");
        pantsDiv.appendChild(cImgHolder);
    });
    resizeImg();
}).fail(function () {
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

document.querySelectorAll(".swipeable").forEach(function (element) {
    console.log(element);
    element.style.height = document.querySelector(".shirt").getBoundingClientRect().height + "px";
    console.log(element.style.height);
});

function resizeImg() {
    document.querySelectorAll(".swipeable img").forEach(function (element) {
        console.log(element);
        element.style.height = document.querySelector(".shirt").getBoundingClientRect().height + "px";
        console.log(element.style.height);
    });
}