function generateRange(min, max, step){
    var gen = [];
    for (i = min; i < max+1; i+=step) {
      gen.push(i);
    }
    return gen;
  }