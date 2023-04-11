#!/usr/bin/node

const nums = parseInt(process.argv[4]);
if (isNaN(nums)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + nums);
}
