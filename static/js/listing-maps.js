!function (e) {
    "use strict";
    var t = {anchor: new google.maps.Point(10, 15), url: "images/map-marker.png"};
    var a = document.getElementById("myMap");
    void 0 !== a && null != a && google.maps.event.addDomListener(window, "load", function () {
        function a(e, t, a, l, s, i, o, n, r) {
            return '<div class="map-info-popup"><div class="item-popup-box"><span class="close-info"><i class="la la-close"></i></span><a href="#" class="map-badge">' + t + '</a><a href="' + e + '" class="map-img-box position-relative d-block"><img src="' + a + '" alt=""></a> <div class="item-list-content position-relative"><h4 class="mb-2"><a href=' + e + ">" + l + '</a></h4><div class="item-ratting mb-3" data-star-rating="' + n + '"><span class="map-review-count">' + r + ' reviews</span></div><span class="location-info d-block mb-2"><i class="la la-map-marker"></i>' + s + '</span><span class="item-call d-block mb-2"><i class="la la-phone"></i><a href="#">' + i + '</a></span><span class="item-call d-block"><i class="la la-clock-o"></i>' + o + "</span></div></div></div>"
        }

        var l = [[a("listing-details.html", "Restaurant", "images/img1.jpg", "Brenda French Soul Food", "121 Parkview, London ", "+1246-345-0695", " Open Now", "5", "27"), 42.5620277, 12.5930638, 0, t], [a("listing-details.html", "Travel", "images/img2.jpg", "The Blue Beach", "34 Parkview, New York", "+1246-345-0695", "Closed. Open at 6:30 AM - 11PM", "4", "12"), 24.6900406, 46.7109742, 0, t], [a("listing-details.html", "Hotel & Restaurant", "images/img1.jpg", "The Party Center", "181 Wellington Street, Toronto", "+1246-345-0695", "Now Open", "5", "52"), 43.6421237, -79.3803969, 0, t], [a("listing-details.html", "Travel", "images/img2.jpg", "Maldana Blue Beach Resort", "Montreal Street, Canada ", "+1246-345-0695", "Now Open", "5", "27"), 41.7948911, -88.0054919, 0, t], [a("listing-details.html", "Hotel", "images/img3.jpg", "Monopoly Rest the Center", "131 Esplanade, Toronto, Canada", "+1246-345-0695", "Closed. Open at 6:30 AM - 11PM", "5", "12"), 43.650005, -79.379946, 0, t], [a("listing-details.html", "Event", "images/img4.jpg", "Bodega Garage - Filipino Night Club", "10, Aberdeen, United Kingdom", "+1246-345-0695", "Now Open", "5", "12"), 40.7312782, -74.2170747, 0, t], [a("listing-details.html", "Hotels", "images/img5.jpg", "Luxary Rest Hotel", "370, Calgary, AB 3H7, Canada", "+1246-345-0695", "Now Open", "5", "17"), 543.651521, -79.37782, 0, t], [a("listing-details.html", "Gym", "images/img6.jpg", "Perform For Life - Hayes Valley", "London, United Kingdom", "+1246-345-0695", "Now Open", "5", "22"), 47.0962411, 2.4587676, 0, t], [a("listing-details.html", "Bear & Bar", "images/img7.jpg", "Collin Bear Bar", "2545 Montreal Street, Canada", "+1246-345-0695", "Closed. Open at 6:30 AM - 11PM", "4", "11"), 43.9959016, -72.6871069, 0, t], [a("listing-details.html", "Art & Design", "images/img8.jpg", "Kamran's Art & Design Center ", "323,Kamran Avenue, New York", "+1246-345-0695", "Now Open", "5", "12"), 24.691415, 46.7175295, 0, t], [a("listing-details.html", "Event and Conference", "images/img1.jpg", "Graphic Design Conference", "280 Adelaide St, Canada", "+1246-345-0695", "Open at 6:30 AM - 11PM", "5", "17"), 43.6477128, -79.3930809, 0, t], [a("listing-details.html", "Hotels", "images/img9.jpg", "Monolight Hotel", "40 Journal Square Plaza, NJ, USA", "+1246-345-0695", "Closed. Open at 6:30 AM - 11PM", "4", "32"), 41.0346449, 28.9776183, 0, t], [a("listing-details.html", "Hotels", "images/img10.jpg", "Moonlight Party Hotel", "40 Journal Square Plaza, NJ, USA", "+1246-345-0695", "Now Open", "5", "22"), 39.7449686, -88.6840435, 0, t], [a("listing-details.html", "Restaurants", "images/img1.jpg", "The Goggi Restaurant", "101 Intervale Ave, Bronx, NY, USA", "+1246-345-0695", "Closed. Open at 6:30 AM - 11PM", "4", "10"), 43.651521, -79.37782, 0, t], [a("listing-details.html", "Hotels", "images/img11.jpg", "New Year Eve Party", "102, Strasbourg, France", "+1246-345-0695", "Now Open", "4", "11"), 37.2582904, -102.6537497, 0, t], [a("listing-details.html", "Hotels", "images/img12.jpg", "New Year Eve Party", "102, Strasbourg, France", "+1246-345-0695", "Now Open", "5", "42"), 51.255512, 22.5733453, 0, t]],
            s = new google.maps.Map(document.getElementById("myMap"), {
                zoom: 3,
                scrollwheel: !1,
                center: new google.maps.LatLng(40.728157, -74.077644),
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                zoomControl: !0,
                mapTypeControl: !1,
                fullscreenControl: !0,
                styles: [{
                    featureType: "water",
                    elementType: "geometry",
                    stylers: [{color: "#e9e9e9"}, {lightness: 17}]
                }, {
                    featureType: "landscape",
                    elementType: "geometry",
                    stylers: [{color: "#f5f5f5"}, {lightness: 20}]
                }, {
                    featureType: "road.highway",
                    elementType: "geometry.fill",
                    stylers: [{color: "#ffffff"}, {lightness: 17}]
                }, {
                    featureType: "road.highway",
                    elementType: "geometry.stroke",
                    stylers: [{color: "#ffffff"}, {lightness: 29}, {weight: .2}]
                }, {
                    featureType: "road.arterial",
                    elementType: "geometry",
                    stylers: [{color: "#ffffff"}, {lightness: 18}]
                }, {
                    featureType: "road.local",
                    elementType: "geometry",
                    stylers: [{color: "#ffffff"}, {lightness: 16}]
                }, {
                    featureType: "poi",
                    elementType: "geometry",
                    stylers: [{color: "#f5f5f5"}, {lightness: 21}]
                }, {
                    featureType: "poi.park",
                    elementType: "geometry",
                    stylers: [{color: "#dedede"}, {lightness: 21}]
                }, {
                    elementType: "labels.text.stroke",
                    stylers: [{visibility: "on"}, {color: "#ffffff"}, {lightness: 16}]
                }, {
                    elementType: "labels.text.fill",
                    stylers: [{saturation: 36}, {color: "#333333"}, {lightness: 40}]
                }, {elementType: "labels.icon", stylers: [{visibility: "off"}]}, {
                    featureType: "transit",
                    elementType: "geometry",
                    stylers: [{color: "#f2f2f2"}, {lightness: 19}]
                }, {
                    featureType: "administrative",
                    elementType: "geometry.fill",
                    stylers: [{color: "#fefefe"}, {lightness: 20}]
                }, {
                    featureType: "administrative",
                    elementType: "geometry.stroke",
                    stylers: [{color: "#fefefe"}, {lightness: 17}, {weight: 1.2}]
                }]
            }), i = document.createElement("div");
        i.className = "map-info-box";
        var o, n, r = {
            content: i,
            disableAutoPan: !0,
            alignBottom: !0,
            pixelOffset: new google.maps.Size(-146, -35),
            boxStyle: {width: "310px"},
            closeBoxMargin: "0",
            closeBoxURL: ""
        }, g = [];
        for (n = 0; n < l.length; n++) {
            o = new google.maps.Marker({
                position: new google.maps.LatLng(l[n][1], l[n][2]),
                icon: l[n][4],
                id: n
            }), g.push(o);
            var m = new InfoBox;
            google.maps.event.addListener(m, "domready", function () {
                itemRatting()
            }), google.maps.event.addListener(o, "click", function (t, a) {
                return function () {
                    m.setOptions(r), i.innerHTML = l[a][0], m.close(), m.open(s, t), t.id;
                    var o = new google.maps.LatLng(l[a][1], l[a][2]);
                    s.panTo(o), s.panBy(0, -180), google.maps.event.addListener(m, "domready", function () {
                        e(".close-info").click(function (e) {
                            e.preventDefault(), m.close()
                        })
                    })
                }
            }(o, n))
        }
        new MarkerClusterer(s, g, {
            imagePath: "../images/",
            styles: [{textColor: "white", url: "", height: 50, width: 50}],
            minClusterSize: 2
        }), google.maps.event.addDomListener(window, "resize", function () {
            var e = s.getCenter();
            google.maps.event.trigger(s, "resize"), s.setCenter(e)
        });
        var p = e(".enable-scroll");
        e(p).on("click", function (t) {
            t.preventDefault(), e(this).toggleClass("enabled"), e(this).is(".enabled") ? s.setOptions({scrollwheel: !0}) : s.setOptions({scrollwheel: !1})
        })
    })
}(this.jQuery);