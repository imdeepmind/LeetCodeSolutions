/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const mapper = {}

    this.forEach((item) => {
        const key = fn(item);

        if (mapper[key]) mapper[key].push(item)
        else mapper[key] = [item]
    })
    
    return mapper;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */