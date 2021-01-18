for (let a = 6; a <= 100; a++) {
    for (let b = 2; b < a; b++) {
        for (let c = b; c < a; c++) {
            for (let d = c; d < a; d++){
                if (a*a*a === b*b*b + c*c*c + d*d*d) {
                    console.log(`Cube = ${a}, Triple = (${b},${c},${d})`)
                }
            }
        }
    }
}