#!/usr/bin/node

function secBiggestInt (args) {
  if (args.length < 3) {
    return 0;
  } else {
    const intList = args.map(arg => parseInt(arg));
    const sortedList = intList.sort((i, j) => j - i);
    return sortedList[2];
  }
}

console.log(secBiggestInt(process.argv.slice(3)));
