var stars;
var stars2;
var stars3;
document.addEventListener('DOMContentLoaded', () => {
stars = document.querySelectorAll(".grid-rankCmf span");
stars2 = document.querySelectorAll(".grid-rankAT span");
stars3 = document.querySelectorAll(".grid-rankCom span");

stars.forEach(item => {
	item.addEventListener('click', function () {
		var rating = this.getAttribute("data-rating");
		return SetRatingStar(rating, stars);
	});
});
stars2.forEach(item => {
        item.addEventListener('click', function () {
        var rating = this.getAttribute("data-rating");
        return SetRatingStar(rating, stars2);
    });
});
stars3.forEach(item => {
        item.addEventListener('click', function () {
        var rating = this.getAttribute("data-rating");
        return SetRatingStar(rating, stars3);
    });
});
});

function SetRatingStar(rating, stars) {
var len = stars.length;
console.log(rating);

for (var i = 0; i < len; i++) {
	if (i < rating) {
		stars[i].innerHTML = '<i class="fas fa-star"></i>';
	} else {
		stars[i].innerHTML = '<i class="far fa-star"></i>';
	}
}

};
