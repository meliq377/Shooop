// alert(123)
//
// $(document).ready(function(){
// 	$(function () {
// 		$.scrollUp({
// 	        scrollName: 'scrollUp', // Element ID
// 	        scrollDistance: 300, // Distance from top/bottom before showing element (px)
// 	        scrollFrom: 'top', // 'top' or 'bottom'
// 	        scrollSpeed: 300, // Speed back to top (ms)
// 	        easingType: 'linear', // Scroll to top easing (see http://easings.net/)
// 	        animation: 'fade', // Fade, slide, none
// 	        animationSpeed: 200, // Animation in speed (ms)
// 	        scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
// 					//scrollTarget: false, // Set a custom target element for scrolling to the top
// 	        scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
// 	        scrollTitle: false, // Set a custom <a> title if required.
// 	        scrollImg: false, // Set true to use image
// 	        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
// 	        zIndex: 2147483647 // Z-Index for the overlay
// 		});
// 	});
// });
// alert(23234)
//
//
//
// $(function () {
//         $("#price-range").slider({
//             steps: 2,
//             range: true,
//             min: 10, max: 500,
//             values: [10, 500],
//             slide: function (event, ui) {
//                 $("#priceRange").val(ui.values[0] + " - " + ui.values[1]);
//                 $('#min').val(ui.values[0])
//                 $('#max').val(ui.values[1])
//             }
//         });
//         $("#priceRange").val($("#price-range").slider("values", 0) + " - " + $("#price-range").slider("values", 1));
//         $(document).on('click', '.filter', function () {
// 			var n = $('#min').val();
//             const min = $('.filter').attr('min', n);
//             var x = $('#max').val();
//             const max = $('.filter').attr('max', x);
//         });
//     });
//
