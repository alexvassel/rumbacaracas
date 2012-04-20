	if($.cookie('prepagina') == null) {
        $.cookie('realreferrer', document.referrer);
        $.cookie('prepagina', "si");
		window.location = "http://media.rumbacaracas.com/static/pre.html"
	}
