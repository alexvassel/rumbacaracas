<?php include("header.php"); ?><!-- start:content -->
	<div id="content">
		<?php $current = 13; include("menu.php"); ?>
		
		<div id="mainContent">
			
			<div id="title">
				<small>Rich Media</small>
				<h1>Video Banner</h1>
			</div>
			<div id="colTxt">
				<p>Creatividad cuadrada ubicada en algunas páginas del sitio que muestra un pequeño video en formato (flv - flash video) que permite ser totalmente controlado (inicio, pausa, reinicio, volumen) y tiene la característica de descargarse progresivamente. Puede ser fijo en algunas secciones o rotar con otras publicidades.</p>
				<h2>Especificaciones:</h2>
				<ul>
                  <li><strong>Formato:</strong> Flash</li>
				  <li><strong>Tama&ntilde;o:</strong> 300 x 250 p&iacute;xeles</li>
				  <li><strong>Peso:</strong> no mayor de 80K</li>
			      <li>El video  debe comenzar en <strong>MUTE</strong> por default. </li>
			      <li>Puede o no comenzar con <strong>AUTOPLAY</strong> </li>
			      <li>Se recomienda una imagen transparente encima del video que haga enlace a la página web del cliente con el <strong>Target _blank</strong></li>
			      <li>El video debe  venir de un archivo .flv externo. Para esto, se le debe indicar al banner (archivo .swf) que llame al .flv a través del  URL <a href="http://www.rumbacaracas.com/flv/turner/NOMBRELDEVIDEO.FLV">http://www.rumbacaracas.com/flv/NOMBRE DEL CLIENTE/NOMBREL DEl VIDEO.FLV<br />
			      </a>Ejemplo: http://www.rumbacaracas.com/flv/<strong>toyota/videopromocional.flv</strong></li>
			      <li>El cliente debe entregar: El Video (archivo .flv) y el Banner (archivo .swf)</li>
			  </ul>
		  <!--span class="btn"><a href="h#" rel="ligthbox"  class="botonVerB">Ver Especificaciones</a></span>
				<h2>Especificaciones:</h2>
				<ul>
					<li><strong>Formato: </strong></li>
					<li><strong>Medidas:</strong></li>
				</ul--></div>
			<div id="colImg">
				<img src="images/muestras/videobanner.jpg" alt="Ejemplo de video banner" />
			</div>
			<!--script type="text/javascript">
				// <![CDATA[
				
				var so = new SWFObject("media/videoFlotante.swf", "peel", "351", "503", "9", "#FFFFFF");
				so.addParam("wmode", "transparent");
				so.write("colImg");
				
				// ]]>
			</script-->
			<div class="clear"></div>
		</div>
		
		<div class="clear"></div>
		
	</div>
	<!-- end:content -->

</div>
</body>
</html>