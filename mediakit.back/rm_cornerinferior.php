<?php include("header.php"); ?><!-- start:content -->
	<div id="content">
		<?php $current = 11; include("menu.php"); ?>
		
		<div id="mainContent">
			
			<div id="title">
				<small>Rich Media</small>
				<h1>Banner Corner Inferior</h1>
			</div>
			<div id="colTxt">
				<p>Este formato puede posicionarse en determinadas esquinas del sitio y despierta la curiosidad del usuario mostrando solo parte del anuncio, para así revelarlo cuando el usuario pase el cursor sobre la creatividad.</p>
				<p>Al <em>clickear</em> en cualquier &aacute;rea del banner, el enlace debe estar dirigido a la página del cliente.</p>
				<p><a href="http://www.motorcycle-superstore.com/1/1/39/33038/ITEM/Icon-Overlord-Jacket.aspx" target="_blank" style="font-weight: bold">Ejemplo 1</a></p>
				<span class="btn"><a href="espec_bnCornerInferior.html" onclick="Modalbox.show(this.href, {title: this.title, width: 800}); return false;" title="Especificaciones:" class="botonVerB">Ver Especificaciones</a></span>
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
				
				var so = new SWFObject("media/cornerinferior.swf", "corner", "351", "270", "9", "#FFFFFF");
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