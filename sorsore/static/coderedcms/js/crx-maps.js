/*
Wagtail CRX (https://www.coderedcorp.com/cms/)
Copyright 2018-2023 CodeRed LLC
License: https://github.com/coderedcorp/sorsore/blob/main/LICENSE
@license magnet:?xt=urn:btih:c80d50af7d3db9be66a4d0a86db0286e4fd33292&dn=bsd-3-clause.txt BSD-3-Clause
*/

/**
 * Initialize the map on the Gooogle Maps API js callback.
 */
function initMap() {
  const crMap = document.querySelector("#cr-map");
  // Set defaults
  const map = new google.maps.Map(crMap, {
    zoom: parseInt(crMap.dataset.zoom),
    center: {
      lat: parseFloat(crMap.dataset.latitude),
      lng: parseFloat(crMap.dataset.longitude),
    },
    mapTypeControl: crMap.dataset.mapTypeControl,
    streetViewControl: crMap.dataset.streetViewControl,
  });
  // Create an infowindow object.
  var infowindow = new google.maps.InfoWindow({});

  if (navigator.geolocation) {
    var currentLocationControlDiv = document.createElement("div");
    var currentLocation = new CurrentLocationControl(
      currentLocationControlDiv,
      map
    );

    currentLocationControlDiv.index = 1;
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(
      currentLocationControlDiv
    );
  }

  // Listener to update the map markers when the map is idling.
  google.maps.event.addListener(map, "idle", () => {
    const sw = map.getBounds().getSouthWest();
    const ne = map.getBounds().getNorthEast();
    let locationDataFeatures = [];
    map.data.loadGeoJson(
      crMap.dataset.geojsonUrl +
        `&viewport=${sw.lat()},${sw.lng()}|${ne.lat()},${ne.lng()}`,
      null,
      (features) => {
        locationDataFeatures.forEach((dataFeature) => {
          map.data.remove(dataFeature);
        });
        locationDataFeatures = features;
        if (crMap.dataset.showList == "True") {
          updateList(locationDataFeatures);
        }
      }
    );
  });

  // Listener to update the info window when a marker is clicked.
  map.data.addListener("click", (ev) => {
    const f = ev.feature;
    infowindow.setContent(f.getProperty("pin_description"));
    infowindow.setPosition(f.getGeometry().get());
    infowindow.setOptions({
      pixelOffset: new google.maps.Size(0, -30),
    });
    infowindow.open(map);
  });

  // Logic to create a search box and move the map on successful search.

  if (crMap.dataset.showSearch == "True") {
    var input = document.getElementById("pac-input");
    var searchBox = new google.maps.places.SearchBox(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    map.addListener("bounds_changed", function () {
      searchBox.setBounds(map.getBounds());
    });
    searchBox.addListener("places_changed", function () {
      var places = searchBox.getPlaces();
      if (places.length == 0) {
        return;
      }
      // For each place, get the icon, name and location.
      var bounds = new google.maps.LatLngBounds();
      places.forEach(function (place) {
        if (!place.geometry) {
          return;
        }
        if (place.geometry.viewport) {
          // Only geocodes have viewport.
          bounds.union(place.geometry.viewport);
        } else {
          bounds.extend(place.geometry.location);
        }
      });
      map.fitBounds(bounds);
    });
  }

  // Updates the list to the side of the map with markers that are in the viewport.
  function updateList(features) {
    locList = document.querySelector("#LocationList");
    locListEmpty = document.querySelector("#LocationListEmpty");
    new_html = "";
    if (features.length == 0) {
      locList.style.display = "none";
      locListEmpty.style.display = "";
    } else {
      locList.style.display = "";
      locListEmpty.style.display = "none";
      for (i = 0; i < features.length; i++) {
        feature = features[i];
        new_html += feature.getProperty("list_description");
      }
    }
    locList.innerHTML = new_html;
  }
}

function CurrentLocationControl(controlDiv, map) {
  var controlUI = document.createElement("div");
  controlUI.style.backgroundColor = "#fff";
  controlUI.style.border = "2px solid #fff";
  controlUI.style.borderRadius = "3px";
  controlUI.style.boxShadow = "0 2px 2px rgba(0,0,0,.3)";
  controlUI.style.cursor = "pointer";
  controlUI.style.marginTop = "10px";
  controlUI.style.marginBottom = "22px";
  controlUI.style.marginLeft = "10px";
  controlUI.style.textAlign = "center";
  controlUI.title = "Near Me";
  controlDiv.appendChild(controlUI);

  // Set CSS for the control interior.
  var controlText = document.createElement("div");
  controlText.style.color = "rgb(25,25,25)";
  controlText.style.fontFamily = "Roboto,Arial,sans-serif";
  controlText.style.fontSize = "16px";
  controlText.style.lineHeight = "36px";
  controlText.style.paddingLeft = "5px";
  controlText.style.paddingRight = "5px";
  controlText.innerHTML = "Near Me";
  controlUI.appendChild(controlText);

  // Setup the click event listeners: simply set the map to Chicago.
  controlUI.addEventListener("click", function () {
    navigator.geolocation.getCurrentPosition(function (position) {
      currentPosition = new google.maps.LatLng(
        position.coords.latitude,
        position.coords.longitude
      );
      map.setCenter(currentPosition);
    });
  });
}

/* @license-end */
