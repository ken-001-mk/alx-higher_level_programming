#!/usr/bin/node

const nums = parseInt(process.argv[4]);
if (isNaN(nums)) {
  console.log('No a number');
} else {
  console.log('My number: ' + nums);
}
