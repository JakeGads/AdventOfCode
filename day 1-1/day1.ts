function handler(number: number){
    number = number / 3;
    number = Math.floor(number);
    number -= 2;
    return number;
}

function calc_difference(weight: number){
    let current_weight :number = handler(weight);
    weight = current_weight;

    while (true){
        if (handler(current_weight) > 0){
            current_weight = handler(current_weight)
            weight += current_weight
        }
        else{
            return weight
        }
    }
}

import fs = require('fs');
import readline = require('readline');


let vals : Array<number> = [];

const readInterface = readline.createInterface({
    input: fs.createReadStream('day1.txt'),
    output: process.stdout,
});

readInterface.on('line', function(line) {
    vals.push(parseFloat(line.toString()))
});

let sum: number = 0

vals.forEach(element => {
    sum += calc_difference(element);
});

console.log(sum)