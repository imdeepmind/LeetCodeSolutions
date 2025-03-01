/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (obj == null) return null
    if (Array.isArray(obj)) {
        return obj.filter(x => !!x).map(x => compactObject(x));
    }
    
    if (typeof obj === "object") {
        const response = {}
        for (const key in obj) {
            const item = compactObject(obj[key]);

            if (!!item) response[key] = item;
        }

        return response;
    }

    return obj;
};