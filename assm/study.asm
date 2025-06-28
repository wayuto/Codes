section .text
    global _start

%macro printf 2
    mov eax,4
    mov ebx,1
    mov ecx,%1
    mov edx,%2
    int 0x80
%endmacro

_start:
    printf msg,len

    mov eax,1
    int 0x80

section .data
    msg db "Hello world!", 0xa
    len equ $ - msg