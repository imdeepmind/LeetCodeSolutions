/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if (arr.length <= 0) return arr
    
    const chunks = []
    let i = 0,
        j = size;
    
    while (true) {
        if (i+1 > arr.length) break

        chunks.push(arr.slice(i, j))
        i = j
        j += size
    }

    return chunks
};
