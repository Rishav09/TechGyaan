$(document).ready(function(){
	$("#about-btn").click(function(event){
		alert("You clicked the button using Jquery!");
	});
	$("p").hover(function(){
		$(p).css('color','red');
	},
	function(){
		$(p).css('color','blue');
	});
});