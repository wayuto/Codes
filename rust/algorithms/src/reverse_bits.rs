pub fn reverse_bits(mut x: u32) -> u32 {
    let mut res: u32 = 0;

    for _ in 0..32 {
        res = (res << 1) | (x & 1);
        x >>= 1;
    }

    res
}