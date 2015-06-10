<?php
$active[$current] = "class=current";
?>
		
		<div id="colMenu">
			<ul>
				<li>
					<h3>Publicidad en Banners</h3>
					<ul>
						<li <?php echo $active[1] ?>><a href="pb_grande.php">Banner Grande</a></li>
						<li <?php echo $active[2] ?>><a href="pb_pequeno.php">Banner peque&ntilde;o del home</a></li>
						<li <?php echo $active[3] ?>><a href="pb_estandar.php">Banner Est&aacute;ndar</a></li>
						<li <?php echo $active[4] ?>><a href="pb_cuadrado.php">Banner Cuadrado</a></li>
						<li <?php echo $active[5] ?>><a href="pb_rascacielos.php">Rascacielos</a></li>
						<li <?php echo $active[6] ?>><a href="pb_estampilla.php">Estampilla est&aacute;ndar</a></li>
						<li <?php echo $active[7] ?>><a href="pb_boton.php">Bot&oacute;n</a></li>
						<li <?php echo $active[8] ?>><a href="pb_prepag.php">Publicidad previa / Pre-p&aacute;gina</a></li>
					</ul>
				</li>
				<li>
					<h3>Rich Media</h3>
					<ul>
						<li <?php echo $active[9] ?>><a href="rm_desplegable.php">Banner Desplegable</a></li>
						<li <?php echo $active[10] ?>><a href="rm_pushdown.php">Banner Pushdown Expandible</a></li>
						<li <?php echo $active[11] ?>><a href="rm_corner.php">Banner Corner</a></li>
						<li <?php echo $active[12] ?>><a href="rm_peel.php">Banner Peel</a></li>
						<li <?php echo $active[13] ?>><a href="rm_videoBanner.php">Video Banner</a></li>
						<li <?php echo $active[14] ?>><a href="rm_videoFlotante.php">Video Flotante</a></li>
						<li <?php echo $active[15] ?>><a href="rm_satelite.php">Sat&eacute;lite</a></li>
					</ul>
				</li>
				<li>
					<h3>Patrocinios</h3>
					<ul>
						<li <?php echo $active[16] ?>><a href="pa_seccion.php">Secci&oacute;n</a></li>
						<li <?php echo $active[17] ?>><a href="pa_mobil.php">Mobil</a></li>
						<li <?php echo $active[18] ?>><a href="pa_lightbox.php">Imagen en LightBox</a></li>
						<li <?php echo $active[19] ?>><a href="pa_minisite.php">Minisite</a></li>
					</ul>
				</li>
				<li>
					<h3>E-Rumba</h3>
					<ul>
						<li <?php echo $active[20] ?>><a href="er_semanal.php">E-rumba Semanal</a></li>
						<li <?php echo $active[21] ?>><a href="er_especial.php">E-Rumba Especial</a></li>
					</ul>
				</li>
				<li <?php echo $active[22] ?>><a href="estadisticas.php"><h3>Estad&iacute;sticas</h3></a></li>
				<!--li < ?php echo $active[23] ?>><a href="target.php"><h3>Nuestro Target</h3></a></li-->
				<li <?php echo $active[24] ?>><a href="contacto.php"><h3>Contacto</h3></a></li>
			</ul>
		</div>
