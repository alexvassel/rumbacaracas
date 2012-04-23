	if($.cookie('prepagina') == null) {
        $.cookie('realreferrer', document.referrer,{path: '/', domain: '.rumbacaracas.com'});
        $.cookie('prepagina', "si", {path: '/', domain: '.rumbacaracas.com'});
		window.location = "http://media.rumbacaracas.com/static/pre.html"
	}
