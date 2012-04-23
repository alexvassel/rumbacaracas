    if($.cookie('prepagina') == null) {
        $.cookie('realreferrer', document.referrer,{path: '/', domain: '.rumbavenezuela.com'});
                $.cookie('prepagina', "si", {path: '/', domain: '.rumbavenezuela.com'});
        window.location = "http://media.rumbacaracas.com/static/preve.html"
    }
