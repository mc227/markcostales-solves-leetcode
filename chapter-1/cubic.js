function exampleCubic(n){
    for(let i = 0; i < n; i++){
        console.log(`\n╔═══ OUTER i = ${i} ═══╗`)
        for(let j = i; j < n; j++){
            console.log(`║  ┌─ MIDDLE j = ${j}`)
            for (let k = j; k < n; k++){
                console.log(`║  │  └→ INNER k = ${k}`)
            }
        }
        console.log(`╚═══ END i = ${i} ═══╝`)
    }
}
exampleCubic(4)