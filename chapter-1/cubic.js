function exampleCubic(n){
    for (let i = 0; i < n; i++){
        console.log(`\n╔═══ OUTER i = ${i} ═══╗`)
        for (let j = i; j < n; j++){
            console.log(`║  ┌─ MIDDLE j = ${j}`)
            for (let k = j; k < n; k++){
                console.log(`║  │  └→ INNER k = ${k}`)
            }
        }
        console.log(`╚═══ END i = ${i} ═══╝`)
    }
}

exampleCubic(4)


/**
╔═══ OUTER i = 0 ═══╗
║  ┌─ MIDDLE j = 0
║  │  └→ INNER k = 0
║  │  └→ INNER k = 1
║  │  └→ INNER k = 2
║  │  └→ INNER k = 3
║  ┌─ MIDDLE j = 1
║  │  └→ INNER k = 1
║  │  └→ INNER k = 2
║  │  └→ INNER k = 3
║  ┌─ MIDDLE j = 2
║  │  └→ INNER k = 2
║  │  └→ INNER k = 3
║  ┌─ MIDDLE j = 3
║  │  └→ INNER k = 3
╚═══ END i = 0 ═══╝
 */