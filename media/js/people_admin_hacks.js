django.jQuery(document).ready(function () {
    django.jQuery('.file-upload a').each(function(){
        var el = django.jQuery(this);
        var length = el.text().length;
        if (length > 10) {
            el.css('display','block');
            el.text(el.text().substring(0,30))
        }
    })
})
