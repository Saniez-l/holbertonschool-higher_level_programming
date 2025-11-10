document.addEventListener('DOMContentLoaded', () => {
  const helloElement = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloElement.textContent = data.hello;
    })
})