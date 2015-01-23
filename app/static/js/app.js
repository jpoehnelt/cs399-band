var map = L.map('map').setView([45.505, -95.09], 2);
L.tileLayer('https://{s}.tiles.mapbox.com/v4/jpoehnelt.l0lfh10a/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoianBvZWhuZWx0IiwiYSI6IklPWWxnd3cifQ.-BV62TCUw6DmQa7mbKmphA').addTo(map);

var markers = [];

for (var i = 0; i < 10; i++) {
    var marker = L.marker([Math.random()*(50-25)+28, Math.random()*(100-70)-115]).addTo(map);
}