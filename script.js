async function createMap() {
    // Centering map around Hong Kong
    var center = { lat: 22.3193, lng: 114.1694 };

    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: center
    });

    let currentInfoWindow = null;
    let currentMarker = null;


    try {

        let response = await fetch("http://localhost:5000/ev_stations_data");
        let stations = await response.json();

        console.log(stations.length)

        

        for (let i = 0; i < stations.length; i++) {
            let station = stations[i];

            var lat = parseFloat(station["latitude"])
            var long = parseFloat(station["longitude"])

            if (isNaN(lat) || isNaN(long)) {
                console.warn(`Skipping station due to invalid coordinates: ${station["name"]}`);
                continue;  // Skip this station if coordinates are invalid
            }


            
    
            let marker = new google.maps.Marker({
                position: {lat: lat, lng: long},
                map: map,
                title: station["name"]
            });

            console.log(marker.title);

            
                 
    
            marker.addListener("click", function () {
                if (currentInfoWindow && currentMarker == marker) {
                    currentInfoWindow.close();
                    currentInfoWindow = null;
                    currentMarker = null;
                    return;
                } else if (currentInfoWindow) {
                    currentInfoWindow.close();
                    currentInfoWindow = null;

                }

                let infoWindow = new google.maps.InfoWindow({
                    content: `<h3>Name: ${station["name"]}</h3>`
                });

                infoWindow.open(map, marker);


                currentInfoWindow = infoWindow;
                currentMarker = marker;
                
                
            });

            console.log(currentInfoWindow);
    
        }
    
    } catch (error) {
        console.error("Error fetching station data:", error);
    }
   


    
    
}