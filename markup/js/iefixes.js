/**
+------------------------------------------------------------------------------------------+
* COMPANY: Raven Developers 2010
+------------------------------------------------------------------------------------------+
* FILE INFO: Fixes IE (the biggest virus and worms explorer in the world) bugs, the lack of
* support for CSS 3 of a non W3C standards dull and pathetic browser.
+------------------------------------------------------------------------------------------+
* WEBSITE: http://www.ravendevelopers.com
+------------------------------------------------------------------------------------------+
* Portions created by Anirudh K. Mahant are Copyright of Raven Developers (C) 2010.
+------------------------------------------------------------------------------------------+
* COPYRIGHT NOTICE:
* The original author(s) retain all the copyrights of this file.
* Portions created by Anirudh K. Mahant (original developer) are Copyright of Raven Developers (C) 2010.
* Portions contains JavaScript framework jQuery developed by John Resig and other community members
* http://docs.jquery.com/About
* jQuery LICENSE:
* Copyright (c) 2008 John Resig (jquery.com)
* Dual licensed under the MIT (MIT-LICENSE.txt)
* and GPL (GPL-LICENSE.txt) licenses.
+------------------------------------------------------------------------------------------+
*/

/**
*	PNGFix
*/
(function($){jQuery.fn.pngFix=function(settings){settings=jQuery.extend({blankgif:"blank.gif"},settings);var ie55=(navigator.appName=="Microsoft Internet Explorer"&&parseInt(navigator.appVersion)==4&&navigator.appVersion.indexOf("MSIE 5.5")!=-1);var ie6=(navigator.appName=="Microsoft Internet Explorer"&&parseInt(navigator.appVersion)==4&&navigator.appVersion.indexOf("MSIE 6.0")!=-1);if(jQuery.browser.msie&&(ie55||ie6)){jQuery(this).find("img[src$=.png]").each(function(){jQuery(this).attr("width",jQuery(this).width());jQuery(this).attr("height",jQuery(this).height());var prevStyle="";var strNewHTML="";var imgId=(jQuery(this).attr("id"))?'id="'+jQuery(this).attr("id")+'" ':"";var imgClass=(jQuery(this).attr("class"))?'class="'+jQuery(this).attr("class")+'" ':"";var imgTitle=(jQuery(this).attr("title"))?'title="'+jQuery(this).attr("title")+'" ':"";var imgAlt=(jQuery(this).attr("alt"))?'alt="'+jQuery(this).attr("alt")+'" ':"";var imgAlign=(jQuery(this).attr("align"))?"float:"+jQuery(this).attr("align")+";":"";var imgHand=(jQuery(this).parent().attr("href"))?"cursor:hand;":"";if(this.style.border){prevStyle+="border:"+this.style.border+";";this.style.border="";}if(this.style.padding){prevStyle+="padding:"+this.style.padding+";";this.style.padding="";}if(this.style.margin){prevStyle+="margin:"+this.style.margin+";";this.style.margin="";}var imgStyle=(this.style.cssText);strNewHTML+="<span "+imgId+imgClass+imgTitle+imgAlt;strNewHTML+='style="position:relative;white-space:pre-line;display:inline-block;background:transparent;'+imgAlign+imgHand;strNewHTML+="width:"+jQuery(this).width()+"px;"+"height:"+jQuery(this).height()+"px;";strNewHTML+="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader"+"(src='"+jQuery(this).attr("src")+"', sizingMethod='scale');";strNewHTML+=imgStyle+'"></span>';if(prevStyle!=""){strNewHTML='<span style="position:relative;display:inline-block;'+prevStyle+imgHand+"width:"+jQuery(this).width()+"px;"+"height:"+jQuery(this).height()+"px;"+'">'+strNewHTML+"</span>";}jQuery(this).hide();jQuery(this).after(strNewHTML);});jQuery(this).find("*").each(function(){var bgIMG=jQuery(this).css("background-image");if(bgIMG.indexOf(".png")!=-1){var iebg=bgIMG.split('url("')[1].split('")')[0];jQuery(this).css("background-image","none");jQuery(this).get(0).runtimeStyle.filter="progid:DXImageTransform.Microsoft.AlphaImageLoader(src='"+iebg+"',sizingMethod='scale')";}});jQuery(this).find("input[src$=.png]").each(function(){var bgIMG=jQuery(this).attr("src");jQuery(this).get(0).runtimeStyle.filter="progid:DXImageTransform.Microsoft.AlphaImageLoader"+"(src='"+bgIMG+"', sizingMethod='scale');";jQuery(this).attr("src",settings.blankgif);});}return jQuery;};})(jQuery);

jQuery(document).ready(function() {
	if (jQuery.browser.msie){
		jQuery("a.outnone").focus(function(){jQuery(this).blur();});jQuery(".outnone a").each(function(){jQuery(this).focus(function(){jQuery(this).blur();});});
		if (jQuery.browser.version <= 6.0){jQuery(document).pngFix();}
    jQuery('#main-contents #col-left .node .content p:last').addClass('pb0');
    jQuery('#main-contents #col-right div.widget:first').addClass('mt0');
	}
});