function exampleQuadratic(n){
    for (let i = 0; i < n; i++){
        console.log(`\n--- Outer loop i = ${i}---`)
        for (let j = i; j < n; j++){
            console.log(`   Inner loop j = ${j}`)
        }
    }
}

exampleQuadratic(4)