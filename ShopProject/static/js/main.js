// alert(456)
//
// $(document).ready(function () {
//     $(function () {
//         $.scrollUp({
//             scrollName: 'scrollUp', // Element ID
//             scrollDistance: 300, // Distance from top/bottom before showing element (px)
//             scrollFrom: 'top', // 'top' or 'bottom'
//             scrollSpeed: 300, // Speed back to top (ms)
//             easingType: 'linear', // Scroll to top easing (see http://easings.net/)
//             animation: 'fade', // Fade, slide, none
//             animationSpeed: 200, // Animation in speed (ms)
//             scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
//             //scrollTarget: false, // Set a custom target element for scrolling to the top
//             scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
//             scrollTitle: false, // Set a custom <a> title if required.
//             scrollImg: false, // Set true to use image
//             activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
//             zIndex: 2147483647 // Z-Index for the overlay
//         });
//     });
//     alert(123)
//
// });
//
//
// $(function () {
//     $("#price-range").slider({
//         steps: 2,
//         range: true,
//         min: 10, max: 500,
//         values: [10, 500],
//         slide: function (event, ui) {
//             $("#priceRange").val(ui.values[0] + " - " + ui.values[1]);
//             $('#min').val(ui.values[0])
//             $('#max').val(ui.values[1])
//         }
//     });
//     $("#priceRange").val($("#price-range").slider("values", 0) + " - " + $("#price-range").slider("values", 1));
//     $(document).on('click', '.filter', function () {
//         alert('dfsdfh');
//         var n = $('#min').val();
//         const min = $('.filter').attr('min', n);
//         var x = $('#max').val();
//         const max = $('.filter').attr('max', x);
//     });
//     $('body').on('click', '.filter-cat-products', function () {
//         var n = $('#min').val();
//         const min = $('.filter-cat-products').attr('min', n);
//         var x = $('#max').val();
//         const max = $('.filter-cat-products').attr('max', x);
//     });
// });
// $(document).on('click', '.filter', function () {
//     console.log(1111111111111)
//     const min = $(this).attr('min');
//     const max = $(this).attr('max');
//     $.ajax({
//         url: '/ajax_price_range/',
//         data: {min: min,
//                max: max,
//                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
//         },
//         dataType: 'json',
//         type: 'post',
//         success: function (data) {
//             console.log(data)
//             $('.features_items div').remove()
//             $.map(data, function (item) {
//                 $('.features_items').append(
//                     `
//                 <div class="col-sm-4">
//                     <div class="product-image-wrapper">
//                         <div class="single-products">
//                             <div class="productinfo text-center">
//                                 <img src="${item.photo.url}" alt="" style="height: 200px"/>
//                                 <h2>${item.price}</h2>
//                                 <p>${item.title}</p>
//                                 <a href="javascript:;" class="btn btn-default add-to-cart"><i
//                                         class="fa fa-shopping-cart"></i>Add
//                                     to
//                                     cart</a>
//                             </div>
//                             <div class="product-overlay">
//                                 <div class="overlay-content">
//                                     <h2>${item.price}</h2>
//                                     <p>${item.title}</p>
//                                     <form action="{% url 'cart:cart_add' item.id %}" method="post">
//                                         {% csrf_token %}
//                                         <button type="submit" class="btn btn-default add-to-cart">
//                                             <i class="fa fa-shopping-cart"></i>
//                                             Add to cart
//                                         </button>
//                                     </form>
//
//
//                                 </div>
//                             </div>
//                         </div>
//                         <div class="choose">
//                             <ul class="nav nav-pills nav-justified">
//                                 <li><a href="#"><i class="fa fa-plus-square"></i>Add to wishlist</a></li>
//                                 <li><a href="#"><i class="fa fa-plus-square"></i>Add to compare</a></li>
//                             </ul>
//                             <ul style="margin-left: 50px ">
//                                 <li>
//                                     <a href="{% url 'Eshopper:detail_product' item.slug %}">Product Detail </a>
//                                 </li>
//                             </ul>
//                         </div>
//                     </div>
//                 </div>
//                 `
//                 )
//             });
//         },
//     });
// });
