$(document).ready(function(){
	
	// Hide or show user profile information
	$('.tab-link').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('.tab-link').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	});
	
	$('.back-btn').click(function(){
		window.history.back();
	});
	
	$('.sidenav').sidenav({edge:'right'});
	
	$(".dropdown-trigger").dropdown({coverTrigger: false});
	
    $('select').formSelect();
    
    $('textarea').characterCounter();
})