<?php include("header.php"); ?>

	<!-- start:content -->
	<div id="content">
		<?php $current = 9; include("menu.php"); ?>
		
		<div id="mainContent">
			
			<div id="title">
				<small>Rich Media</small>
				<h1>Banner Desplegable</h1>
			</div>
			<div id="colTxt">
				<p>El formato comienza con un banner rectangular en su tama&ntilde;o original. Cuando el usuario se posiciona por sobre el anuncio (<em>mouse-over</em>), &eacute;ste se expande hacia abajo. El banner se repliega al quitarle el cursor de la imagen.</p>
				<p>Al <em>clickear</em> en cualquier &aacute;rea del banner, el enlace debe estar dirigido a la página del cliente.</p>
				<span class="btn"><a href="espec_bnDeplegable.html" onclick="Modalbox.show(this.href, {title: this.title, width: 800}); return false;" title="Especificaciones" class="botonVerB">Ver Especificaciones</a></span>
				<!--h2>Especificaciones:</h2>
				<ul>
					<li><strong>Formato: </strong></li>
					<li><strong>Medidas:</strong></li>
				</ul--></div>
			<div id="colImg">
				Debe actualizar su versión de <a href="http://www.adobe.com/getflash/">flash</a>.
			</div>
			<script type="text/javascript">
				// <![CDATA[
				
				var so = new SWFObject("images/muestras/desplegable.swf", "desplegable", "351", "767", "9", "#FFFFFF");
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