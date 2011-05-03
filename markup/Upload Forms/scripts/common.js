
$(document).ready(function( )
{
	if ($("img.facebook").length > 0)
	{
		$("img.facebook").mouseover(function( )
		{
			this.src = this.src.replace(".jpg", "-hover.jpg");
		});


		$("img.facebook").mouseout(function( )
		{
			this.src = this.src.replace("-hover.jpg", ".jpg");
		});
	}
	
	
	if ($(".calendar #txtDate").length > 0)
	{
		$(".calendar #txtDate").datepicker( { showOn          : "button",
						      buttonImage     : "images/icons/calendar.jpg",
						      buttonImageOnly : true,
						      dateFormat      : "yy-mm-dd"
					    	    } );
	}
	
	if ($(".calendar #txtFromDate").length > 0)
	{
		$(".calendar #txtFromDate").datepicker( { showOn          : "button",
						          buttonImage     : "images/icons/calendar.jpg",
						          buttonImageOnly : true,
						          dateFormat      : "yy-mm-dd"
					                } );
	}	
	
	if ($(".calendar #txtToDate").length > 0)
	{
		$(".calendar #txtToDate").datepicker( { showOn          : "button",
						        buttonImage     : "images/icons/calendar.jpg",
						        buttonImageOnly : true,
						        dateFormat      : "yy-mm-dd"
					               } );
	}		
});