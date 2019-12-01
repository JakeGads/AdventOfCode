"use strict";
exports.__esModule = true;
function handler(number) {
    number = number / 3;
    number = Math.floor(number);
    number -= 2;
    return number;
}
function calc_difference(weight) {
    var current_weight = handler(weight);
    weight = current_weight;
    while (true) {
        if (handler(current_weight) > 0) {
            current_weight = handler(current_weight);
            weight += current_weight;
        }
        else {
            return weight;
        }
    }
}
var fs = require("fs");
var readline = require("readline");
var vals = [];
var readInterface = readline.createInterface({
    input: fs.createReadStream('day1.txt'),
    output: process.stdout
});
readInterface.on('line', function (line) {
    vals.push(parseFloat(line.toString()));
});
var sum = 0;
vals.forEach(function (element) {
    sum += calc_difference(element);
});
console.log(sum);
