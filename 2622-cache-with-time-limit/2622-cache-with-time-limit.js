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
    if (this.cache.hasOwnProperty(key)) {
        this.cache[key] = {
            value,
            ttl: +new Date() + duration
        }

        if (this.get(key) === -1) {
            return false
        }

        return true
    }

    this.cache[key] = {
        value,
        ttl: +new Date() + duration
    }

    return false;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.cache[key] && this.cache[key]['ttl'] > +new Date()) {
        return this.cache[key]['value']
    }

    return -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let count = 0

    Object.keys(this.cache).forEach(key => {
        if (this.get(key) !== -1) count += 1;
    })

    return count
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */