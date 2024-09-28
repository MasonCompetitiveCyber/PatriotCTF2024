 $(".gallery ul li a").click(function() {
	var hash = $(this).attr('media');
	var pic = $(this).attr('rel');
	let t1="view.php?pic=";
	let t2="&hash=";
	window.location=t1.concat('',pic).concat('',t2).concat('',hash);
 });
