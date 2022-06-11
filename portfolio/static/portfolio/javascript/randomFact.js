



    function getAnimal(){
        var animalName = document.querySelector('.animalName')
        var animalLatinName = document.querySelector('.animalLatinName')
        var animalActiveTime = document.querySelector('.animalActiveTime')
        var animalType = document.querySelector('.animalType')
        var animalDiet = document.querySelector('.animalDiet')
        var animalHabitat = document.querySelector('.animalHabitat')

        fetch('https://zoo-animal-api.herokuapp.com/animals/rand')
            .then(response => response.json())
            .then(data => {

                animalName.innerHTML = data['name'];
                document.querySelector(".animalImg").src = data['image_link'];
                animalLatinName.innerHTML = "Nome Latim: " + data['latin_name'];
                animalActiveTime.innerHTML = "Tempo de Actividade: " + data['active_time'];
                animalType.innerHTML = "Tipo de Animal: " + data['animal_type'];
                animalDiet.innerHTML = "Dieta: " + data['diet'];
                animalHabitat.innerHTML = "Habitat: " + data['habitat'];


        }).catch(error => {
        console.error('Erro nos animais!', error);
    });
    }




