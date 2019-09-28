$(document).ready(function(){
	
	$('.tab-link').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('.tab-link').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	})

})