pub fn climb_stairs(n: i32) -> i32 {
    (0..n).fold([1,1],|way,_|[way[1],way[0]+way[1]])[0]
}