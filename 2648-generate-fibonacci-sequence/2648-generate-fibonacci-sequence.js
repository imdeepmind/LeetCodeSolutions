/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let prev = 0, current = 1;

    while (true) {
        yield prev

        temp = prev + current
        prev = current
        current = temp
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */