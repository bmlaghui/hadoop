function itemRatting() {
    $.fn.duplicate = function (t, a) {
        for (var i = [], n = 0; n < t; n++) $.merge(i, this.clone(a).get());
        return this.pushStack(i)
    }, $(".item-ratting").each(function (t) {
        var a = $(this).attr("data-star-rating");
        $("<i class='la la-star'></i>").duplicate(a).prependTo(this)
    })
}