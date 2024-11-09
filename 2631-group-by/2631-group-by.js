/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const hash = {}

    for (const item of this) {
        const value = fn(item)

        if (hash.hasOwnProperty(value)) {
            hash[value].push(item)
        } else {
            hash[value] = [item]
        }
    }

    return hash
    
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */