const fs = require('fs');
const nums = fs.readFileSync('input.txt').toString().trim().split('\n').map(x => +x).sort((a,b) => a-b);
const diff = nums.reduce((a, b) => a + b) - 100
let found = false
for (let n1 = 0; n1 < 8; n1++)  {
    for (let n2 = n1+1; n2 < 9; n2++) {
        if (diff === nums[n1] + nums[n2]) {
            nums.splice(n2, 1)
            nums.splice(n1, 1)
            found = true
            console.log(nums.join('\n'))
            break
        }
    }
    if (found) {
        break
    }
}