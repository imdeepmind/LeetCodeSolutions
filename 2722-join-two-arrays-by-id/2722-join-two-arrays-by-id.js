/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const joinedArray = [];
    const merged = {};

    arr1.forEach((item) => {
        if (merged[item.id]) merged[item.id] = {...merged[item.id], ...item}
        else merged[item.id] = item
    })

    arr2.forEach((item) => {
        if (merged[item.id]) merged[item.id] = {...merged[item.id], ...item}
        else merged[item.id] = item
    })
    
    for (const key in merged) {
        joinedArray.push(merged[key])
    }

    return joinedArray;
};