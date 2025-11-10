#!/usr/bin/node

const list = document.querySelector('.my_list');
const redHeader = document.querySelector('#add_item');
redHeader.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'item';
  list.append(newItem);
});
