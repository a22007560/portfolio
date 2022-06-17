    function getNews(){
        fetch('https://gnews.io/api/v4/top-headlines?token=f5244e8b9006523a706b443bbbdbe0be&lang=en')
            .then(response => response.json())
            .then(data => {
                console.log(data);

                for (let i = 0; i < 10; i++) {
                    var newsTitle = document.createElement("h3");
                    var newsImg = document.createElement("img");
                    var newsDesc = document.createElement("p");
                    var newsUrl = document.createElement("a");
                    var newsDate = document.createElement("p");
                    var newsSource = document.createElement("p");
                    var newsBox = document.getElementById("newsBox" + i);

                    newsBox.append(newsTitle)
                    newsBox.append(newsImg)
                    newsBox.append(newsDesc)
                    newsBox.append(newsUrl)
                    newsBox.append(newsDate)
                    newsBox.append(newsSource)

                    newsTitle.innerHTML = data['articles'][i]['title'];
                    newsImg.src = data['articles'][i]['image'];
                    newsDesc.innerHTML = data['articles'][i]['description'];
                    newsUrl.innerHTML = "Ler notícia..."
                    newsUrl.target = "blank_"
                    newsUrl.href = data['articles'][i]['url'];
                    newsDate.innerHTML = "Publicado a: " + data['articles'][i]['publishedAt'];
                    newsSource.innerHTML = "Fonte: " + data['articles'][i]['source']['name'];
                }


        }).catch(error => {
        console.error('Erro nas Noticias!', error);
    });
    }
