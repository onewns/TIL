let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split(' ').map((x) => +x);
const [m, seed, x1, x2] = input
let find = false
for (let a = 0; a < m; a++) {
    for (let c = 0; c < m; c++) {
        let t1 = (a * seed + c) % m
        let t2 = (a * t1 + c) % m
        if (x1 === t1 & x2 === t2) {
            console.log(a, c);
            find = true
            break
        };
    };
    if (find) {
        break
    }
}