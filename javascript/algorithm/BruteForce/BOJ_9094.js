const fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');
let tc = input[0]
for (let i = 1; i <= tc; i++) {
    const [n, m] = input[i].split(' ').map((x) => +x);
    let ans = 0;
    for (let a = 1; a < n - 1; a++) {
        for (let b = a + 1; b < n; b++) {
            if (!((a ** 2 + b ** 2 + m) % (a * b))) {
                ans++
            }
        }
    }
    console.log(ans)
}