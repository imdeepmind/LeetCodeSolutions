/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const res = [];
    let batch = []

    arr.forEach(item => {
        if (size > batch.length) {
            batch.push(item)
        } else {
            res.push(batch)
            batch = [item]
        }
    })

    if (batch.length > 0) {
        res.push(batch);
    }

    return res
};
