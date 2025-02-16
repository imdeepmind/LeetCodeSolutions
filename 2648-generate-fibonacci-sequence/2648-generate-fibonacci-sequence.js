/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let prev = 0,
        current = 1;

    while (true) {
        yield prev
        temp = prev
        prev = current
        current = temp + current
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */