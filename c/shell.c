#include <unistd.h>
#include <sys/wait.h>

int real_waitid(idtype_t idtype, id_t id, siginfo_t *infop, int options, void*);

int main(void) {
    char cmd[255] = "";
    for (;;) {
        write(1, "# ", 2);
        int count = read(0, cmd, 255);
        cmd[count - 1] = 0;
        pid_t fork_res = fork();
        if (fork_res == 0) {
            execve(cmd, 0, 0);
            break;
        } else {
            siginfo_t info;
            real_waitid(P_ALL, 0, &info, WEXITED, 0);
        }
    }

    _exit(0);
}
