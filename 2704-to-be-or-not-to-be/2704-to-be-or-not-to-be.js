/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: compare => {
            if (compare === val) return true
            else throw new Error("Not Equal")
        },
        notToBe: compare => {
            if (compare !== val) return true
            else throw new Error("Equal")
        }
    }
};
