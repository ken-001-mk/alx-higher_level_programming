#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < x; a++) {
    console.log('C is fun');
  }
}
