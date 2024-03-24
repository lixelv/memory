# https://www.codewars.com/kata/58e61f3d8ff24f774400002c
import re

def read(arg, registers):
    if arg[0] == "'" and arg[-1] == "'":
        return arg.replace("'", '')
    else: 
        for key in registers:
            if key in arg:
                arg = arg.replace(key, str(registers[key]))
        return eval(arg)

def assembler_interpreter(program):
    
    program = [i.split(";")[0].strip() for i in program.split('\n') if i.split(";")[0].strip()]
    registers = {
        "__loops__": {program[i].replace(':', ''): i for i in range(len(program)) if (program[i][-1] if program[i] else '') == ':'},
        "__cmp__": None,
        "__return_cursor__": [],
        "__output__": ""
                 }
    cursor = 0
    
    while cursor < len(program):
        line = program[cursor]
        
        if line[-1] == ':': 
            cursor += 1
            continue
        
        parsed_line = re.findall("('[^']*'|\w+)", line)
        cmd = parsed_line[0]
        args = parsed_line[1:] if len(parsed_line) > 1 else []
        
        if cmd == "mov": 
            registers[args[0]] = read(args[1], registers)
            
        elif cmd == "dec": 
            registers[args[0]] -= 1
            
        elif cmd == "inc": 
            registers[args[0]] += 1
            
        elif cmd == "add":
            registers[args[0]] += read(args[1], registers)
            
        elif cmd == "sub":
            registers[args[0]] -= read(args[1], registers)
            
        elif cmd == "mul":
            registers[args[0]] *= read(args[1], registers)
            
        elif cmd == "div":
            registers[args[0]] //= read(args[1], registers)
            
        elif cmd == "cmp":
            registers["__cmp__"] = (read(args[0], registers), read(args[1], registers))
                    
        elif cmd == "jmp":
            cursor = registers["__loops__"][args[0]] - 1
            
        elif cmd == "je":
            if registers["__cmp__"][0] == registers["__cmp__"][1]:
                cursor = registers["__loops__"][args[0]] - 1
        
        elif cmd == "jne":
            if registers["__cmp__"][0] != registers["__cmp__"][1]:
                cursor = registers["__loops__"][args[0]] - 1
        
        elif cmd == "jge":
            if registers["__cmp__"][0] >= registers["__cmp__"][1]:
                cursor = registers["__loops__"][args[0]] - 1
        
        elif cmd == "jg":
            if registers["__cmp__"][0] > registers["__cmp__"][1]:
                cursor = registers["__loops__"][args[0]] - 1
                
        elif cmd == "jle":
            if registers["__cmp__"][0] <= registers["__cmp__"][1]:
                cursor = registers["__loops__"][args[0]] - 1
                
        elif cmd == "jl":
            if registers["__cmp__"][0] < registers["__cmp__"][1]:
                cursor = registers["__loops__"][args[0]] - 1
                
        elif cmd == "call":
            registers["__return_cursor__"].append(cursor)
            cursor = registers["__loops__"][args[0]] - 1
        
        elif cmd == "ret":
            cursor = registers["__return_cursor__"][-1]
            del registers["__return_cursor__"][-1]
            
        elif cmd == "msg":
            registers["__output__"] += "".join([str(read(args[i], registers)) for i in range(len(args))])
            
        elif cmd == "end":
            return registers["__output__"]
        
        cursor += 1
        
    return -1

if __name__ == "__main__":
    # with open('assembler.txt', encoding='utf-8') as f:
    #     program = f.read()
    program = '''mov a, 10
                mov b, 5
                mul b, a
                
                msg b
                end'''
        
    print(assembler_interpreter(program))