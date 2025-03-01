class EventEmitter {
    constructor() {
        this.events = {};
    }
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (this.events[eventName]) this.events[eventName].push(callback)
        else this.events[eventName] = [callback]

        return {
            unsubscribe: () => {
                if (this.events[eventName]) {
                    this.events[eventName].forEach((event, index) => {
                        if (event === callback) {
                            this.events[eventName].splice(index, 1)
                            return
                        }
                    })
                }
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        if (this.events[eventName] === undefined) return [];

        const res = [];

        this.events[eventName].forEach((func) => {
            res.push(func(...args));
        })

        return res;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */