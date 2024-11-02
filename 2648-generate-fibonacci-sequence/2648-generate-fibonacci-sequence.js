/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let current = 0, 
        next = 1

    while (true) {
        yield current

        tempCurrent = current
        current = next
        next = tempCurrent+next
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */