SYS_WRITE equ 4
STDOUT equ 1
SYS_READ equ 3
STDIN equ 0
SYS_EXIT equ 1

section .text
    global _start

_start:
    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,tips
    mov edx,tips_len
    int 0x80

    mov eax,SYS_READ
    mov ebx,STDIN
    mov ecx,n1
    mov edx,2
    int 0x80

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,tips1
    mov edx,tips1_len
    int 0x80

    mov eax,SYS_READ
    mov ebx,STDIN
    mov ecx,n2
    mov edx,2
    int 0x80

    mov eax,[n1]
    sub eax,'0'
        
    mov ebx,[n2]
    sub ebx,'0'

    add eax,ebx
    add eax,'0'

    mov [res], eax

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,tips2
    mov edx,tips2_len
    int 0x80

    mov eax,SYS_WRITE
    mov ebx,STDOUT
    mov ecx,res
    mov edx,1
    int 0x80
    jmp exit

section .bss
    n1 resb 2
    n2 resb 2
    res resb 1

section .data
    tips db "Please enter the first number: "
    tips_len equ $ - tips

    tips1 db "Please enter the second number: "
    tips1_len equ $ - tips1

    tips2 db "The sum is: "
    tips2_len equ $ - tips2

exit:
    mov eax,SYS_EXIT
    int 0x80