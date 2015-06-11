<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="author" content="Lucas Recalde www.doliaku.com" />
<title>Media Kit :::: RumbaCaracas.com</title>
<link rel="stylesheet" type="text/css" href="css/estilo.css" />
<script src="http://www.google.com/jsapi" type="text/javascript"></script>
<script type="text/javascript" charset="utf-8">
	google.load("jquery", "1.3");
</script>
<link rel="stylesheet" href="css/prettyPhoto.css" type="text/css" media="screen" title="prettyPhoto main stylesheet" charset="utf-8" />
<script src="js/jquery.prettyPhoto.js" type="text/javascript" charset="utf-8"></script>
</head>

<body class="contacto">
<div id="bodyWrapper">
	<!-- start:header -->
	<div id="header">
		<div id="mediaKit"><img src="images/mediaKit.png" alt="RumbaCaracas.com Media Kit" /></div>
		<div id="logo">
			<a href="http://www.rumbacaracas.com/" title="Volver a RumbaCaracas.com"><img src="images/logo.png" alt="RumbaCaracas.com" /></a>
			<img src="images/slogan.png" alt="Nos tomamos la Rumba en serio..." class="slogan" />
		</div>
	</div>
	<!-- end:header -->

	<!-- start:content -->
	<div id="content">
		<?php $current = 24; include("menu.php"); ?>
		
		<div id="mainContent">
			<div id="title">
				<small>RumbaCaracas.com</small>
				<h1>Contacto</h1>
			</div>
			<div id="colTxt">
				<form method="post" action="#">
					<p><label for="name">Nombre:</label><br />
					<input type="text" id="name" name="name" /></p>
					<p><label for="apellido">Apellido:</label><br />
					<input type="text" id="apellido" name="apellido" /></p>
					<p><label for="email">E-mail:</label><br />
					<input type="text" id="email" name="email" /></p>
					<p><label for="tel">Teléfono:</label><br />
					<input type="text" id="tel" name="tel" /></p>
					<p><label for="comment">Comentario:</label><br />
					<textarea id="comment" name="comment" cols="20" rows="5"></textarea></p>
					<p class="alignright"><button type="submit" value="Enviar" class="botonVerB">Enviar</button>
				</form>
			</div>
			<div class="clear"></div>
		</div>
		
		<div class="clear"></div>
		
	</div>
	<!-- end:content -->

</div>
</body>
</html>