pub fn pivot_integer(n: i32) -> i32 {
    let sum = n * (n + 1) / 2;
    for i in 0..n + 1 {
        let s = i * (i + 1) / 2;
        if sum - s + i == s { return i }
    }
    -1
}