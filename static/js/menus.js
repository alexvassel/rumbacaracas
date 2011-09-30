/**
+------------------------------------------------------------------------------------------+
COMPANY: Raven Developers 2010
+------------------------------------------------------------------------------------------+
FILE INFO: Menu system Java Script
+------------------------------------------------------------------------------------------+
WEBSITE: http://www.ravendevelopers.com
+------------------------------------------------------------------------------------------+
Portions created by Anirudh K. Mahant are Copyright of Raven Developers (C) 2010.
+------------------------------------------------------------------------------------------+
COPYRIGHT NOTICE:
The contents of this file are protected and copyrighted and are subject to
the original developer(s) of this file;Unauthorised use of this file is strictly prohibited.	
+------------------------------------------------------------------------------------------+
*/

jQuery.fn.getBox = function() {
  try{
    return {
        left: $(this).offset().left,
        top: $(this).offset().top,
        width: $(this).outerWidth(),
        height: $(this).outerHeight()
    };
  } catch(e){};
}

jQuery.fn.position = function(target, options) {

  try{
    var anchorOffsets = {t: 0, l: 0, c: 0.5, b: 1, r: 1};
    var defaults = {
      anchor: ['tl', 'tl'],
      animate: false,
      offset: [0, 0]
    };
    options = $.extend(defaults, options);
    var targetBox = $(target).getBox();
    var sourceBox = $(this).getBox();
    //-- Origin is at the top-left of the target element
    var left = targetBox.left;
    var top = targetBox.top;
    //-- Alignment with respect to source
    top -= anchorOffsets[options.anchor[0].charAt(0)] * sourceBox.height;
    left -= anchorOffsets[options.anchor[0].charAt(1)] * sourceBox.width;
    //-- Alignment with respect to target
    top += anchorOffsets[options.anchor[1].charAt(0)] * targetBox.height;
    left += anchorOffsets[options.anchor[1].charAt(1)] * targetBox.width;
    //-- Add offset to final coordinates
    left += options.offset[0];
    top += options.offset[1];
    $(this).css({
      left: left + 'px',
      top: top + 'px'
    });
  } catch(e){};
}

var jmenu={
	effect: 'fade', /* default animation effect */
	duration: 400,  /* default duration */
  behaviour: 'onmouseover',  /* default behaviour of menu */
	set: function (settings){
	 try{
     switch(settings.animation){
       case 'show':
         this.effect = 'show';
         break;
       case 'slide':
         this.effect = 'slide';
         break;
       case 'fade':
         this.effect = 'fade';
         break;
       case 'smoothslide':
         this.effect = 'smoothslide';
         break;
     }
		} catch (e) {}
		try{
			this.duration=settings.duration;
			this.sensitivity = settings.sensitivity;
			this.interval = settings.interval;
			this.timeout = settings.timeout;
      this.behaviour = settings.behaviour;
      this.anchor = settings.anchor;
		} catch (e) {}
	},
	fix_pos:function(elem){
//		if ($(elem).parent('ul').parent('li').length){
//			$(elem).children('ul').eq(0).css({marginTop:-$(elem).height(),marginLeft:$(elem).width()});
//		} else{
//			$(elem).children('ul').eq(0).css({'top':$(elem).offset().top+$(elem).height(),'left':$(elem).offset().left});
//		}
    if (this.anchor){
      $(elem).children('ul').eq(0).position($(elem), {
  //      anchor: ['tr', 'br'],
        anchor: this.anchor,
        offset: [0, 0]
      });
    }
    
		$(elem).children('ul').eq(0).hover(
			function(){$(this).parents('li').find('a').eq(0).addClass('active');},
			function(){$(this).parents('li').find('a').eq(0).removeClass('active');}
		);
	},
	show:function(elem){
		try{
      $(elem).children('ul').eq(0).css('z-index', '999999');
      $(elem).find('div.menu-overlay').eq(0).css('z-index', '998');
			switch(this.effect){
				case 'fade':
					$(elem).children('ul').eq(0).stop(1,1).fadeIn(this.duration);
					break;
				case 'slide':
					$(elem).children('ul').eq(0).stop(1,1).slideDown(this.duration);
					break;
				case 'show':
//					$(elem).children('ul').eq(0).stop(1,1).show(this.duration);
//					$(elem).find('div.menu-overlay').eq(0).stop(1,1).show(this.duration);
					$(elem).children('ul').eq(0).css({display: "block", visibility: "visible" });
					break;
				case 'smoothslide':
					slideToggle($(elem).children('ul').eq(0), true, this.duration);
					break;
			}
		}catch(e){}
	},
	hide: function(elem){
		try{
      $(elem).children('ul').eq(0).css('z-index', '0');
			switch(this.effect){
				case 'fade':
					$(elem).children('ul').eq(0).stop(1,1).fadeOut(this.duration);
					break;
				case 'slide':
					$(elem).children('ul').eq(0).stop(1,1).slideUp(this.duration);
					break;
				case 'show':
//					$(elem).children('ul').eq(0).stop(1,1).hide(this.duration);
//					$(elem).find('div.menu-overlay').eq(0).stop(1,1).hide(this.duration);
					$(elem).children('ul').eq(0).css({display: "none", visibility: "hidden" });
					break;
				case 'smoothslide':
					slideToggle($(elem).children('ul').eq(0), false, this.duration); //.stop(1,1).slideUp({duration: this.duration, easing:easeEffectOut});
					break;
			}
		}catch(e){}		
	}
}

$.fn.jmenu=function(settings){
  $(this).find('li').each(function(){
    $(this).hover(function(){
      jmenu.set(settings);
      jmenu.fix_pos(this);
      jmenu.show(this);
    },function() {
      jmenu.hide(this);
    });
  });
//  if (settings.behaviour == 'onmouseover'){
//    alert('that was fuckin hard');
//    $(this).find('li').each(function(){
//      $(this).hover(function(){
//        jmenu.set(settings);
//        jmenu.fix_pos(this);
//        jmenu.show(this);
//      },function() {
//        jmenu.hide(this);
//      });
//    });
//  } else{
//    $(this).find('li').each(function(){
//      var config = {
//       sensitivity: settings.sensitivity, // number = sensitivity threshold (must be 1 or higher)
//       interval: settings.interval, // number = milliseconds for onMouseOver polling interval
//       over: function(){jmenu.set(settings);jmenu.fix_pos(this);jmenu.show(this);}, // function = onMouseOver callback (REQUIRED)
//       timeout: settings.timeout, // number = milliseconds delay before onMouseOut
//       out: function(){jmenu.hide(this);} // function = onMouseOut callback (REQUIRED)
//      };
//      $(this).hoverIntent(config);
//    });
//  }
  
//	$(this).find('li').each(function(){
//    if (settings.behaviour == 'onmouseover'){
//      alert('that was fuckin hard');
//      $(this).hover(function(){
//        $(this).toggle(function(){
//          jmenu.set(settings);
//          jmenu.fix_pos(this);
//          jmenu.show(this);
//        },function() {
//          jmenu.hide(this);
//        });
//      });
//    } else{
//      var config = {
//       sensitivity: settings.sensitivity, // number = sensitivity threshold (must be 1 or higher)
//       interval: settings.interval, // number = milliseconds for onMouseOver polling interval
//       over: function(){jmenu.set(settings);jmenu.fix_pos(this);jmenu.show(this);}, // function = onMouseOver callback (REQUIRED)
//       timeout: settings.timeout, // number = milliseconds delay before onMouseOut
//       out: function(){jmenu.hide(this);} // function = onMouseOut callback (REQUIRED)
//      };
//      $(this).hoverIntent(config);
//    }
//	});
}

// this is a fix for the $ slide effects
function slideToggle(el, bShow, slideDuration){
  var $el = $(el), height = $el.data("originalHeight"), visible = $el.is(":visible");
  // if the bShow isn't present, get the current visibility and reverse it
  if( arguments.length == 1 ) bShow = !visible;
  // if the current visiblilty is the same as the requested state, cancel
  if( bShow == visible ) return false;
  // get the original height
  if( !height ){
    // get original height
    height = $el.show().height();
    // update the height
    $el.data("originalHeight", height);
    // if the element was hidden, hide it again
    if( !visible ) $el.hide().css({height: 0});
  }
  // expand the knowledge (instead of slideDown/Up, use custom animation which applies fix)
  if( bShow ){
    $el.show().animate({height: height}, {duration: slideDuration});
  } else {
    $el.animate({height: 0}, {duration: slideDuration, complete:function (){
        $el.hide();
      }
    });
  }
}

$(document).ready(function(){
	$('ul#top-menu-primary').jmenu({animation:'show',duration:300,sensitivity:3,interval:100,timeout:100, behviour:'onmouseover'});
	$('ul#top-menu-tertiary').jmenu({animation:'show',duration:300,sensitivity:3,interval:10,timeout:50, behviour:'onmouseover'});
	$('ul#top-menu-secondary').jmenu({animation:'show',duration:300,sensitivity:3,interval:10,timeout:50, behviour:'onmouseover'});
  $('ul.teaser-options').jmenu({animation:'show',duration:1,sensitivity:1,interval:1,timeout:1,behviour:'onmouseover'});
  $('#main-contents #col-left .recent-events-list .teaser ul.teaser-options').jmenu({animation:'show',duration:1,sensitivity:1,interval:1,timeout:1,anchor:['tr', 'br'],behviour:'onmouseover'});
//	$('ul#top-menu-tertiary').find('li').each(function(){
//		var overlayWidth = $(this).find('a').eq(0).innerWidth();
//		var overlayHeight = $(this).find('a').eq(0).innerHeight() + $(this).children('ul').eq(0).innerHeight();
//		$(this).find('ul').eq(0).width(overlayWidth);
//		$(this).find('div.menu-overlay').width(overlayWidth);
//		$(this).find('div.menu-overlay').height(overlayHeight);
//	});


	$("ul.top-menu-secondary li.medios").mouseover(function( )
	{
		$(this).find("a").eq(0).css("color", "#F06001");
	});
	
	$("ul.top-menu-secondary li.medios").mouseout(function( )
	{
		$(this).find("a").eq(0).css("color", "#010101");
	});

	$("ul.top-menu-secondary li.medios ul").mouseover(function( )
	{
		$(this).parent( ).find("a").eq(0).css("color", "#F06001");
	});
	
	$("ul.top-menu-secondary li.medios ul").mouseout(function( )
	{
		$(this).parent( ).find("a").eq(0).css("color", "#010101");
	});

});