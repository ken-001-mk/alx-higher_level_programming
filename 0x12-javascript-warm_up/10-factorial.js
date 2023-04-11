#!/usr/bin/node

function factorial (sum) {
  if (isNaN(sum)) {
    return 1;
  } else if (sum === 0) {
    return 1;
  } else {
    return sum * factorial(sum - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
