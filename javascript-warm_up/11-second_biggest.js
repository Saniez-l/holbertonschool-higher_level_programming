#!/usr/bin/node

const argv = process.argv.slice(2).map(Number);

if (argv.length < 2) {
  console.log(0);
} else {
  argv.sort((a, b) => b - a);
  console.log(argv[1]);
}
