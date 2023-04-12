#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

const rect1 = new Rectangle(4, 5);
console.log(rect1);
console.log(rect1.width);
console.log(rect1.height);

const rect2 = new Rectangle(4, -6);
console.log(rect1);
console.log(rect2.width);
console.log(rect2.height);
