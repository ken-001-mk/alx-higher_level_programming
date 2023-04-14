#!/usr/bin/node

const arg1 = process.argv[3];
if (arg1 === 0) {
  console.log('Python is fun');
} else if (arg1 === 2) {
  console.log('HBTN is undefined');
} else {
  console.log('undefined is undefined');
}
