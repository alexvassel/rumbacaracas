<?php include("header.php"); ?><!-- start:content -->
	<div id="content">
		<?php $current = 10; include("menu.php"); ?>
		
		<div id="mainContent">
			<div id="title">
				<small>Rich Media</small>
				<h1>Banner Pushdown Expandible</h1>
			</div>
			<div id="colTxt">
				<p>En primera instancia el banner se muestra sin expandir y mediante el bot&oacute;n de "abrir", el banner se despliega hacia abajo desplazando parcialmente el contenido del sitio. Se repliega autom&aacute;ticamente mediante el bot&oacute;n de "cerrar". El contenido del sitio que ha sido desplazado vuelve a su lugar original.</p>
				<p>Al <em>clickear</em> en cualquier &aacute;rea del banner, el enlace debe estar dirigido a la página del cliente.</p>
				<span class="btn"><a href="espec_bnPushdown.html" onclick="Modalbox.show(this.href, {title: this.title, width: 800}); return false;" title="Especificaciones" class="botonVerB">Ver Especificaciones</a></span>
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
				
				var so = new SWFObject("media/pushdown.swf", "pushdown", "351", "503", "9", "#FFFFFF");
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