section .text
    global _start

atoi:
    xor rax, rax        
    xor rbx, rbx        

.convert_loop:
    lodsb               
    test al, al         
    jz .done
    cmp al, 0xa         
    je .done
    sub al, '0'         
    imul rbx, 10        
    add rbx, rax        
    jmp .convert_loop   
    
.done:
    mov rax, rbx        
    ret

itoa:
    mov rbx, 10         
    mov rcx, 0          
    
    lea r8, [rdi + 19]  
    mov byte [r8], 0    

.convert_loop:
    xor rdx, rdx        
    div rbx             
    add dl, '0'         
    dec r8              
    mov [r8], dl        
    inc rcx             
    test rax, rax       
    jnz .convert_loop   
    
    mov rax, rcx        
    mov rdi, r8         
    ret

%macro print 2
    mov rax, 1
    mov rdi, 1
    mov rsi, %1
    mov rdx, %2
    syscall
%endmacro

%macro exit 1
    mov rax, 60
    mov rdi, %1
    syscall
%endmacro

_start:
    print prompt, prompt_len
    
    mov rax, 0
    mov rdi, 0
    mov rsi, inbuf
    mov rdx, 20
    syscall

    mov rsi, inbuf
    call atoi           
    add rax, 1          
    
    mov rdi, outbuf     
    call itoa           
    
    mov r12, rdi        
    mov r13, rax        
    
    print result, result_len
    
    mov rsi, r12        
    mov rdx, r13        
    mov rax, 1
    mov rdi, 1
    syscall             
    
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall
    
    mov rax, 60
    xor rdi, rdi
    syscall

section .bss
    inbuf  resb 20
    outbuf resb 20

section .data
    prompt db "Enter a number: "
    prompt_len equ $ - prompt

    result db "Result: "
    result_len equ $ - result

    newline db 0xa