/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let counter = init
    
    return {
        increment: () => ++counter,
        reset: () => counter = init,
        decrement: () => --counter
    }
};

// const counter = createCounter(5)
// console.log(counter.increment()); // 6
// counter.reset(); // 5
// counter.decrement(); // 4
