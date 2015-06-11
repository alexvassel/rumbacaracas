<?php include("header.php"); ?><!-- start:content -->
	<div id="content">
		<?php $current = 12; include("menu.php"); ?>
		
		<div id="mainContent">
			
			<div id="title">
				<small>Rich Media</small>
				<h1>Banner Corner Inferior</h1>
			</div>
			<div id="colTxt">
				<p>Se trata de un formato de gran impacto que desgarra la página desde la esquina superior derecha, mostrando luego la publicidad. El desgarre de la página puede ser automático o mediante el botón "abrir" o al colocar el cursor por encima.</p>
				<p>Al <em>clickear</em> en cualquier &aacute;rea del banner, el enlace debe estar dirigido a la página del cliente.</p>
				<h2>Especificaciones:</h2>
				<ul>
                  <li><strong>Formato:</strong> Flash</li>
				  <li><strong>Tama&ntilde;o:</strong> Ancho: 300 - 800 p&iacute;xeles. Alto: Variable. Dependiendo del diseño de la pieza</li>
				  <li><strong>Peso:</strong> no mayor de 200K</li>
			  </ul>
				<p>&nbsp;</p>
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
				
				var so = new SWFObject("media/peel.swf", "peel", "351", "503", "9", "#FFFFFF");
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