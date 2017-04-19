$('#likes').click(function(){
	var catid;
	catid=$(this).attr("data-catid");
	$.get('/techGyaan/like/',{category_id:catid},function(data){
		$('#like_count').html(data);
			$('#likes').hide();
	});
});