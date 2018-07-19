;(function() {
'use strict';
window.onload = function() {




var show_menu = document.getElementById('show-menu');
var close_menu = document.getElementById('close-menu');
var menu = document.getElementById('menu');

var page_width = document.documentElement.clientWidth || document.documentElement.scrollWidth

console.log(page_width)
if (page_width <= 1080) {
  show_menu.addEventListener('click', function (){menu.classList.add("slider-show");menu.classList.remove("slider-close");})
  close_menu.addEventListener('click', function() {menu.classList.add("slider-close");menu.classList.remove("slider-show");})	
}




$(document).ready(function(){
	var total = $(".product-window").length;
	if (total < 16) {$("#show-more").hide();}
	var startShow = 0;
	var endShow = 16;
	  $(".product-window").slice(endShow).hide();
	  $("#show-more").click(function(){
	  endShow += 8;
	  $(".product-window").slice(0, endShow).slideDown();
	  $(".product-window").slice(endShow).hide();
	})

})







};
})()
