#!/usr/bin/node

const arg1 = process.argv[3];
if (arg1 === 0) {
  console.log('No argument');
} else if (arg1 === 2) {
  console.log('HBTN cool');
} else {
  console.log('HBTN');
}
