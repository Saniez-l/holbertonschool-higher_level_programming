#!/usr/bin/node

const args = process.argv.slice(2);
const myVar = ('C is fun');

for (let i = 0; i < args[0]; i++) {
  console.log(myVar);
}
