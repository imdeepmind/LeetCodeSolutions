/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n === 0) return arr;

    return arr.reduce((acc, item) => {
        if (Array.isArray(item)) {
            acc.push(...flat(item, n-1))
        } else {
            acc.push(item)
        }

        return acc
    }, [])
};