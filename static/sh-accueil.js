$(document).ready(function () {

	var panelopened = false;
	var linkopened = false;
	var win = $(window);
var col_numb =  parseInt( win.width() / 5 * 4 / 310 );
	$('#links_gotop').hide();
	$('#img_refresh').click(function() { refresh(); });
$('#news').width( 310 * col_numb );

	$('#links_gotop').click(function(e) { $('html, body').animate({ scrollTop: 0 }, 400); });
	$('#links_gobot').click(function(e) { $('html, body').animate({ scrollTop: $(document).height() }, 400); });
	$(window).bind('focus', function() { refresh(); });
	$(window).bind('blur', function() { refresh(); });
	
	$('#display_block').click(function() {
		var oldlink = document.getElementsByTagName("link").item(1);
		var newlink = document.createElement("link");
        newlink.setAttribute("rel", "stylesheet");
        newlink.setAttribute("type", "text/css");
        newlink.setAttribute("href", "/static/index-normal.css");
        document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
	});
	
	$('#display_line').click(function() {
		var oldlink = document.getElementsByTagName("link").item(1);
		var newlink = document.createElement("link");
        newlink.setAttribute("rel", "stylesheet");
        newlink.setAttribute("type", "text/css");
        newlink.setAttribute("href", "/static/index-line.css");
        document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
	});
	
	$('#applicate').click(function(e) { 
		filters = JSON.stringify(get_filters());
	$.ajax({
		    type: "POST",
		    url: '/apply_news/',
		    data: {
		    	static_url: "{{ STATIC_URL }}",
		    	filters: filters
		    }
		}).done(function(msg){
			$('#avai_news').css('color', 'grey');
			$('.new').remove()
			$('#img_refresh').after(msg);
			$('.new').each(function() {
		    	$(this).fadeIn("slow");
			});
		});
	});
	
	$('#links_opener').click(function(){
		if ( linkopened ) {
			linkopened = false;
	    	$('#links').animate({ "right": "-70px" }, 'fast');
	    	$('#img_links_opener').attr("src", "{{ STATIC_URL }}flechegauche.png");
	    } else {
	    	linkopened = true;
	    	$('#links').animate({ "right": "20px" }, 'fast');
	    	$('#img_links_opener').attr("src", "{{ STATIC_URL }}flechedroite.png");
	    }
	});
	
	$('.part_filter').click(function() {
		var classname = $(this).attr('class').split(' ')[1];
		var check = $(this).is(':checked');
		$('.' + classname).each(function() { $(this).prop('checked', check); });
	});
	
	$('#panel_opener').click(function(){
		if ( panelopened ) {
			panelopened = false;
	    	$('#panel').animate({ "left": "-400" }, 300);
	    	$('#img_panel_opener').attr("src", "{{ STATIC_URL }}flechedroite.png");
	    } else {
	    	panelopened = true;
	    	$('#panel').animate({ "left": "20" }, 300);
	    	$('#img_panel_opener').attr("src", "{{ STATIC_URL }}flechegauche.png");
	    }
	});
	
	$(window).on('scroll', function() {
	    var scrollTop = $(this).scrollTop();
	    if ( scrollTop != 0 ) {
	    	$('#links_gotop').show();
	    } else {
	    	$('#links_gotop').hide();
	    }
	    if(scrollTop + $(window).height() == $(document).height()) {
	    	$('#links_gobot').hide();
	    } else {
	    	$('#links_gobot').show();
	    }
	});
	
$('#avai_news').click(function() {
	if ( document.getElementById('avai_news').innerHTML != '0 Nouvelles Actus !' ) {
		filters = JSON.stringify(get_filters());
        	last_id = $("#news div:nth-child(3)").attr('id');
        	$.ajax({
			    type: "POST",
			    url: '/get_news/',
			    data: { 
			    	last_id: last_id,
			    	static_url: "{{ STATIC_URL }}",
			    	filters: filters
			    }
			}).done(function(msg){
				$('#avai_news').css('color', 'grey');
				$('#avai_news').html('0 Nouvelles Actus !');
				$('#img_refresh').after(msg);
				$('.new').each(function() {
			    	$(this).fadeIn("slow");
				});
			});
		}
	});
});

$(window).on('resize', function(){
var win = $(this);
var col_numb =  parseInt( win.width() / 5 * 4 / 310 );
$('#news').width( 310 * col_numb );
});

function refresh(){
	last_id = $("#news a div:nth-child(1)").attr('id');
	filters = JSON.stringify(get_filters());
	$.ajax({
	    type: "POST",
	    url: '/refresh/',
	    data: { 
	    	last_id: last_id,
	    	filters: filters,
	    }
	}).done(function(msg, news){
		$('#avai_news').html(msg);
		$('#avai_news').slideDown(1000);
		if (news == true){
			$('title').html("Sports Hub ["+msg+"]");
			$('#avai_news').css('color', 'white');
		}
	});
}

function get_filters(){
	var filters = {};
	$('.part_filter').each(function() {
		if ($(this).is(':checked')) {
			var classname = $(this).attr('class').split(' ')[1];
			var checked = '';
	    	$('.'+classname).each(function() {
	    		if ($(this).is(':checked')) {
	    			checked += $(this).parent().text() + ";";
	    		}
	    	});
	    	filters[$(this).parent().text()] = checked;
	    }
	});
	return filters;
}
