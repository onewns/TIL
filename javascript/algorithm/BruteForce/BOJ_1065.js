let fs = require('fs');
let input = fs.readFileSync('input.txt').toString();
let ans = 0;
for (let index = 1; index <= input; index++) {
    if (index <= 99) {
        ans++
    } else {
        let n = index.toString();
        const diff = n[0] - n[1]
        let find = true
        for (let i = 2; i < n.length; i++) {
            if (n[i-1] - n[i] !== diff) {
                find = false
                break
            }
        }
        if (find) {
            ans++
        }
    }
};
console.log(ans)