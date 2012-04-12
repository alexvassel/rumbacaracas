
	function leerCookie(nombre) {
	   a = document.cookie.substring(document.cookie.indexOf(nombre + '=') + nombre.length + 1,document.cookie.length);
	   if(a.indexOf(';') != -1)a = a.substring(0,a.indexOf(';'))
	   return a; 
	}

	if(leerCookie('prepagina')!="si") {
		document.cookie = "realreferrer="+encodeURIComponent(document.referrer)+"; path=/";	
		document.cookie="prepagina = si"
		document.cookie="direccion = "+location.href
		window.location = "http://media.rumbacaracas.com/static/pre.html"
	}
