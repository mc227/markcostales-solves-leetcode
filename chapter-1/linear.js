/* Linear example from book */
/*
function exampleLinear(n){
    for(let i = 0; i < n; i++){
        console.log(i)
    }
}

exampleLinear(5)
*/


/** I asked Claude for other O of n time complexity examples because i had only associated 
 * them with so what i'm doing below is trying to come up from scratch what
 * claude came up with so there maybe a little staring into the blank page
 */

function sumArray(arr){
    return arr.reduce((sum, item)=> sum+item,0)
}

let numbers = [1,2,3,4,5]
console.log(sumArray(numbers))