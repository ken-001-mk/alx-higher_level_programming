#!/usr/bin/node

const args = process.argv.length = 3;
if (args === 3) {
  console.log('No argument');
} else if (args === 4) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
