#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('Not a number');
} else {
  const number = parseInt(args[0], 10);
  if (isNaN(number)) {
    console.log('Not a number');
  } else {
    console.log('My number:', number);
  }
}
