#!/usr/bin/node

const header = document.querySelector('header');
const redHeader = document.querySelector('#toggle_header');

redHeader.addEventListener('click', () => {
if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add("green");
  }
else {
    header.classList.remove('green');
    header.classList.add("red");
}
});
