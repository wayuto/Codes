pub fn is_power_of_three(mut n: i32) -> bool {
    if n == 1 { return true }
    if n % 2 == 0 { return false }
    loop {
        if n % 3 != 0 && n != 1 { return false }
        if n == 1 { break }
        n /= 3;
    }
    true
}