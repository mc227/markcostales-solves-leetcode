// function counter(n){
//     let count = 0
//     for(let i = 0; i < n; i++){
//         count += 1
//     }
//     return count
// }

// console.log(counter(5))


// function counter(n){
//     let count = 0
//     for(let i = 0; i < 5*n; i++){
//         count += 1
//     }
//     return count
// }

// console.log(counter(5))

// function counter(n){
//     let count = 0
//     for(let i = 0; i < n; i++){
//         count += 3
//     }
//     return count
// }

// console.log(counter(5))

/**
 * example of sum rule, adding up big-Os
 */

// function a(n){
//     let count = 0

//     for(let i = 0; i < n; i++){
//         count += 1
//     }

//     for(let i = 0; i < 5*n; i++){
//         count += 1
//     }

//     return count
// }

// console.log(a(5))

/**my attempt to create a nested loop to show O of n squared */

// function a(n){
//     let count = 0

//     for(let i = 0; i < n; i++){
//         for(let i = 0; i < 5*n; i++){
//             count += 1
//         }
//     }

//     return count
// }

// console.log(a(5))

// function a(n){
//     let count = 0

//     for(let i = 0; i < n*n; i++){
//         count += 1
//     }
    

//     return count
// }

// console.log(a(5))

/**
 1) O of n squared
 2) O of n cubed
 3) O of 1
 4) O of n
 5) O log of n
 6) O of inifinity
 */