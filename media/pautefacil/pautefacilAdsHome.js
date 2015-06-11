<!--

	/*	Variables que se deben editar segun el sitio, se debe cambiar el codigo del ID que da la interfaz de e-planning y el nombre del div en el que
		va a buscar la informacion del sitio.
	*/
	
	var espacio_id 	= "e78d8bfd238ebaa1";
	var espacio_id_m 	= "0c043ce869cd59e9";
	var	tipo 		= "2";
	var timeout 	= "0";
	var maxAds 		= "2";
	var div 		= "contenidoSitio";//nombre de la clase
	//Si es una clase deben dejar el parametro que se llama eClassName, si es ID deben dejar el que se llama eId
	var tipContene	= "eId";//"eId"
	
	/*	Hasta aqui se debe editar	*/
	var eplArgs = {sV:"http://ads.us.e-planning.net/",vV:"4",sI:"58d6",kC:"txtad",tipContene:div};
	var eplAdsArray = new Array();
		
	/*	La funcion eplPautefacil da el formato el texto, este formato puede ser definido incluyendo aqui los estilos que se necesiten.		*/		
	function eplPautefacil(adsArray) {

	var r=''; pad=''; a1=false;
	// Variables para personalizar:
	var adsVert = true; var imgFloat = '';
	// fin variables personalizables
	for (var i=0; i<adsArray.length; i++) {
		var ad = adsArray[i];

		if (!ad.shown && (1==ad.t||2==ad.t||7==ad.t||8==ad.t||41==ad.t) && !(7==ad.e||8==ad.e)) {
			if (!a1) {
				

				r+= '<div class="pauteFacil"><ul><li class="pautefacilLogo"><a href="http://www.pautefacil.com/?utm_source=PF&utm_medium=banner&utm_campaign=caja" target="_blank" title="PauteFacil.com, pautar en Internet, publicidad online"><img src="http://www.pautefacil.com/imagenes/pautefacil_anuncios.png" border="0"></a></li>';
				if (!adsVert) { r+= ''; }
				a1 = true;
			} else {
				pad = 'padding:5px';

			}
			r+= '';
			if (41==ad.t) { // link de texto
				r+= '<li class="pautefacilBox"><a class="pautefacilTitle" rel="nofollow" target="_blank" href="'+ ad.lU +'"><strong>'+ ad.tit +'</strong></a>';

				if (ad.desc) r+= '<br/><span class="pautefacilDescrip">'+ ad.desc +'</span>';
				if (ad.urlv) r+= '<br/><a rel="nofollow" class="pautefacilUrlv" target="_blank" href="' + ad.lU + '">' + ad.urlv + '</a>';

			} else if (!ad.e) { // flash o imagen sin efecto
				r+= ad.getBaseTag();			
			} else { // imagen+texto
				r+= '<li class="pautefacilBox1"><a class="pautefacilTitle" rel="nofollow" target="_blank" href="'+ ad.lU +'"><strong>'+ ad.tit +'</strong></a><br />';

				if (33!=ad.e) r+= '<div class="gif"'+(imgFloat?' style="float:right;"':'')+'><a target="_blank" href="'+ ad.lU +'"><img src="'+ ad.getURL() +'" border=0 width="150px" height="90" /></a></div>';
				if (34==ad.e) r+= '';
				if (35==ad.e) r+= ''

				r+= '<span class="pautefacilDescrip1">'+ ad.desc +'</span>';
				if (ad.urlv) r+= '<br/><a rel="nofollow" class="pautefacilUrlv1" target="_blank" href="' + ad.lU + '">'+ ad.urlv +'</a>';

			}
			r+= '</li>';
			if (adsVert) r += '';
			ad.shown = true;		
		}
	}
	if (a1) {
		if (!adsVert) r+= '';
		r+= '</ul></div>';
	}
	return r;
}
	
	function eplInit() {
        if (this.readyState == 'complete') {
                document.epl.eplInit(eplArgs);
                for (var i=0; i<eplAdsArray.length; i++) { document.epl.eplPushAd(eplAdsArray[i][0], eplAdsArray[i][1], eplAdsArray[i][2], eplAdsArray[i][3], eplAdsArray[i][4]); 
				}
        }
	}
	if (document.epl != undefined) {
        document.epl.eplInit(eplArgs);
	} 
	else {
        var array = document.getElementsByTagName('script');
        var e = undefined;
        for (var i=0; i<array.length; i++) {
                if (array[i].src.indexOf('epl-41.js') != -1) {
                        e = array[i];
                }
        }
        if (e != undefined) { e.onreadystatechange = eplInit; }
	}
	
	function eplAD4(espacio_id, tipo, timeout, maxAds, custom) {
        document.write('<div id="eplAdDiv'+ espacio_id +'"></div>');
			if (document.epl != undefined) {
				document.epl.eplPushAd(espacio_id, tipo, timeout, maxAds);
            if (custom != undefined) {
                document.epl.setCustomAdShow(espacio_id, custom);
            }
        } 
		else {
            eplAdsArray.push(new Array(espacio_id, tipo, timeout, maxAds, custom));
        }
	}
// -->