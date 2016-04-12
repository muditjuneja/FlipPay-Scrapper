from bs4 import BeautifulSoup
from .models import Item, Order



flipkart_str = """
<div class="fk-inf-scroll-item order physical collapsed">
<div class="line order-collapsed fk-hidden">
<div class="unit size1of5">
<strong>OD203339050476421300</strong>
</div>
<div class="unit size3of5 smallText">
TerraVulc Walking Shoes (Total: 1 item)
</div>
<div class="unit size1of6">
<span class="smallText">Order Total:</span> <strong>Rs.339</strong>
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Show order details'></a>
</div>
</div>
<div class="line order-expanded">
<div class="unit size1of4">
<a class="orderIdBtn btn btn-medium btn-blue" target="_blank" href="/order_details?order_id=OD203339050476421300&src=od&link=order_number">OD203339050476421300</a>
</div>
<div class="unit size3of5">
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Hide order details'></a>
</div>
</div>
<div class="line js-order-details fk-hidden">
<div class="line order-item ">
<div class="line order-item-inner">
<div class="unit size1of8 fk-text-center product-image">
<a href="http://www.flipkart.com/terravulc-walking-shoes/p/itme4agykrdq7rmx?pid=SHOE4AGXUKN3GSN7" target="__blank">
<img class="item-image" onerror="img_onerror(this);" data-error-url="https://img1.flixcart.com/img/thumb-default.jpg" src="https://img1.flixcart.com/img/thumb-default.jpg" onload="lzld(this);" data-src="https://img1a.flixcart.com/image/shoe/5/y/r/navy-red-ss151001-terravulc-10-75x75-imae4mhfyzqcbkgp.jpeg" title="TerraVulc Walking Shoes" alt="TerraVulc Walking Shoes">
</a>
</div>
<div class="unit size2of7">
<a target="_blank" href="http://www.flipkart.com/terravulc-walking-shoes/p/itme4agykrdq7rmx?pid=SHOE4AGXUKN3GSN7">
TerraVulc Walking Shoes </a>
<p class="smallText tmargin10">
Color: Navy, Red &nbsp; Size: 7 &nbsp; Qty: 1 </p>
</div>
<div class="unit size1of6">
<div class="lpadding10">
Rs. 339 <p class="tmargin10 fk-font-small">
<span class="offers">OFFERS:</span> 2 </p>
</div>

</div>
<div class="unit size2of7">
<p class="greyText bmargin10">
Delivered on Wed, 15th Jul'15 </p>

</div>
<div class="lastUnit text_right">
</div>
</div>

</div>
<div class="line order-total">
<div class="line">
<div class="unit size2of5">
<span class="smallText">Seller:</span> <span class="rmargin20">WS Retail</span>
<span class="smallText fk-inline-block">Date:</span> Fri, 10th Jul'15 </div>
<div class="lastUnit text_right">
<span class="smallText">Order Total:</span> <strong>Rs.339</strong>
</div>
</div>
</div>
</div>
</div>
<div class="fk-inf-scroll-item order physical collapsed">
<div class="line order-collapsed fk-hidden">
<div class="unit size1of5">
<strong>OD103331807459757300</strong>
</div>
<div class="unit size3of5 smallText">
Amore Anime Girl Vinyl Laptop Decal (Total: 1 item)
</div>
<div class="unit size1of6">
<span class="smallText">Order Total:</span> <strong>Rs.199</strong>
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Show order details'></a>
</div>
</div>
<div class="line order-expanded">
<div class="unit size1of4">
<a class="orderIdBtn btn btn-medium btn-blue" target="_blank" href="/order_details?order_id=OD103331807459757300&src=od&link=order_number">OD103331807459757300</a>
</div>
<div class="unit size3of5">
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Hide order details'></a>
</div>
</div>
<div class="line js-order-details fk-hidden">
<div class="line order-item ">
<div class="line order-item-inner">
<div class="unit size1of8 fk-text-center product-image">
<a href="http://www.flipkart.com/amore-anime-girl-vinyl-laptop-decal/p/itmdzqzf6kbsvtkp?pid=LSDDZQZFMHHHGXW9" target="__blank">
<img class="item-image" onerror="img_onerror(this);" data-error-url="https://img1.flixcart.com/img/thumb-default.jpg" src="https://img1.flixcart.com/img/thumb-default.jpg" onload="lzld(this);" data-src="https://img1a.flixcart.com/image/laptop-skin-decal/x/w/9/15-6-amore-anime-girl-75x75-imadzqzzuxqdgtpx.jpeg" title="Amore Anime Girl Vinyl Laptop Decal" alt="Amore Anime Girl Vinyl Laptop Decal">
</a>
</div>
<div class="unit size2of7">
<a target="_blank" href="http://www.flipkart.com/amore-anime-girl-vinyl-laptop-decal/p/itmdzqzf6kbsvtkp?pid=LSDDZQZFMHHHGXW9">
Amore Anime Girl Vinyl Laptop Decal </a>
<p class="smallText tmargin10">
Qty: 1 </p>
</div>
<div class="unit size1of6">
<div class="lpadding10">
Rs. 199 <p class="tmargin10 fk-font-small">
<span class="offers">OFFERS:</span> 1 </p>
</div>

</div>
<div class="unit size2of7">
<p class="greyText bmargin10">
Delivered on Mon, 20th Jul'15 </p>

</div>
<div class="lastUnit text_right">
</div>
</div>

</div>
<div class="line order-total">
<div class="line">
<div class="unit size2of5">
<span class="smallText">Seller:</span> <span class="rmargin20">Amore</span>
<span class="smallText fk-inline-block">Date:</span> Thu, 9th Jul'15 </div>
<div class="lastUnit text_right">
<span class="smallText">Order Total:</span> <strong>Rs.199</strong>
</div>
</div>
</div>
</div>
</div>
<div class="fk-inf-scroll-item order physical collapsed">
<div class="line order-collapsed fk-hidden">
<div class="unit size1of5">
<strong>OD202035026152242400</strong>
</div>
<div class="unit size3of5 smallText">
Select Grey Sporty Walking Shoes (Total: 1 item)
</div>
<div class="unit size1of6">
<span class="smallText">Order Total:</span> <strong>Rs.549</strong>
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Show order details'></a>
</div>
</div>
<div class="line order-expanded">
<div class="unit size1of4">
<a class="orderIdBtn btn btn-medium btn-blue" target="_blank" href="/order_details?order_id=OD202035026152242400&src=od&link=order_number">OD202035026152242400</a>
</div>
<div class="unit size3of5">
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Hide order details'></a>
</div>
</div>
<div class="line js-order-details fk-hidden">
<div class="line order-item ">
<div class="line order-item-inner">
<div class="unit size1of8 fk-text-center product-image">
<a href="http://www.flipkart.com/select-grey-sporty-walking-shoes/p/itmefg9zzvhkeggg?pid=SHOEFG9ZZCHGKPAC" target="__blank">
<img class="item-image" onerror="img_onerror(this);" data-error-url="https://img1.flixcart.com/img/thumb-default.jpg" src="https://img1.flixcart.com/img/thumb-default.jpg" onload="lzld(this);" data-src="https://img1a.flixcart.com/image/shoe/x/z/h/grey-gsb-s-3-select-35-75x75-imaefezgc9rpsz9d.jpeg" title="Select Grey Sporty Walking Shoes" alt="Select Grey Sporty Walking Shoes">
</a>
</div>
<div class="unit size2of7">
<a target="_blank" href="http://www.flipkart.com/select-grey-sporty-walking-shoes/p/itmefg9zzvhkeggg?pid=SHOEFG9ZZCHGKPAC">
Select Grey Sporty Walking Shoes </a>
<p class="smallText tmargin10">
Color: Grey &nbsp; Size: 40 &nbsp; Qty: 1 </p>
</div>
<div class="unit size1of6">
<div class="lpadding10">
Rs. 549 </div>

</div>
<div class="unit size2of7">
<p class="greyText bmargin10">
Delivered on Wed, 18th Feb'15 </p>

</div>
<div class="lastUnit text_right">
</div>
</div>

</div>
<div class="line order-total">
<div class="line">
<div class="unit size2of5">
<span class="smallText">Seller:</span> <span class="rmargin20">GOGIASALES</span>
<span class="smallText fk-inline-block">Date:</span> Mon, 9th Feb'15 </div>
<div class="lastUnit text_right">
<span class="smallText">Order Total:</span> <strong>Rs.549</strong>
</div>
</div>
</div>
</div>
</div>
<div class="fk-inf-scroll-item order physical collapsed">
<div class="line order-collapsed fk-hidden">
<div class="unit size1of5">
<strong>OD30711043907</strong>
</div>
<div class="unit size3of5 smallText">
Yepme Printed Women's Tunic (Size: XL), Mumbai Slang Printed Women'... (Total: 4 items)
</div>
<div class="unit size1of6">
<span class="smallText">Order Total:</span> <strong>Rs.1407</strong>
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Show order details'></a>
</div>
</div>
<div class="line order-expanded">
<div class="unit size1of4">
<a class="orderIdBtn btn btn-medium btn-blue" target="_blank" href="/order_details?order_id=OD30711043907&src=od&link=order_number">OD30711043907</a>
</div>
<div class="unit size3of5">
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Hide order details'></a>
</div>
</div>
<div class="line js-order-details fk-hidden">
<div class="line order-item ">
<div class="line order-item-inner">
<div class="unit size1of8 fk-text-center product-image">
<a href="http://www.flipkart.com/yepme-printed-women-s-tunic/p/itmdk99f89ycyhrm?pid=TUNDK97K8ZW34MWR" target="__blank">
<img class="item-image" onerror="img_onerror(this);" data-error-url="https://img1.flixcart.com/img/thumb-default.jpg" src="https://img1.flixcart.com/img/thumb-default.jpg" onload="lzld(this);" data-src="https://img1a.flixcart.com/image/tunic/m/w/r/ypmkurt0056-yepme-s-75x75-imadhzh7gacenttp.jpeg" title="Yepme Printed Women's Tunic (Size: XL)" alt="Yepme Printed Women's Tunic (Size: XL)">
</a>
</div>
<div class="unit size2of7">
<a target="_blank" href="http://www.flipkart.com/yepme-printed-women-s-tunic/p/itmdk99f89ycyhrm?pid=TUNDK97K8ZW34MWR">
Yepme Printed Women's Tunic (Size: XL) </a>
<p class="smallText tmargin10">
Color: Orange &nbsp; Size: XL &nbsp; Qty: 1 </p>
</div>
<div class="unit size1of6">
<div class="lpadding10">
Rs. 414 <p class="tmargin10 fk-font-small">
<span class="offers">OFFERS:</span> 1 </p>
</div>

</div>
<div class="unit size2of7">
<p class="greyText bmargin10">
Delivered on Mon, 15th Jul'13 </p>

</div>
<div class="lastUnit text_right">
</div>
</div>

</div>
<div class="line order-item ">
<div class="line order-item-inner">
<div class="unit size1of8 fk-text-center product-image">
<a href="http://www.flipkart.com/mumbai-slang-printed-women-s-tunic/p/itmdh5dmceqz3pjj?pid=TUNDH5DHSHH4Y6VC" target="__blank">
<img class="item-image" onerror="img_onerror(this);" data-error-url="https://img1.flixcart.com/img/thumb-default.jpg" src="https://img1.flixcart.com/img/thumb-default.jpg" onload="lzld(this);" data-src="https://img1a.flixcart.com/image/tunic/6/v/c/mgtn000020-mumbai-slang-m-75x75-imadm66hyqyrvkcm.jpeg" title="Mumbai Slang Printed Women's Tunic (Size: XL)" alt="Mumbai Slang Printed Women's Tunic (Size: XL)">
</a>
</div>
<div class="unit size2of7">
<a target="_blank" href="http://www.flipkart.com/mumbai-slang-printed-women-s-tunic/p/itmdh5dmceqz3pjj?pid=TUNDH5DHSHH4Y6VC">
Mumbai Slang Printed Women's Tunic (S... </a>
<p class="smallText tmargin10">
Color: Green, Grey &nbsp; Size: XL &nbsp; Qty: 1 </p>
</div>
<div class="unit size1of6">
<div class="lpadding10">
Rs. 475 <p class="tmargin10 fk-font-small">
<span class="offers">OFFERS:</span> 1 </p>
</div>

</div>
<div class="unit size2of7">
<p class="greyText bmargin10">
Delivered on Mon, 15th Jul'13 </p>

</div>
<div class="lastUnit text_right">
</div>
</div>

</div>
<div class="line order-item ">
<div class="line order-item-inner">
<div class="unit size1of8 fk-text-center product-image">
<a href="http://www.flipkart.com/fruit-loom-casual-sleeveless-solid-women-s-top/p/itmdmwhcyz6hhxnt?pid=TOPDK2JTZZJJKGSB" target="__blank">
<img class="item-image" onerror="img_onerror(this);" data-error-url="https://img1.flixcart.com/img/thumb-default.jpg" src="https://img1.flixcart.com/img/thumb-default.jpg" onload="lzld(this);" data-src="https://img1a.flixcart.com/image/top/y/6/2/2001-pinkz-fruit-of-the-loom-s-75x75-imadhstcfyqqnvvz.jpeg" title="Fruit of the Loom Solid Women's Top (Size: XL)" alt="Fruit of the Loom Solid Women's Top (Size: XL)">
</a>
</div>
<div class="unit size2of7">
<a target="_blank" href="http://www.flipkart.com/fruit-loom-casual-sleeveless-solid-women-s-top/p/itmdmwhcyz6hhxnt?pid=TOPDK2JTZZJJKGSB">
Fruit of the Loom Solid Women's Top (... </a>
<p class="smallText tmargin10">
Color: Pink &nbsp; Size: XL &nbsp; Qty: 1 </p>
</div>
<div class="unit size1of6">
<div class="lpadding10">
Rs. 236 <p class="tmargin10 fk-font-small">
<span class="offers">OFFERS:</span> 1 </p>
</div>

</div>
<div class="unit size2of7">
<p class="greyText bmargin10">
Delivered on Mon, 15th Jul'13 </p>

</div>
<div class="lastUnit text_right">
</div>
</div>

</div>
<div class="line order-item ">
<div class="line order-item-inner">
<div class="unit size1of8 fk-text-center product-image">
<a href="http://www.flipkart.com/baggit-m-dulhan-jimjim-mobile-pouch/p/itmdjg8ynxadmawv?pid=PPSDJG8YWCT7GAFV" target="__blank">
<img class="item-image" onerror="img_onerror(this);" data-error-url="https://img1.flixcart.com/img/thumb-default.jpg" src="https://img1.flixcart.com/img/thumb-default.jpg" onload="lzld(this);" data-src="https://img1a.flixcart.com/image/pouch-potli/a/f/v/2177920347220-baggit-mobile-pouch-m-dulhan-jimjim-75x75-imadjjj9juf8z6yx.jpeg" title="Baggit M Dulhan Jimjim Mobile Pouch (Black)" alt="Baggit M Dulhan Jimjim Mobile Pouch (Black)">
</a>
</div>
<div class="unit size2of7">
<a target="_blank" href="http://www.flipkart.com/baggit-m-dulhan-jimjim-mobile-pouch/p/itmdjg8ynxadmawv?pid=PPSDJG8YWCT7GAFV">
Baggit M Dulhan Jimjim Mobile Pouch (... </a>
<p class="smallText tmargin10">
Color: Black &nbsp; Qty: 1 </p>
</div>
<div class="unit size1of6">
<div class="lpadding10">
Rs. 282 </div>

</div>
<div class="unit size2of7">
<p class="greyText bmargin10">
Delivered on Mon, 15th Jul'13 </p>

</div>
<div class="lastUnit text_right">
</div>
</div>

</div>
<div class="line order-total">
<div class="line">
<div class="unit size2of5">
<span class="smallText">Seller:</span> <span class="rmargin20">WS Retail</span>
<span class="smallText fk-inline-block">Date:</span> Thu, 11th Jul'13 </div>
<div class="lastUnit text_right">
<span class="smallText">Order Total:</span> <strong>Rs.1407</strong>
</div>
</div>
</div>
</div>
</div>
<div class="fk-inf-scroll-item order physical collapsed">
<div class="line order-collapsed fk-hidden">
<div class="unit size1of5">
<strong>OD21216180870</strong>
</div>
<div class="unit size3of5 smallText">
Engineering Mechanics - S.S. Bhavikatti (Total: 1 item)
</div>
<div class="unit size1of6">
<span class="smallText">Order Total:</span> <strong>Rs.299</strong>
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Show order details'></a>
</div>
</div>
<div class="line order-expanded">
<div class="unit size1of4">
<a class="orderIdBtn btn btn-medium btn-blue" target="_blank" href="/order_details?order_id=OD21216180870&src=od&link=order_number">OD21216180870</a>
</div>
<div class="unit size3of5">
</div>
<div class="lastUnit text_right">
<a class="toggle-details" title='Hide order details'></a>
</div>
</div>
<div class="line js-order-details fk-hidden">
<div class="line order-item ">
<div class="line order-item-inner">
<div class="unit size1of8 fk-text-center product-image">
<a href="http://www.flipkart.com/engineering-mechanics-english-4th/p/itmeyf5t2gbspxym?pid=9788122433739" target="__blank">
<img class="item-image" onerror="img_onerror(this);" data-error-url="https://img1.flixcart.com/img/thumb-default.jpg" src="https://img1.flixcart.com/img/thumb-default.jpg" onload="lzld(this);" data-src="https://img1a.flixcart.com/image/book/7/3/9/engineering-mechanics-75x75-imadh9vfsufhqhvp.jpeg" title="Engineering Mechanics - S.S. Bhavikatti" alt="Engineering Mechanics - S.S. Bhavikatti">
</a>
</div>
<div class="unit size2of7">
<a target="_blank" href="http://www.flipkart.com/engineering-mechanics-english-4th/p/itmeyf5t2gbspxym?pid=9788122433739">
Engineering Mechanics - S.S. Bhavikatti </a>
<p class="smallText tmargin10">S S Bhavikatti</p>
<p class="smallText tmargin10">
Qty: 1 </p>
</div>
<div class="unit size1of6">
<div class="lpadding10">
Rs. 269 </div>

</div>
<div class="unit size2of7">
<p class="greyText bmargin10">
Delivered on Thu, 20th Dec'12 </p>

</div>
<div class="lastUnit text_right">
</div>
</div>

</div>
<div class="line order-total">
<div class="line">
<div class="unit size2of5">
<span class="smallText">Seller:</span> <span class="rmargin20">WS Retail</span>
<span class="smallText fk-inline-block">Date:</span> Sun, 16th Dec'12 </div>
<div class="lastUnit text_right">
<span class="smallText">Order Total:</span> <strong>Rs.299</strong>
</div>
</div>
</div>
</div>
</div>
<script type="text/javascript+fk-onload">
FKART && FKART.OrderCancel && FKART.OrderCancel.showDisabledReason();
</script>
"""

#html for Jabong!

html_jabong = '''
<section class="order-dashboard-block"><div class="order-dashboard-header clearfix"><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 order-id-block"><h4 class="text-uppercase">order id <span>160213009170155</span></h4><p class="order-placed">Placed on <span>Sat, 13th Feb&#39;16 at 5:45am</span></p><p class="order-amount">Total amount:<span class="standard-price">495.75</span></p></div><div class="col-sm-4 col-md-3 col-lg-3 col-xs-4 col-xxs-12 text-right order-btn-block"><a href="/customer/order/view/160213009170155" class="order btn btn-primary btn-small" data-gaq-event="track order~$~view order~$~160213009170155">order details</a> </div></div><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">London Bridge</h5><h5 class="desc"><a href="/london-bridge-Black-Slim-Fit-Casual-Shirt-1533920.html" target="_blank">Black Slim Fit Casual Shirt</a></h5></div><div class="media"><span class="media-left media-top"><a href="/london-bridge-Black-Slim-Fit-Casual-Shirt-1533920.html" target="_blank"><img src="http://static.jabong.com/p/London-Bridge-Black-Slim-Fit-Casual-Shirt-0731-0293351-1-new_cart.jpg" alt="160213009170155"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">40</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase  delivered  '>Delivered</h5><p>on Mon, 22 Feb 2016</p></div></div></div></div>        <div class="col-md-3 col-sm-4 col-xs-4 col-lg-3 text-right notice-block">               <a href="/customer/order/return?order_nr=160213009170155" class="btn btn-default btn-sm text-uppercase  btn-small">return</a> </div>  </section></section><section class="order-dashboard-block"><div class="order-dashboard-header clearfix"><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 order-id-block"><h4 class="text-uppercase">order id <span>160211718245035</span></h4><p class="order-placed">Placed on <span>Thu, 11th Feb&#39;16 at 1:27am</span></p><p class="order-amount">Total amount:<span class="standard-price">541.80</span></p></div><div class="col-sm-4 col-md-3 col-lg-3 col-xs-4 col-xxs-12 text-right order-btn-block"><a href="/customer/order/view/160211718245035" class="order btn btn-primary btn-small" data-gaq-event="track order~$~view order~$~160211718245035">order details</a> </div></div><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">Newport</h5><h5 class="desc"><a href="/newport-Blue-Low-Rise-Slim-Fit-Jeans-1816970.html" target="_blank">Blue Low Rise Slim Fit Jeans</a></h5></div><div class="media"><span class="media-left media-top"><a href="/newport-Blue-Low-Rise-Slim-Fit-Jeans-1816970.html" target="_blank"><img src="http://static.jabong.com/p/Newport-Blue-Low-Rise-Slim-Fit-Jeans-4694-0796181-1-new_cart.jpg" alt="160211718245035"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">36</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase  delivered  '>Delivered</h5><p>on Thu, 18 Feb 2016</p></div></div></div></div>        <div class="col-md-3 col-sm-4 col-xs-4 col-lg-3 text-right notice-block">               <a href="/customer/order/return?order_nr=160211718245035" class="btn btn-default btn-sm text-uppercase  btn-small">return</a> </div>  </section></section><section class="order-dashboard-block"><div class="order-dashboard-header clearfix"><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 order-id-block"><h4 class="text-uppercase">order id <span>160123631987381</span></h4><p class="order-placed">Placed on <span>Sat, 23rd Jan&#39;16 at 11:03pm</span></p><p class="order-amount">Total amount:<span class="standard-price">0.00</span></p></div><div class="col-sm-4 col-md-3 col-lg-3 col-xs-4 col-xxs-12 text-right order-btn-block"><a href="/customer/order/view/160123631987381" class="order btn btn-primary btn-small" data-gaq-event="track order~$~view order~$~160123631987381">order details</a> </div></div><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">Blue Saint</h5><h5 class="desc"><a href="/blue-saint-Blue-Mid-Rise-Slim-Fit-Jeans-1834126.html" target="_blank">Blue Mid Rise Slim Fit Jeans</a></h5></div><div class="media"><span class="media-left media-top"><a href="/blue-saint-Blue-Mid-Rise-Slim-Fit-Jeans-1834126.html" target="_blank"><img src="http://static.jabong.com/p/Blue-Saint-Blue-Mid-Rise-Slim-Fit-Jeans-5105-6214381-1-new_cart.jpg" alt="160123631987381"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">36</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase  delivered  '>Delivered</h5><p>on Mon, 25 Jan 2016</p></div></div></div></div> <div class="col-md-3 col-sm-4 col-xs-4 col-lg-3 text-right notice-block">                                      <p>You cannot return or exchange this Order as returns/Exchange period has expired.</p>               </div>         </section></section><section class="order-dashboard-block"><div class="order-dashboard-header clearfix"><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 order-id-block"><h4 class="text-uppercase">order id <span>160116550358149</span></h4><p class="order-placed">Placed on <span>Sat, 16th Jan&#39;16 at 8:47pm</span></p><p class="order-amount">Total amount:<span class="standard-price">1405.95</span></p></div><div class="col-sm-4 col-md-3 col-lg-3 col-xs-4 col-xxs-12 text-right order-btn-block"><a href="/customer/order/view/160116550358149" class="order btn btn-primary btn-small" data-gaq-event="track order~$~view order~$~160116550358149">order details</a> </div></div><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">Blue Saint</h5><h5 class="desc"><a href="/blue-saint-Black-Mid-Rise-Slim-Fit-Jeans-1686174.html" target="_blank">Black Mid Rise Slim Fit Jeans</a></h5></div><div class="media"><span class="media-left media-top"><a href="/blue-saint-Black-Mid-Rise-Slim-Fit-Jeans-1686174.html" target="_blank"><img src="http://static.jabong.com/p/Blue-Saint-Black-Mid-Rise-Slim-Fit-Jeans-6119-4716861-1-new_cart.jpg" alt="160116550358149"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">36</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase '>Refund Initiated</h5><p></p></div></div></div></div><div class="col-sm-4 col-md-3 col-lg-3 col-xs-4 col-xxs-12 text-right notice-block"><a class="btn btn-secondary btn-small track-item" data-target="#track-items" data-order-number="160116550358149" data-sku="BL131MA25YIWINDFAS-5442553" data-size='modal-lg' data-url="/customer/order/track/160116550358149"data-gaq-event="Track Order~$~Track Item~$~BL131MA25YIWINDFAS-5442553">track item</a></div>   </section><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">Dais</h5><h5 class="desc"><a href="/dais-Blue-Mid-Rise-Slim-Fit-Jeans-1807166.html" target="_blank">Blue Mid Rise Slim Fit Jeans</a></h5></div><div class="media"><span class="media-left media-top"><a href="/dais-Blue-Mid-Rise-Slim-Fit-Jeans-1807166.html" target="_blank"><img src="http://static.jabong.com/p/Dais-Blue-Mid-Rise-Slim-Fit-Jeans-5802-6617081-1-new_cart.jpg" alt="160116550358149"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">36</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase '>Refund Initiated</h5><p></p></div></div></div></div><div class="col-sm-4 col-md-3 col-lg-3 col-xs-4 col-xxs-12 text-right notice-block"><a class="btn btn-secondary btn-small track-item" data-target="#track-items" data-order-number="160116550358149" data-sku="DA016MA33VIKINDFAS-5871803" data-size='modal-lg' data-url="/customer/order/track/160116550358149"data-gaq-event="Track Order~$~Track Item~$~DA016MA33VIKINDFAS-5871803">track item</a></div>   </section></section><section class="order-dashboard-block"><div class="order-dashboard-header clearfix"><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 order-id-block"><h4 class="text-uppercase">order id <span>160116529953351</span></h4><p class="order-placed">Placed on <span>Sat, 16th Jan&#39;16 at 8:13pm</span></p><p class="order-amount">Total amount:<span class="standard-price">1352.40</span></p></div><div class="col-sm-4 col-md-3 col-lg-3 col-xs-4 col-xxs-12 text-right order-btn-block"><a href="/customer/order/view/160116529953351" class="order btn btn-primary btn-small" data-gaq-event="track order~$~view order~$~160116529953351">order details</a> </div></div><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">Blue Saint</h5><h5 class="desc"><a href="/blue-saint-Black-Mid-Rise-Slim-Fit-Jeans-1686174.html" target="_blank">Black Mid Rise Slim Fit Jeans</a></h5></div><div class="media"><span class="media-left media-top"><a href="/blue-saint-Black-Mid-Rise-Slim-Fit-Jeans-1686174.html" target="_blank"><img src="http://static.jabong.com/p/Blue-Saint-Black-Mid-Rise-Slim-Fit-Jeans-6119-4716861-1-new_cart.jpg" alt="160116529953351"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">36</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase '>Failed transaction</h5><p></p></div></div></div></div>   </section><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">Phosphorus</h5><h5 class="desc"><a href="/phosphorus-Indigo-Slim-Fit-Jeans-1210845.html" target="_blank">Indigo Slim Fit Jeans</a></h5></div><div class="media"><span class="media-left media-top"><a href="/phosphorus-Indigo-Slim-Fit-Jeans-1210845.html" target="_blank"><img src="http://static.jabong.com/p/Phosphorus-Indigo-Slim-Fit-Jeans-8210-5480121-1-new_cart.jpg" alt="160116529953351"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">36</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase '>Failed transaction</h5><p></p></div></div></div></div>   </section></section><section class="order-dashboard-block"><div class="order-dashboard-header clearfix"><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 order-id-block"><h4 class="text-uppercase">order id <span>151005688688795</span></h4><p class="order-placed">Placed on <span>Mon, 5th Oct&#39;15 at 12:37am</span></p><p class="order-amount">Total amount:<span class="standard-price">1076.25</span></p></div><div class="col-sm-4 col-md-3 col-lg-3 col-xs-4 col-xxs-12 text-right order-btn-block"><a href="/customer/order/view/151005688688795" class="order btn btn-primary btn-small" data-gaq-event="track order~$~view order~$~151005688688795">order details</a> </div></div><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">Phosphorus</h5><h5 class="desc"><a href="/phosphorus-Beige-Slim-Fit-Chinos-1095593.html" target="_blank">Beige Slim Fit Chinos</a></h5></div><div class="media"><span class="media-left media-top"><a href="/phosphorus-Beige-Slim-Fit-Chinos-1095593.html" target="_blank"><img src="http://static.jabong.com/p/Phosphorus-Beige-Slim-Fit-Chinos-6249-3955901-1-new_cart.jpg" alt="151005688688795"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">36</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase  delivered  '>Delivered</h5><p>on Tue, 6 Oct 2015</p></div></div></div></div> <div class="col-md-3 col-sm-4 col-xs-4 col-lg-3 text-right notice-block">                                      <p>You cannot return or exchange this Order as returns/Exchange period has expired.</p>               </div>         </section><section class="product-info-wrapper clearfix" ><div class="col-sm-8 col-md-9 col-lg-9 col-xs-8 "><div class="product-headding"><h5 class="text-uppercase brand-name">Phosphorus</h5><h5 class="desc"><a href="/phosphorus-Light-Blue-Slim-Fit-Jeans-1264236.html" target="_blank">Light Blue Slim Fit Jeans</a></h5></div><div class="media"><span class="media-left media-top"><a href="/phosphorus-Light-Blue-Slim-Fit-Jeans-1264236.html" target="_blank"><img src="http://static.jabong.com/p/Phosphorus-Light-Blue-Slim-Fit-Jeans-4588-6324621-1-new_cart.jpg" alt="151005688688795"></a></span><div class="media-body text-left"><div class="text-uppercase size-block"><span class="select-size"><span class="text-capitalize">size</span><span class="clr-black">36</span></span><span class="size-separator">|</span><span class="qty-block"><span class="text-capitalize">qty</span><span class="clr-black">1</span></span></div><div class="deliver-time"><h5 class='text-uppercase  delivered  '>Delivered</h5><p>on Tue, 6 Oct 2015</p></div></div></div></div> <div class="col-md-3 col-sm-4 col-xs-4 col-lg-3 text-right notice-block">                                      <p>You cannot return or exchange this Order as returns/Exchange period has expired.</p>               </div>         </section></section>
'''

html_amazon = """

"""


# for flipkart
def flipkart(html_str=flipkart_str):
    """
    parses the markup str and returns the order objects
    :param html_str: markup as str
    :return: list of Order objects, the orders contained in html
    """

    soup = BeautifulSoup(html_str, "html.parser")
    # finding all the orders
    orders = soup.findAll("div", attrs={"class": "order"})

    order_objs = list()
    # iterating over all the orders to get details
    for order in orders:
        order_details = order.find("div", {"class": "order-collapsed"})
        order_details = order_details.findAll("div")  # details of the order
        order_id = order_details[0].find("strong").string  # order ID
        name = order_details[1].string.strip()  # order name
        # total order value
        value = float(order_details[2].find('strong').string.split('s.')[1])
        # print("Order details:")
        # print("ID: ", order_id)
        # print("Name: ", name)
        # print("Value: ", value)
        # print("Items:")
        # now adding items and their details
        items = order.find(
            "div", {"class": "js-order-details"}
        ).findAll(
            "div", {"class": "order-item"})
        item_objs = list()
        for item in items:
            item_details = item.find(
                'div', {'class': 'order-item-inner'}
            ).findAll('div')
            item_url = item_details[0].find('a')['href']
            image_url = item_details[0].find('img')['data-src']
            item_name = item_details[1].find('a').string.strip()
            properties = item_details[1].findAll('p')[-1].string.strip()
            
            # prop_list = properties.split('\xa0')
            # prop_dict = {e.split(':')[0].strip(): e.split(':')[1].strip() for
            #              e in prop_list}
            price = float(item_details[2].find('div').text.strip().split(' ')[1])
            status = item_details[4].text.strip()
            # print("Item details:")
            # print("Name: ", item_name)
            # print("Item URL: ", item_url)
            # print("Image URL: ", image_url)
            # print("Properties: ", prop_dict)
            # print("Price: ", price)
            # print("Staus: ", status)
            item_obj = Item(name=item_name, properties=properties, price=price,
                            image_url=image_url, item_url=item_url,
                            status=status)
            item_objs.append(item_obj)
        order_summary = order.find(
            "div", {"class": "js-order-details"}
        ).find(
            "div", {"class": "order-total"}
        ).find("div", {"class": "unit size2of5"})
        seller_and_date = order_summary.text.strip()
        seller, order_date = (e.split(":")[1].strip() for
                              e in seller_and_date.split("\n"))
        # print("Order date: ", order_date)
        # print("Seller: ", seller)
        order_obj = Order(id=order_id, name=name, value=value, items=item_objs,
                          order_date=order_date, seller=seller)
        order_objs.append(order_obj)

    return order_objs


# for jabong
def jabong(html_str=html_jabong):
    """
    parses the html string for jabong and extracts useful information
    for jabong
    :param html_str: markup of jabong as str
    :return: list of Order objects
    """
    print "entered"
    soup = BeautifulSoup(html_str, 'html.parser')
    # find all orders
    orders = soup.find_all('section', attrs= {'class': 'order-dashboard-block'})
    order_objs = []

    # looping all orders
    for order in orders:
        order_details = order.find('div', {'class': 'order-dashboard-header clearfix'})
        id = order_details.find('h4').find('span').string
        order_date = order_details.find('p', {'class':'order-placed'}).find('span').string.split(' at')[0]
        value = float(order_details.find('p', {'class':'order-amount'}).find('span').string)
        name = 'Not Provided'
        seller = 'Not Provided'
        # print('value:  ', value)
        items = order.findAll('section', {'class': 'product-info-wrapper clearfix'})

        item_objs = []
        for item in items:
            item_name = item.find('h5', {'class': 'desc'}).string
            item_url = item.find('h5', {'class': 'desc'}).find('a').get('href')
            img_url = item.find('div', {'class': 'media'}).find('img').get('src')
            price = None
            media = item.find('div', {'class': 'media'})
            status = media.find('div', {'class': 'deliver-time'}).find('h5').string
            props = item.find('div', {'class': 'text-uppercase size-block'}).findAll('span')
            prop_dict = {e.findAll('span')[0].string.strip(): e.findAll('span')[1].string.strip() for e in props if e.find('span')}

            # print ('id', id, '--item---', name, '--item_url---', item_url, '--img url---', img_url,'--status--', status)
            # print('--props--', prop_dict)
            item_obj = Item(
                name=item_name,
                item_url=item_url,
                image_url=img_url,
                price=price,
                properties=prop_dict,
                status=status
            )
            item_objs.append(item_obj)
        order_obj = Order(
            id=id,
            name=name,
            value=value,
            order_date=order_date,
            seller=seller,
            items=item_objs
        )
        order_objs.append(order_obj)
    return order_objs


# for amazon
def amazon(html_str):
    """
    parses html string and extracts useful information for amazon
    :param html_str: html markup of amazon as str
    :return: list of Order objects extracted from markup
    """
    soup = BeautifulSoup(html_str, "html.parser")
    # finding all the orders
    orders = soup.findAll("div", {"class": "order"})

    order_objs = list()
    # iterating over all the orders to get details
    for order in orders:
        order_date = order.find("span", {"class": "value"}).text.strip()
        value_str = order.findAll("span", {"class": "value"})[1].text
        value = float(value_str.split('s.')[1].replace(',', '').strip())
        order_id = order.findAll(
            "span", {"class": "value"}
        )[-1].text.strip()
        links = order.findAll("a", {"class": "a-link-normal"})
        name = links[-2].text.strip()
        seller = links[-1].text.strip()
        status = order.find(
            "div", {"class": "shipment"}
        ).find("span").text.strip()
        image_url = order.find("img")["data-a-hires"]
        item_url = order.find(
            "div", {"class": "item-view-left-col-inner"}
        ).find("a")["href"]
        item_obj = Item(name=name, properties={}, price=value,
                        image_url=image_url, item_url=item_url,
                        status=status)
        order_obj = Order(id=order_id, name=name, value=value,
                          items=[item_obj], order_date=order_date,
                          seller=seller)
        order_objs.append(order_obj)

    return order_objs
