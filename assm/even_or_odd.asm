section .text
    global _start


_start:
    mov ax,8h
    and ax,1
    jz even
    mov eax,4
    mov ebx,1
    mov ecx,odd_msg
    mov edx,odd_len
    int 0x80
    jmp exit

even:
    mov ah,09h
    mov eax,4
    mov ebx,1
    mov ecx,even_msg
    mov edx,even_len
    int 0x80

exit:
    mov eax,1
    int 0x80

section .data
    even_msg db "Even", 0xa
    even_len equ $ - even_msg

    odd_msg db "Odd", 0xa
    odd_len equ $ - odd_msg