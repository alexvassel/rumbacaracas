/**
*------------------------------------------------------------------------------------------+
* COMPANY: Raven Developers 2010
+------------------------------------------------------------------------------------------+
* FILE INFO: Site wide Java Script functions
+------------------------------------------------------------------------------------------+
* WEBSITE: http://www.ravendevelopers.com
+------------------------------------------------------------------------------------------+
* Portions created by Anirudh K. Mahant are Copyright of Raven Developers (C) 2010.
+------------------------------------------------------------------------------------------+
* COPYRIGHT NOTICE:
* The original author(s) retain all the copyrights of this file.
* Portions created by Anirudh K. Mahant (original developer) are Copyright of Raven Developers (C) 2010.
* Portions may contain jQuery JavaScript framework developed by John Resig and other
* community members. More info at http://docs.jquery.com/About
* jQuery LICENSE:
* Copyright (c) 2008 John Resig (jquery.com)
* Dual licensed under the MIT (MIT-LICENSE.txt) and GPL (GPL-LICENSE.txt) licenses.
+-------------------------------------------------------------------------------------------+
*/

function URLDecode(psEncodeString){var lsRegExp=/\+/g;return unescape(String(psEncodeString).replace(lsRegExp," "));}function ZebraTables(){theTable=jQuery.find("table.zebra-table");jQuery(theTable).each(function(i){if(this){jQuery(this).find("tr").each(function(i){var zclass=(i%2==0)?"odd":"even";jQuery(this).addClass(zclass);});}});}function ZebraUL(){theUL=jQuery(document).find("ul.zebra-ul");jQuery(theUL).each(function(i){if(this){jQuery(this).find("li").each(function(i){var zclass=(i%2==0)?"odd":"even";jQuery(this).addClass(zclass);});}});}function BlurFocusText(){theText=jQuery("input.blur-focus");jQuery(theText).each(function(i){if(this){jQuery(this).blur(function(){if(this.value==""){this.value=this.defaultValue;}});jQuery(this).focus(function(){if(this.value==this.defaultValue){this.value="";}});}});}

/**
* hoverIntent r5 // 2007.03.27 // jQuery 1.1.2+
* <http://cherne.net/brian/resources/jquery.hoverIntent.html>
* 
* @param  f  onMouseOver function || An object with configuration options
* @param  g  onMouseOut function  || Nothing (use configuration options object)
* @author    Brian Cherne <brian@cherne.net>
*/
(function($){$.fn.hoverIntent=function(f,g){var cfg={sensitivity:7,interval:100,timeout:0};cfg=$.extend(cfg,g?{over:f,out:g}:f);var cX,cY,pX,pY;var track=function(ev){cX=ev.pageX;cY=ev.pageY;};var compare=function(ev,ob){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t);if((Math.abs(pX-cX)+Math.abs(pY-cY))<cfg.sensitivity){$(ob).unbind("mousemove",track);ob.hoverIntent_s=1;return cfg.over.apply(ob,[ev]);}else{pX=cX;pY=cY;ob.hoverIntent_t=setTimeout(function(){compare(ev,ob);},cfg.interval);}};var delay=function(ev,ob){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t);ob.hoverIntent_s=0;return cfg.out.apply(ob,[ev]);};var handleHover=function(e){var p=(e.type=="mouseover"?e.fromElement:e.toElement)||e.relatedTarget;while(p&&p!=this){try{p=p.parentNode;}catch(e){p=this;}}if(p==this){return false;}var ev=jQuery.extend({},e);var ob=this;if(ob.hoverIntent_t){ob.hoverIntent_t=clearTimeout(ob.hoverIntent_t);}if(e.type=="mouseover"){pX=ev.pageX;pY=ev.pageY;$(ob).bind("mousemove",track);if(ob.hoverIntent_s!=1){ob.hoverIntent_t=setTimeout(function(){compare(ev,ob);},cfg.interval);}}else{$(ob).unbind("mousemove",track);if(ob.hoverIntent_s==1){ob.hoverIntent_t=setTimeout(function(){delay(ev,ob);},cfg.timeout);}}};return this.mouseover(handleHover).mouseout(handleHover);};})(jQuery);

/*!
 * equalWidths jQuery Plugin
 * Examples and documentation at: hhttp://aloestudios.com/tools/jquery/equalwidths/
 * Copyright (c) 2010 Andy Ford
 * Version: 0.1 (2010-04-13)
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 * Requires: jQuery v1.2.6+
 */
(function($){
	$.fn.equalWidths = function(options) {
		var opts = $.extend({
			stripPadding: 'none', // options: 'child', 'grand-child', 'both'
			minusWidth: 0
		},options);
		return this.each(function(){
			var child_count = $(this).children().size();
			if (child_count > 0) { // only proceed if we've found any children
				var w_parent = $(this).width();
				var w_child = Math.floor(w_parent / child_count);
				var w_child_last = (w_parent - (w_child * (child_count -1)))-opts.minusWidth;
				if ($.browser.msie){
					var w_child = (Math.floor(w_parent / child_count)) - 5;
					var w_child_last = ((w_parent - (w_child * (child_count -1)))-opts.minusWidth)-5;
				}
				$(this).children().css({ 'width' : w_child + 'px' });
				$(this).children(':last-child').css({ 'width' : w_child_last + 'px' });
				if((opts.stripPadding == 'child') || (opts.stripPadding == 'both')){
					$(this).children().css({
						'padding-right': '0',
						'padding-left': '0'
					});
				}
				if((opts.stripPadding == 'grand-child') || (opts.stripPadding == 'both')){
					$(this).children().children().css({
						'padding-right': '0',
						'padding-left': '0'
					});
				}
			}
		});
	};
})(jQuery);

(function($){
	$.fn.tabify = function(options) {
		var opts = $.extend({
			tabifyContainers: null,
			tabifyLinks: null
		}, options);
		return this.each(function(){
			var tabContainers=jQuery(opts.tabifyContainers);
			jQuery(opts.tabifyLinks).click(function(){
				tabContainers.hide().filter(this.hash).show();
				jQuery(opts.tabifyLinks).removeClass("active");
				jQuery(this).addClass("active");return false;
			}).filter(":first").click();
		});
	};
})(jQuery);

/* Animation Effects */
jQuery.fn.fadeToggle = function(speed, easing, callback) {
  return this.animate({opacity: 'toggle'}, speed, easing, callback);  
};
jQuery.fn.slideFadeToggle = function(speed, easing, callback) {
  return this.animate({opacity: 'toggle', height: 'toggle'}, speed, easing, callback);
};
jQuery.fn.blindToggle = function(speed, easing, callback) {
  var h = this.height() + parseInt(this.css('paddingTop')) + parseInt(this.css('paddingBottom'));
  return this.animate({marginTop: parseInt(this.css('marginTop')) < 0 ? 0 : -h}, speed, easing, callback);
};

//-- Vertical center function, also applied on Browser resize!
(function($){
	$.fn.vAlign = function() {
		return this.each(function(i){
			var ah = $(this).height();
			var ph = $(this).parent().height();
			var mh = (ph - ah) / 2;
			$(this).css('margin-top', mh);
		});
	};
})(jQuery);

//-- Horizontal center function, also applied on Browser resize!
(function ($) {
 $.fn.hAlign = function() {
  return this.each(function(i){
    var w = $(this).width();
    var ow = $(this).outerWidth();
    var ml = (w + (ow - w)) / 2;
    $(this).css("margin-left", "-" + ml + "px");
    $(this).css("left", "50%");
    $(this).css("position", "absolute");
  });
 };
})(jQuery);

jQuery.easing['jswing']=jQuery.easing['swing'];jQuery.extend(jQuery.easing,{def:'easeOutQuad',swing:function(x,t,b,c,d){return jQuery.easing[jQuery.easing.def](x,t,b,c,d)},easeInQuad:function(x,t,b,c,d){return c*(t/=d)*t+b},easeOutQuad:function(x,t,b,c,d){return-c*(t/=d)*(t-2)+b},easeInOutQuad:function(x,t,b,c,d){if((t/=d/2)<1)return c/2*t*t+b;return-c/2*((--t)*(t-2)-1)+b},easeInCubic:function(x,t,b,c,d){return c*(t/=d)*t*t+b},easeOutCubic:function(x,t,b,c,d){return c*((t=t/d-1)*t*t+1)+b},easeInOutCubic:function(x,t,b,c,d){if((t/=d/2)<1)return c/2*t*t*t+b;return c/2*((t-=2)*t*t+2)+b},easeInQuart:function(x,t,b,c,d){return c*(t/=d)*t*t*t+b},easeOutQuart:function(x,t,b,c,d){return-c*((t=t/d-1)*t*t*t-1)+b},easeInOutQuart:function(x,t,b,c,d){if((t/=d/2)<1)return c/2*t*t*t*t+b;return-c/2*((t-=2)*t*t*t-2)+b},easeInQuint:function(x,t,b,c,d){return c*(t/=d)*t*t*t*t+b},easeOutQuint:function(x,t,b,c,d){return c*((t=t/d-1)*t*t*t*t+1)+b},easeInOutQuint:function(x,t,b,c,d){if((t/=d/2)<1)return c/2*t*t*t*t*t+b;return c/2*((t-=2)*t*t*t*t+2)+b},easeInSine:function(x,t,b,c,d){return-c*Math.cos(t/d*(Math.PI/2))+c+b},easeOutSine:function(x,t,b,c,d){return c*Math.sin(t/d*(Math.PI/2))+b},easeInOutSine:function(x,t,b,c,d){return-c/2*(Math.cos(Math.PI*t/d)-1)+b},easeInExpo:function(x,t,b,c,d){return(t==0)?b:c*Math.pow(2,10*(t/d-1))+b},easeOutExpo:function(x,t,b,c,d){return(t==d)?b+c:c*(-Math.pow(2,-10*t/d)+1)+b},easeInOutExpo:function(x,t,b,c,d){if(t==0)return b;if(t==d)return b+c;if((t/=d/2)<1)return c/2*Math.pow(2,10*(t-1))+b;return c/2*(-Math.pow(2,-10*--t)+2)+b},easeInCirc:function(x,t,b,c,d){return-c*(Math.sqrt(1-(t/=d)*t)-1)+b},easeOutCirc:function(x,t,b,c,d){return c*Math.sqrt(1-(t=t/d-1)*t)+b},easeInOutCirc:function(x,t,b,c,d){if((t/=d/2)<1)return-c/2*(Math.sqrt(1-t*t)-1)+b;return c/2*(Math.sqrt(1-(t-=2)*t)+1)+b},easeInElastic:function(x,t,b,c,d){var s=1.70158;var p=0;var a=c;if(t==0)return b;if((t/=d)==1)return b+c;if(!p)p=d*.3;if(a<Math.abs(c)){a=c;var s=p/4}else var s=p/(2*Math.PI)*Math.asin(c/a);return-(a*Math.pow(2,10*(t-=1))*Math.sin((t*d-s)*(2*Math.PI)/p))+b},easeOutElastic:function(x,t,b,c,d){var s=1.70158;var p=0;var a=c;if(t==0)return b;if((t/=d)==1)return b+c;if(!p)p=d*.3;if(a<Math.abs(c)){a=c;var s=p/4}else var s=p/(2*Math.PI)*Math.asin(c/a);return a*Math.pow(2,-10*t)*Math.sin((t*d-s)*(2*Math.PI)/p)+c+b},easeInOutElastic:function(x,t,b,c,d){var s=1.70158;var p=0;var a=c;if(t==0)return b;if((t/=d/2)==2)return b+c;if(!p)p=d*(.3*1.5);if(a<Math.abs(c)){a=c;var s=p/4}else var s=p/(2*Math.PI)*Math.asin(c/a);if(t<1)return-.5*(a*Math.pow(2,10*(t-=1))*Math.sin((t*d-s)*(2*Math.PI)/p))+b;return a*Math.pow(2,-10*(t-=1))*Math.sin((t*d-s)*(2*Math.PI)/p)*.5+c+b},easeInBack:function(x,t,b,c,d,s){if(s==undefined)s=1.70158;return c*(t/=d)*t*((s+1)*t-s)+b},easeOutBack:function(x,t,b,c,d,s){if(s==undefined)s=1.70158;return c*((t=t/d-1)*t*((s+1)*t+s)+1)+b},easeInOutBack:function(x,t,b,c,d,s){if(s==undefined)s=1.70158;if((t/=d/2)<1)return c/2*(t*t*(((s*=(1.525))+1)*t-s))+b;return c/2*((t-=2)*t*(((s*=(1.525))+1)*t+s)+2)+b},easeInBounce:function(x,t,b,c,d){return c-jQuery.easing.easeOutBounce(x,d-t,0,c,d)+b},easeOutBounce:function(x,t,b,c,d){if((t/=d)<(1/2.75)){return c*(7.5625*t*t)+b}else if(t<(2/2.75)){return c*(7.5625*(t-=(1.5/2.75))*t+.75)+b}else if(t<(2.5/2.75)){return c*(7.5625*(t-=(2.25/2.75))*t+.9375)+b}else{return c*(7.5625*(t-=(2.625/2.75))*t+.984375)+b}},easeInOutBounce:function(x,t,b,c,d){if(t<d/2)return jQuery.easing.easeInBounce(x,t*2,0,c,d)*.5+b;return jQuery.easing.easeOutBounce(x,t*2-d,0,c,d)*.5+c*.5+b}});

/*
 * Poshy Tip jQuery plugin v1.0
 * http://vadikom.com/tools/poshy-tip-jquery-plugin-for-stylish-tooltips/
 * Copyright 2010, Vasil Dinkov, http://vadikom.com/
 */
(function(e){var a=[],d=/^url\(["']?([^"'\)]*)["']?\);?$/i,c=/\.png$/i,b=e.browser.msie&&e.browser.version==6;function f(){e.each(a,function(){this.refresh(true)})}e(window).resize(f);e.Poshytip=function(h,g){this.$elm=e(h);this.opts=e.extend({},e.fn.poshytip.defaults,g);this.$tip=e(['<div class="',this.opts.className,'">','<div class="tip-inner tip-bg-image"></div>','<div class="tip-arrow tip-arrow-top tip-arrow-right tip-arrow-bottom tip-arrow-left"></div>',"</div>"].join(""));this.$arrow=this.$tip.find("div.tip-arrow");this.$inner=this.$tip.find("div.tip-inner");this.disabled=false;this.init()};e.Poshytip.prototype={init:function(){a.push(this);this.$elm.data("title.poshytip",this.$elm.attr("title")).data("poshytip",this);switch(this.opts.showOn){case"hover":this.$elm.bind({"mouseenter.poshytip":e.proxy(this.mouseenter,this),"mouseleave.poshytip":e.proxy(this.mouseleave,this)});if(this.opts.alignTo=="cursor"){this.$elm.bind("mousemove.poshytip",e.proxy(this.mousemove,this))}if(this.opts.allowTipHover){this.$tip.hover(e.proxy(this.clearTimeouts,this),e.proxy(this.hide,this))}break;case"focus":this.$elm.bind({"focus.poshytip":e.proxy(this.show,this),"blur.poshytip":e.proxy(this.hide,this)});break}},mouseenter:function(g){if(this.disabled){return true}this.clearTimeouts();this.$elm.attr("title","");this.showTimeout=setTimeout(e.proxy(this.show,this),this.opts.showTimeout)},mouseleave:function(){if(this.disabled){return true}this.clearTimeouts();this.$elm.attr("title",this.$elm.data("title.poshytip"));this.hideTimeout=setTimeout(e.proxy(this.hide,this),this.opts.hideTimeout)},mousemove:function(g){if(this.disabled){return true}this.eventX=g.pageX;this.eventY=g.pageY;if(this.opts.followCursor&&this.$tip.data("active")){this.calcPos();this.$tip.css({left:this.pos.l,top:this.pos.t});if(this.pos.arrow){this.$arrow[0].className="tip-arrow tip-arrow-"+this.pos.arrow}}},show:function(){if(this.disabled||this.$tip.data("active")){return}this.reset();this.update();this.display()},hide:function(){if(this.disabled||!this.$tip.data("active")){return}this.display(true)},reset:function(){this.$tip.queue([]).detach().css("visibility","hidden").data("active",false);this.$inner.find("*").poshytip("hide");if(this.opts.fade){this.$tip.css("opacity",this.opacity)}this.$arrow[0].className="tip-arrow tip-arrow-top tip-arrow-right tip-arrow-bottom tip-arrow-left"},update:function(i){if(this.disabled){return}var h=i!==undefined;if(h){if(!this.$tip.data("active")){return}}else{i=this.opts.content}this.$inner.contents().detach();var g=this;this.$inner.append(typeof i=="function"?i.call(this.$elm[0],function(j){g.update(j)}):i=="[title]"?this.$elm.data("title.poshytip"):i);this.refresh(h)},refresh:function(h){if(this.disabled){return}if(h){if(!this.$tip.data("active")){return}var k={left:this.$tip.css("left"),top:this.$tip.css("top")}}this.$tip.css({left:0,top:0}).appendTo(document.body);if(this.opacity===undefined){this.opacity=this.$tip.css("opacity")}var l=this.$tip.css("background-image").match(d),m=this.$arrow.css("background-image").match(d);if(l){var i=c.test(l[1]);if(b&&i){this.$tip.css("background-image","none");this.$inner.css({margin:0,border:0,padding:0});l=i=false}else{this.$tip.prepend('<table border="0" cellpadding="0" cellspacing="0"><tr><td class="tip-top tip-bg-image" colspan="2"><span></span></td><td class="tip-right tip-bg-image" rowspan="2"><span></span></td></tr><tr><td class="tip-left tip-bg-image" rowspan="2"><span></span></td><td></td></tr><tr><td class="tip-bottom tip-bg-image" colspan="2"><span></span></td></tr></table>').css({border:0,padding:0,"background-image":"none","background-color":"transparent"}).find(".tip-bg-image").css("background-image",'url("'+l[1]+'")').end().find("td").eq(3).append(this.$inner)}if(i&&!e.support.opacity){this.opts.fade=false}}if(m&&!e.support.opacity){if(b&&c.test(m[1])){m=false;this.$arrow.css("background-image","none")}this.opts.fade=false}var o=this.$tip.find("table");if(b){this.$tip[0].style.width="";o.width("auto").find("td").eq(3).width("auto");var n=this.$tip.width(),j=parseInt(this.$tip.css("min-width")),g=parseInt(this.$tip.css("max-width"));if(!isNaN(j)&&n<j){n=j}else{if(!isNaN(g)&&n>g){n=g}}this.$tip.add(o).width(n).eq(0).find("td").eq(3).width("100%")}else{if(o[0]){o.width("auto").find("td").eq(3).width("auto").end().end().width(this.$tip.width()).find("td").eq(3).width("100%")}}this.tipOuterW=this.$tip.outerWidth();this.tipOuterH=this.$tip.outerHeight();this.calcPos();if(m&&this.pos.arrow){this.$arrow[0].className="tip-arrow tip-arrow-"+this.pos.arrow;this.$arrow.css("visibility","inherit")}if(h){this.$tip.css(k).animate({left:this.pos.l,top:this.pos.t},200)}else{this.$tip.css({left:this.pos.l,top:this.pos.t})}},display:function(h){var i=this.$tip.data("active");if(i&&!h||!i&&h){return}this.$tip.stop();if((this.opts.slide&&this.pos.arrow||this.opts.fade)&&(h&&this.opts.hideAniDuration||!h&&this.opts.showAniDuration)){var m={},l={};if(this.opts.slide&&this.pos.arrow){var k,g;if(this.pos.arrow=="bottom"||this.pos.arrow=="top"){k="top";g="bottom"}else{k="left";g="right"}var j=parseInt(this.$tip.css(k));m[k]=j+(h?0:this.opts.slideOffset*(this.pos.arrow==g?-1:1));l[k]=j+(h?this.opts.slideOffset*(this.pos.arrow==g?1:-1):0)}if(this.opts.fade){m.opacity=h?this.$tip.css("opacity"):0;l.opacity=h?0:this.opacity}this.$tip.css(m).animate(l,this.opts[h?"hideAniDuration":"showAniDuration"])}h?this.$tip.queue(e.proxy(this.reset,this)):this.$tip.css("visibility","inherit");this.$tip.data("active",!i)},disable:function(){this.reset();this.disabled=true},enable:function(){this.disabled=false},destroy:function(){this.reset();this.$tip.remove();this.$elm.unbind("poshytip").removeData("title.poshytip").removeData("poshytip");a.splice(e.inArray(this,a),1)},clearTimeouts:function(){if(this.showTimeout){clearTimeout(this.showTimeout);this.showTimeout=0}if(this.hideTimeout){clearTimeout(this.hideTimeout);this.hideTimeout=0}},calcPos:function(){var n={l:0,t:0,arrow:""},h=e(window),k={l:h.scrollLeft(),t:h.scrollTop(),w:h.width(),h:h.height()},p,j,m,i,q,g;if(this.opts.alignTo=="cursor"){p=j=m=this.eventX;i=q=g=this.eventY}else{var o=this.$elm.offset(),l={l:o.left,t:o.top,w:this.$elm.outerWidth(),h:this.$elm.outerHeight()};p=l.l+(this.opts.alignX!="inner-right"?0:l.w);j=p+Math.floor(l.w/2);m=p+(this.opts.alignX!="inner-left"?l.w:0);i=l.t+(this.opts.alignY!="inner-bottom"?0:l.h);q=i+Math.floor(l.h/2);g=i+(this.opts.alignY!="inner-top"?l.h:0)}switch(this.opts.alignX){case"right":case"inner-left":n.l=m+this.opts.offsetX;if(n.l+this.tipOuterW>k.l+k.w){n.l=k.l+k.w-this.tipOuterW}if(this.opts.alignX=="right"||this.opts.alignY=="center"){n.arrow="left"}break;case"center":n.l=j-Math.floor(this.tipOuterW/2);if(n.l+this.tipOuterW>k.l+k.w){n.l=k.l+k.w-this.tipOuterW}else{if(n.l<k.l){n.l=k.l}}break;default:n.l=p-this.tipOuterW-this.opts.offsetX;if(n.l<k.l){n.l=k.l}if(this.opts.alignX=="left"||this.opts.alignY=="center"){n.arrow="right"}}switch(this.opts.alignY){case"bottom":case"inner-top":n.t=g+this.opts.offsetY;if(!n.arrow||this.opts.alignTo=="cursor"){n.arrow="top"}if(n.t+this.tipOuterH>k.t+k.h){n.t=i-this.tipOuterH-this.opts.offsetY;if(n.arrow=="top"){n.arrow="bottom"}}break;case"center":n.t=q-Math.floor(this.tipOuterH/2);if(n.t+this.tipOuterH>k.t+k.h){n.t=k.t+k.h-this.tipOuterH}else{if(n.t<k.t){n.t=k.t}}break;default:n.t=i-this.tipOuterH-this.opts.offsetY;if(!n.arrow||this.opts.alignTo=="cursor"){n.arrow="bottom"}if(n.t<k.t){n.t=g+this.opts.offsetY;if(n.arrow=="bottom"){n.arrow="top"}}}this.pos=n}};e.fn.poshytip=function(g){if(typeof g=="string"){return this.each(function(){var i=e(this).data("poshytip");if(i&&i[g]){i[g]()}})}var h=e.extend({},e.fn.poshytip.defaults,g);if(!e("#poshytip-css-"+h.className)[0]){e(['<style id="poshytip-css-',h.className,'" type="text/css">',"div.",h.className,"{visibility:hidden;position:absolute;top:0;left:0;}","div.",h.className," table, div.",h.className," td{margin:0;font-family:inherit;font-size:inherit;font-weight:inherit;font-style:inherit;font-variant:inherit;}","div.",h.className," td.tip-bg-image span{display:block;font:1px/1px sans-serif;height:",h.bgImageFrameSize,"px;width:",h.bgImageFrameSize,"px;overflow:hidden;}","div.",h.className," td.tip-right{background-position:100% 0;}","div.",h.className," td.tip-bottom{background-position:100% 100%;}","div.",h.className," td.tip-left{background-position:0 100%;}","div.",h.className," div.tip-inner{background-position:-",h.bgImageFrameSize,"px -",h.bgImageFrameSize,"px;}","div.",h.className," div.tip-arrow{visibility:hidden;position:absolute;overflow:hidden;font:1px/1px sans-serif;}","</style>"].join("")).appendTo("head")}return this.each(function(){new e.Poshytip(this,h)})};e.fn.poshytip.defaults={content:"[title]",className:"tip-yellow",bgImageFrameSize:10,showTimeout:500,hideTimeout:100,showOn:"hover",alignTo:"cursor",alignX:"right",alignY:"top",offsetX:-22,offsetY:18,allowTipHover:true,followCursor:false,fade:true,slide:true,slideOffset:8,showAniDuration:300,hideAniDuration:300}})(jQuery);

/**
 * CSS Selectors for browser specific CSS
 */
function css_browser_selector(u){var ua = u.toLowerCase(),is=function(t){return ua.indexOf(t)>-1;},g='gecko',w='webkit',s='safari',o='opera',h=document.getElementsByTagName('html')[0],b=[(!(/opera|webtv/i.test(ua))&&/msie\s(\d)/.test(ua))?('ie ie'+RegExp.$1):is('firefox/2')?g+' ff2':is('firefox/3.5')?g+' ff3 ff3_5':is('firefox/3')?g+' ff3':is('gecko/')?g:is('opera')?o+(/version\/(\d+)/.test(ua)?' '+o+RegExp.$1:(/opera(\s|\/)(\d+)/.test(ua)?' '+o+RegExp.$2:'')):is('konqueror')?'konqueror':is('chrome')?w+' chrome':is('iron')?w+' iron':is('applewebkit/')?w+' '+s+(/version\/(\d+)/.test(ua)?' '+s+RegExp.$1:''):is('mozilla/')?g:'',is('j2me')?'mobile':is('iphone')?'iphone':is('ipod')?'ipod':is('mac')?'mac':is('darwin')?'mac':is('webtv')?'webtv':is('win')?'win':is('freebsd')?'freebsd':(is('x11')||is('linux'))?'linux':'','js']; c = b.join(' '); h.className += ' '+c; return c;}; css_browser_selector(navigator.userAgent);

function equalHeight(group) {
  var tallest = 0;
  group.each(function() {
    var thisHeight = jQuery(this).height();
      if(thisHeight > tallest) {
				tallest = thisHeight;
      }
  });
  group.height(tallest);
}

function equalWidth(group) {
  var widest = 0;
  group.each(function() {
    var thisWidth = jQuery(this).width();
      if(thisWidth > widest) {
				widest = thisWidth;
      }
  });
  group.width(widest);
}

function smoothScroll(scrollElement){
  jQuery(scrollElement).ready(function(){
   var destination = jQuery(scrollElement).offset().top;
   jQuery("html:not(:animated),body:not(:animated)").animate({ scrollTop: destination-20}, 2000 );
  });
}

function $cd(vDebug){console.debug(vDebug);}

jQuery(document).ready(function(){
	ZebraTables();ZebraUL();BlurFocusText();
	equalHeight(jQuery(".eqh"));
	equalWidth(jQuery(".eqw"));
  /* Accordions */
  try{
    
    
  } catch (err){}
  jQuery("#main-contents .event-filters-extended ul#outline-titles li, #main-contents #col-left .locales #outline-briefs ul#outline-titles li, #main-contents #col-left .eventos .eventos-outline ul#outline-titles li").each(function(){
    var w = jQuery(this).width();
    var ow = jQuery(this).outerWidth();
    var ml = (w + (ow - w)) / 2;
    jQuery(this).find('div.pointer-tip').css("margin-left", (ml-8) + "px");
  });
  jQuery("a[rel=external]").each(function(){jQuery(this).attr('target', '_blank');});
	
    /*
	jQuery('ul.photo-teaser-cycle').cycle({
		fx: 'scrollHorz',
		speed: 1000,
		timeout: 0,
		sync: 1,
		activePagerClass: 'active', //-- class name used for the active pager link
		easing: 'easeInOutBack',
		containerResize: 1,
    pager:  'ul.carousel-images li ul.carousel-slide',
    pagerAnchorBuilder: function(idx, slide) {
     //-- return selector string for existing anchor
     return 'ul.carousel-images li ul.carousel-slide li:eq(' + idx + ') a'; 
    },
		delay: -2000
	});
	jQuery('ul.photo-teaser-cycle').cycle({
		fx: 'scrollHorz',
		speed: 1000,
		timeout: 0,
		sync: 1,
		activePagerClass: 'active', //-- class name used for the active pager link
		easing: 'easeInOutBack',
		containerResize: 1,
    pager:  'ul.carousel-images li ul.carousel-slide',
    pagerAnchorBuilder: function(idx, slide) {
     //-- return selector string for existing anchor
     return 'ul.carousel-images li ul.carousel-slide li:eq(' + idx + ') a'; 
    },
		delay: -2000
	});
	*/
    
  /* Events Tabs */
//	jQuery('#main-contents .merged-contents ul.event-tab-contents').cycle({
//		fx: 'fade',
//		speed: 10,
//		timeout: 0,
//		sync: 1,
//		activePagerClass: 'active', //-- class name used for the active pager link
//    pager: '#main-contents .merged-contents .event-filters-extended ul#outline-titles',
//		cleartypeNoBg: true,
//		containerResize: 1,
//    pagerAnchorBuilder: function(idx, slide) {
//     //-- return selector string for existing anchor
//     return '#main-contents .merged-contents .event-filters-extended ul#outline-titles li:eq(' + idx + ') a';
//    },
//		updateActivePagerLink: function(pager, currSlideIndex) {
//			$(pager).find('li').removeClass('active')
//				.filter('li:eq('+currSlideIndex+')').addClass('active');
//			$(pager).find('li').find('div.pointer-tip').hide();
//			$(pager).find('li:eq('+currSlideIndex+')').find('div.pointer-tip').show();
//		},
//		delay: -2
//	});
	
	jQuery('.equal-width').equalWidths({'stripPadding': 'child', 'minusWidth': 4});
  //jQuery('.equal-width').equalWidths({'stripPadding': 'both'});
	jQuery('#latest-photos ul#tab-photo-outline').tabify({
    tabifyContainers: '#latest-photos div.tab-parts',
    tabifyLinks: '#latest-photos ul#tab-photo-outline li a'
  });
	jQuery('.vcenter').vAlign();
	jQuery(window).bind('resize', function(){jQuery('.vcenter').vAlign();});
/*	
	jQuery('#main-contents #col-right #whats-today .box-contents ul.recent li a, #main-contents #col-right .more-news ol li a,#main-contents #col-left .node-mini-right .other-news li a, #main-contents #col-left h5.red-title a, #main-contents #col-left .locales .events-duo ul li a')
	.poshytip({
		content: '<img width="80" height="70" alt="imgs_6" src="images/content/imgs_9.jpg"> And the day came when the risk<br />to remain tight in a bud became<br />more painful than the risk<br />it took to blossom.',
    	showTimeout: 10,
    	fade: false,
    	slide: false,
		className: 'tip-darkgray',
		bgImageFrameSize: 11,
		offsetX: -5,
		offsetY: 10
	});
	*/
	
	
});

(function ($) {
// VERTICALLY ALIGN FUNCTION
$.fn.vAlign = function() {
	return this.each(function(i){
	var ah = $(this).height();
	var ph = $(this).parent().height();
	var mh = Math.ceil((ph-ah) / 2);
	$(this).parent().css('padding-top', mh);
	});
};
})(jQuery);

jQuery(window).load(function(){
	if(jQuery('#facebook-like-box').children().children('span').css('width') == '0px'){
		jQuery('#facebook-like-box').hide();
		
		var margin = 0;
		var height_banner = parseInt(jQuery('#new-theme-long-banner').offset().top) + parseInt(jQuery('#new-theme-long-banner').css('height'));
		var height_your_photos = parseInt(jQuery('.your-photos-main-box').offset().top) + parseInt(jQuery('.your-photos-main-box').css('height'));
		margin = height_banner - parseInt(jQuery('.your-photos-main-box').offset().top) + 75;
		if((height_banner - height_your_photos) >= 5)
			jQuery('.your-photos-main-box').css('margin-top',margin);
		
		margin = 0;
		margin = jQuery('.new-theme-videos-box').offset().top - jQuery('#add-below-yourphotos-box').offset().top;
		margin = margin + 25;
		if(margin > 0)
			jQuery('#add-below-yourphotos-box').css('margin-top',margin);
	}
	else{
		var margin = 0;
		var facebook_likebox_height = parseInt(jQuery('#facebook-like-box').offset().top) + parseInt(jQuery('#facebook-like-box').css('height'));
		var banner_start = parseInt(jQuery('#new-theme-long-banner').offset().top);
		if(facebook_likebox_height > banner_start) {
			margin = banner_start - parseInt(jQuery('#facebook-like-box').offset().top);
			jQuery('#facebook-like-box').css('margin-top', margin + 25);
		}
		
		margin = 0;
		margin = jQuery('.new-theme-videos-box').offset().top - jQuery('.your-photos-main-box').offset().top;
		margin = margin + 55;
		if(margin > 0)
			jQuery('.your-photos-main-box').css('margin-top',margin);
		
//		margin = 0;facebook-like-box
//		var height_banner = parseInt(jQuery('#new-theme-long-banner').offset().top) + parseInt(jQuery('#new-theme-long-banner').css('height'));
//		var height_your_photos = parseInt(jQuery('.your-photos-main-box').offset().top) + parseInt(jQuery('.your-photos-main-box').css('height'));
//		margin = height_banner + parseInt(jQuery('.your-photos-main-box').offset().top) + 20;
//		if((height_banner - height_your_photos) >= 5)
//			jQuery('.your-photos-main-box').css('margin-top',margin);
	}
	
	
	
	//jQuery('#add-below-yourphotos-box').offset({top: jQuery('.new-theme-videos-box').offset().top, left: jQuery('#add-below-yourphotos-box').offset().left});
});

