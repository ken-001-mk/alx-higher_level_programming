#!/usr/bin/node

const args = process.argv.length = 2;
if (args === 2) {
  console.log('No arguments');
} else if (args === 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
