/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const hash = {}

    return function(...args) {
        if (hash[JSON.stringify(args)] === undefined) 
            hash[JSON.stringify(args)] = fn(...args)
        
        return hash[JSON.stringify(args)]
    }
}


 
//  let callCount = 0;
//  const memoizedFn = memoize(function (a, b) {
//  	 callCount += 1;
//     return a + b;
//  })
//  memoizedFn(2, 3) // 5
//  memoizedFn(2, 3) // 5
//  console.log(callCount) // 1 
 