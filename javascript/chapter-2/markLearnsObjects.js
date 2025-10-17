/**
 * using remarkable i wrote up from scratch the code i learned from 
 * scratch
 */

// what was the first concept?
// object equality will always yield false
// because of the memory location
console.log("=======================")
let obj1 = {}
let obj2 = {}

console.log(obj1 == obj2) // false
console.log(obj1 === obj2) // false

// i think in practice people use lodash or something
// i've heard a senior engineer mention this before
console.log("=======================")
function isEquivalent(a,b){
    // get list of properties
    let aProps = Object.getOwnPropertyNames(a)
    let bProps = Object.getOwnPropertyNames(b)

    // check length of the property lists
    if (aProps.length !== bProps.length){
        return false
    }

    // if lengths are the same, assuming property names are the same then property values 
    // should be compared
    for (let  i = 0; i < aProps.length; i++){
        let propName = aProps[i];
        if (a[propName] !== b[propName]){
            return false
        }
    }

    return true
}

console.log(isEquivalent({'hi':12},{'hi':12}))

console.log("=======================")

// let obj3 = {'prop1':'test', 'prop2': function() {console.log(2)}}
// let obj4 = {'prop1':'test', 'prop2': function() {console.log(2)}}
let obj3 = {'prop1':'test'}
let obj4 = {'prop1':'test'}

console.log(isEquivalent(obj3, obj4))

console.log("=======================")

let func1 = function(){console.log(2)}
let func2 = function(){console.log(2)}

console.log(func1 === func2)