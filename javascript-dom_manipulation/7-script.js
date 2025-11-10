fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const list = document.querySelector('#list_movies');
    data.results.forEach(film => {
      const newItem = document.createElement('li');
      newItem.textContent = film.title;
      list.appendChild(newItem);
    });
  });
