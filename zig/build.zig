const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{
        .default_target = .{
            .cpu_arch = .x86,
            .cpu_model = .{ .explicit = &std.Target.x86.cpu.athlon_4 },
            .os_tag = .freestanding,
        },
    });

    const optimize = b.standardOptimizeOption(.{});

    const lib_mod = b.createModule(.{
        .root_source_file = b.path("lib/math.zig"),
        .target = target,
        .optimize = optimize,
    });

    const kernel_mod = b.createModule(.{
        .root_source_file = b.path("src/kernel/main.zig"),
        .target = target,
        .optimize = optimize,
    });

    kernel_mod.addImport("math", lib_mod);

    // 编译内核
    const kernel = b.addExecutable(.{
        .name = "kernel",
        .root_module = kernel_mod,
    });
    kernel.setLinkerScript(b.path("src/kernel/linker.ld"));

    // 编译MBR
    const mbr = b.addAssemblyFile(.{
        .file = b.path("src/boot/mbr.s"),
        .target = target,
        .optimize = optimize,
    });

    // 编译loader
    const loader = b.addAssemblyFile(.{
        .file = b.path("src/boot/loader.s"),
        .target = target,
        .optimize = optimize,
    });

    // 创建磁盘镜像
    const create_disk = b.addSystemCommand(&.{ "dd", "if=/dev/zero", "of=disk.img", "bs=1M", "count=10" });

    // 格式化磁盘镜像为FAT12
    const format_disk = b.addSystemCommand(&.{ "mkfs.fat", "-F", "12", "disk.img" });
    format_disk.step.dependOn(&create_disk.step);

    // 安装MBR到磁盘镜像
    const install_mbr = b.addSystemCommand(&.{ "dd", "if=mbr.bin", "of=disk.img", "bs=512", "count=1", "conv=notrunc" });
    install_mbr.step.dependOn(&mbr.step);

    // 安装loader到磁盘镜像
    const install_loader = b.addSystemCommand(&.{ "dd", "if=loader.bin", "of=disk.img", "bs=512", "seek=2", "conv=notrunc" });
    install_loader.step.dependOn(&loader.step);

    // 安装内核到磁盘镜像
    const install_kernel = b.addSystemCommand(&.{ "dd", "if=kernel.bin", "of=disk.img", "bs=512", "seek=10", "conv=notrunc" });
    install_kernel.step.dependOn(&kernel.step);

    // 创建bochs配置文件
    const bochs_config = b.addWriteFiles();
    const bochs_config_file = bochs_config.add("bochsrc.txt",
        \\# Bochs配置文件
        \\romimage: file=/usr/share/bochs/BIOS-bochs-latest
        \\vgaromimage: file=/usr/share/bochs/VGABIOS-lgpl-latest
        \\megs: 32
        \\ata0-master: type=disk, path=disk.img, mode=flat, cylinders=20, heads=16, spt=63
        \\boot: disk
        \\log: bochs.log
        \\panic: action=ask
        \\error: action=report
        \\info: action=report
        \\debug: action=ignore
    );

    // 创建bochs运行命令
    const run_bochs = b.addSystemCommand(&.{ "bochs", "-f", bochs_config_file.path });
    run_bochs.step.dependOn(&install_kernel.step);
    run_bochs.step.dependOn(&install_loader.step);
    run_bochs.step.dependOn(&install_mbr.step);
    run_bochs.step.dependOn(&bochs_config.step);

    // 安装步骤
    b.installArtifact(kernel);
    b.installArtifact(mbr);
    b.installArtifact(loader);

    // 运行步骤
    const run_step = b.step("run", "Run the OS in Bochs");
    run_step.dependOn(&run_bochs.step);

    // 测试步骤
    const test_step = b.step("test", "Run tests");
    const kernel_tests = b.addTest(.{
        .root_module = kernel_mod,
    });
    const run_kernel_tests = b.addRunArtifact(kernel_tests);
    test_step.dependOn(&run_kernel_tests.step);
}
