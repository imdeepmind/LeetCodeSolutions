var TimeLimitedCache = function() {
    this.cache = {}
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const creationTime = +new Date()

    if (this.cache.hasOwnProperty(key)) {
        this.cache[key] = {
            value, duration, creationTime
        }

        if (this.get(key) === -1) {
            return false
        }
        

        return true
    }

    this.cache[key] = {
        value, duration, creationTime
    }

    return false
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const currentTime = +new Date()

    const item = this.cache[key]

    console.log(item, currentTime)

    if (item && item.creationTime + item.duration >= currentTime) return item.value

    return -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let total = 0

    Object.keys(this.cache).forEach(key => {
        if (this.get(key) !== -1) total ++
    })

    return total
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */