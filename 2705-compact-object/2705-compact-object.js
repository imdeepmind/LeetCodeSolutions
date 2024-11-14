/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (obj === null) return null
    if (Array.isArray(obj)) return obj.filter(x => Boolean(x)).map(x => compactObject(x))
    if (typeof obj !== "object") return obj

    const response = {}

    for (const key of Object.keys(obj)) {
        const value = compactObject(obj[key])

        if (Boolean(value)) response[key] = value
    }

    return response
};