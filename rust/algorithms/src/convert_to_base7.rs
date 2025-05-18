pub fn convert_to_base7(mut num: i32) -> String {
    let mut n: String = String::new();
    while num != 1 {
        n.insert_str(0, (num % 7).to_string().as_str());
        num /= 7;
    }
    format!("{}", num)
}