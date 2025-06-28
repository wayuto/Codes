pub fn is_happy(mut n: i32) -> bool {
    let unhappy = [4, 16, 37, 58, 89, 145, 42, 20];

    loop {
        let mut sum = 0;
        while n != 0 {
            let digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }

        if sum == 1 { return true }
        if unhappy.contains(&sum) { return false }

        n = sum;
    }
}