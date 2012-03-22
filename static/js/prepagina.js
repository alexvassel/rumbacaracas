
	function leerCookie(nombre) {
	   a = document.cookie.substring(document.cookie.indexOf(nombre + '=') + nombre.length + 1,document.cookie.length);
	   if(a.indexOf(';') != -1)a = a.substring(0,a.indexOf(';'))
	   return a; 
	}

	if(leerCookie('prepagina')!="si") {
		document.cookie="prepagina = si"
		document.cookie="direccion = "+location.href
		window.location = "http://www.rumbacaracas.com/templates/pre.html"
	}
