#!/usr/bin/node

const args = process.argv.slice(2);
const numb = parseInt(args[0]);
const numb1 = parseInt(args[1]);

if (isNaN(numb) || isNaN(numb1)) {
  console.log('NaN');
} else {
  console.log(numb + numb1);
}
