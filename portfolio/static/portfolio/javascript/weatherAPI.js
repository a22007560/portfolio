    const sunnyIconCode = [1, 3]
    const rainIconCode = [6, 7, 9, 10, 12, 13, 15]
    const heavyRainIconCode = [8, 11]
    const cloudIconCode = [4, 5, 25, 24, 27]
    const partlyCloudy = [2]

    window.onload = function() {
        getWeatherFun()
    };

    function getWeatherFun(){
        var cityCode = document.getElementById("city").value;

        fetch('//api.ipma.pt/open-data/forecast/meteorology/cities/daily/' + cityCode + '.json')
            .then(response => response.json())
            .then(data => {
                for (let i = 0; i < 5; i++){
                    var maxTemp = document.querySelector('.maxTemp' + i);
                    var minTemp = document.querySelector('.minTemp' + i);
                    var dataTemp = document.querySelector('.data' + i);
                    var chuvaProbValue = document.querySelector('.chuvaProb' + i);

                    maxTemp.innerHTML = "Temperatura Máxima: " + data['data'][i]['tMax'] + " ºC";
                    minTemp.innerHTML = "Temperatura Mínima: " + data['data'][i]['tMin'] + " ºC";
                    dataTemp.innerHTML = data['data'][i]['forecastDate'];
                    chuvaProbValue.innerHTML = "Probabilidade de Chuva: " + data['data'][i]['precipitaProb'] + " %";

                    var weatherTypeId = data['data'][i]['idWeatherType'];
                    var weatherIconName = "question.png";

                    if (sunnyIconCode.includes(weatherTypeId)){
                        weatherIconName = "sun.png"
                    } else if (partlyCloudy.includes(weatherTypeId)){
                        weatherIconName = "partly_cloudy.png"
                    } else if (rainIconCode.includes(weatherTypeId)){
                        weatherIconName = "rain.png"
                    } else if (heavyRainIconCode.includes(weatherTypeId)){
                        weatherIconName = "rainV2.png"
                    } else if (cloudIconCode.includes(weatherTypeId)){
                        weatherIconName = "cloud.png"
                    }

                    document.getElementById("weatherIcon" + i).src = "/portfolio/static/portfolio/images/weatherIcons/" + weatherIconName;
                }
        })
    }