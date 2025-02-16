/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let i = init;

    return {
        increment: () => ++i,
        decrement: () => --i,
        reset: () => {
            i=init; 
            return i
        }
    }
};

// const counter = createCounter(5)
// console.log(counter.increment()); // 6
// counter.reset(); // 5
// counter.decrement(); // 4
