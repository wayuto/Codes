pub fn is_power_of_four(mut n: i32) -> bool {
    if n <= 0 { return false }
    let mut p = 0;
    while n > 1 {
        if n % 2 != 0 || n < 0 { return false }
        n /= 2;
        p += 1;
    }
    if p % 2 == 0 { return true }
    false
}