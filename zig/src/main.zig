const std = @import("std");
const func = @import("leetcode/canJump.zig").canJump;

pub fn main() void {
    const x = &[_]i32{ 3, 2, 1, 0, 4 };
    const res = func(x);

    std.debug.print("{}", .{res});
}
