pub fn isPalindromeNum(comptime T: type, x: T) bool {
    if (x < 10) return x >= 0;

    var n: T = x;
    var result: T = 0;

    while (n != 0) : (n = @divTrunc(n, 10))
        result = result * 10 + @rem(n, 10);

    return x == result;
}
