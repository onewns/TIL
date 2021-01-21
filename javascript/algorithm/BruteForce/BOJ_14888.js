const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split('\n')
const n = parseInt(input[0])
const nums = input[1].split(' ').map(x => +x)
let operator = input[2].split(' ').map(x => +x)
let [max, min] = [-Infinity, Infinity]
function cal(n1, n2, op) {
    if (op === 0) {
        return n1 + n2
    } else if (op === 1) {
        return n1 - n2
    } else if (op === 2) {
        return n1 * n2
    } else {
        return parseInt(n1 / n2)
    }
}
function dfs(now, temp) {
    if (now === n) {
        max = Math.max(max, temp)
        min = Math.min(min, temp)
    } else {
        for (let op = 0; op < 4; op++) {
            if (operator[op] > 0) {
                operator[op]--
                dfs(now+1, cal(temp, nums[now], op))
                operator[op]++
            }
        }
    }
}
dfs(1, nums[0])
console.log(max ? max : 0);
console.log(min ? min : 0);