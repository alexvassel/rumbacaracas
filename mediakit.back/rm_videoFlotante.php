<?php include("header.php"); ?><!-- start:content -->
	<div id="content">
		<?php $current = 14; include("menu.php"); ?>
		
		<div id="mainContent">
			
			<div id="title">
				<small>Rich Media</small>
				<h1>Video Flotante</h1>
			</div>
			<div id="colTxt">
				<p>Creatividad flotante que se ubica en una capa (layer) superior a la página donde éste se mostrará. El video flotante aparecerá y/o se desplazará por encima del contenido del sitio pero el usuario puede cerrarlo cuando desee mediante el botón de "cerrar".</p>
				<p>La característica principal de este formato es que combina la libertad creativa de un satélite con la posibilidad de mostrar un pequeño video en formato (flv - flash video). Puede ser fija o rotar con otras publicidades.</p>
				<p>Esta pieza debe ser mostrada en <strong>MUTE</strong> por defaul y debe tener el botón "cerrar". Puede o no comenzar con <em>autoplay</em> y se recomienda una imagen transparente encima del video que haga enlace a la página web del cliente.</p>
				<p><a href="http://essentials.baltimoresun.com/media_kit/ad-examples/rich_media/renn_fest.html" target="_blank" style="font-weight: bold">Ejemplo 1</a></p>
		  <!--span class="btn"><a href="h#" rel="ligthbox"  class="botonVerB">Ver Especificaciones</a></span>
				<h2>Especificaciones:</h2>
				<ul>
					<li><strong>Formato: </strong></li>
					<li><strong>Medidas:</strong></li>
				</ul--></div>
			<div id="colImg" style="margin-top:-70px;">
				Debe actualizar su versión de <a href="http://www.adobe.com/getflash/">flash</a>.
			</div>
			<script type="text/javascript">
				// <![CDATA[
				
				var so = new SWFObject("media/videoBanner.swf", "peel", "351", "503", "9", "#FFFFFF");
				so.addParam("wmode", "transparent");
				so.write("colImg");
				
				// ]]>
			</script>
			<div class="clear"></div>
		</div>
		
		<div class="clear"></div>
		
	</div>
	<!-- end:content -->

</div>
</body>
</html>