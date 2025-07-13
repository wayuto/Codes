pub fn canJump(nums: []const i32) bool {
    var step: i32 = 1;
    var i: usize = nums.len - 2;

    while (i != 0) : (i -= 1) {
        if (nums[i] < step) step += 1 else step = 1;
    }

    return step == 1;
}
