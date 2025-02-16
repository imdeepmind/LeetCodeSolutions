/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (num) => {
            if (num  !== val) {
                throw new Error("Not Equal")
            }

            return true;
        },
        notToBe: (num) => {
            if (num  === val) {
                throw new Error("Equal")
            }

            return true;
        }
    }
};
