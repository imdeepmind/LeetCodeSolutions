/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const arr = Array.from(functions.length).fill(0);
        let count = 0;

        functions.forEach(async (func, index) => {
            try {
                arr[index] = await func();
                count++;
                
                if (count === functions.length) resolve(arr);
            } catch (error) {
                reject(error)
            }
        })

    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */