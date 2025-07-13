pub fn isPowerOfTwo(comptime T: anytype, x: T) bool {
    // if (@mod(x, 2) != 0) return false;

    // var n: T = x;
    // while (n > 1) : (n = @divTrunc(n, 2))
    //     if (@mod(n, 2) != 0) return false;

    // return true;
    return (x & (x - 1)) == 0;
}
