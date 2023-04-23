#!/usr/bin/node

function secBiggestInt (args) {
  if (process.args.length <= 3) {
    return 0;
  } else {
    const intList = process.args.map(Number)
	.slice(2, process.args.length)
	.sort((i, j) => j - i);
    return sortedList[2];
  }
}

console.log(secBiggestInt(process.argv.slice(3)));
