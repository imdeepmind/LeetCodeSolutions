function* fibGenerator(): Generator<number, any, number> {
    let a = 0,
        b = 1;
    while (true){
        yield a;

        const temp = a;
        a=b;
        b=temp+b;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */