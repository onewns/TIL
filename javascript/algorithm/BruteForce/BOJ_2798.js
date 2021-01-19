const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split('\n');
const [n, m] = input[0].split(' ').map(x => +x);
const nums = input[1].split(' ').map(x => +x);
let ans = 0;
let found = false
for (let i1 = 0; i1 < n-2; i1++) {
    for (let i2 = i1+1; i2 < n-1; i2++) {
        for (let i3 = i2+1; i3 < n; i3++) {
            let temp = nums[i1] + nums[i2] + nums[i3]
            if (temp <= m & ans < temp) {
                ans = temp}
            if (temp === m) {
                found = true
                break}
        }
        if (found) {
            break
        }
    }
    if (found) {
        break
    }
}
console.log(ans)