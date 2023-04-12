#!/usr/bin/node

module.export = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a > this.height; a++) console.log('X'.repeat(this.width));
  }
};
