/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (this.length !== rowsCount * colsCount) return []

    const resp = Array.from({ length: rowsCount }, () => Array(colsCount).fill(0));

    for (let column = 0; column < colsCount; column++) {
        for (let row = 0; row < rowsCount; row++) {
            const key = row + (column * rowsCount)
            const value = this[key]

            const rowKey = column % 2 === 0 ? row : rowsCount-row-1
            resp[rowKey][column] = value
        }
    }

    return resp
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */