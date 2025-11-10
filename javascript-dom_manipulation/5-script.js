#!/usr/bin/node

const header = document.querySelector('header');
const element = document.getElementById('update_header');
element.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
