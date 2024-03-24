# https://www.codewars.com/kata/58e61f3d8ff24f774400002c
import re

class Assembler:
    def __init__(self, program):
        self.commands = {
            "mov": self.mov, "inc": self.inc, "dec": self.dec, "add": self.add, 
            "sub": self.sub, "mul": self.mul, "div": self.div, "cmp": self.cmp, 
            "jmp": self.jmp, "je": self.je, "jne": self.jne, "jge": self.jge, 
            "jg": self.jg, "jle": self.jle, "jl": self.jl, "call": self.call, 
            "ret": self.ret, "msg": self.msg, "end": self.end
        }
        self.program = [i.split(";")[0].strip() for i in program.split('\n') if i.split(";")[0].strip()]
        self.registers = {
            "__loops__": {self.program[i].replace(':', ''): i for i in range(len(self.program)) if (self.program[i][-1] if self.program[i] else '') == ':'},
            "__cmp__": None,
            "__return_cursor__": [],
            "__output__": "",
            "__cursor__": 0           
        }
        
    def run(self):
        while self.registers["__cursor__"] < len(program):
            line = self.program[self.registers["__cursor__"]]
            
            if line[-1] == ':': 
                self.registers["__cursor__"] += 1
                continue
            
            parsed_line = re.findall("('[^']*'|\w+)", line)
            cmd = parsed_line[0]
            args = parsed_line[1:] if len(parsed_line) > 1 else []
            
            if self.commands[cmd](args) is None:
                self.registers["__cursor__"] += 1
            else:
                return self.registers["__output__"]
        return -1
        
    def read(self, arg):
        if arg[0] == "'" and arg[-1] == "'":
            return arg.replace("'", '')
        else: 
            for key in self.registers:
                if key in arg:
                    arg = arg.replace(key, str(self.registers[key]))
            return eval(arg)

    def mov(self, args): self.registers[args[0]] = self.read(args[1])
    def dec(self, args): self.registers[args[0]] -= 1
    def inc(self, args): self.registers[args[0]] += 1
    def add(self, args): self.registers[args[0]] += self.read(args[1])
    def sub(self, args): self.registers[args[0]] -= self.read(args[1])
    def mul(self, args): self.registers[args[0]] *= self.read(args[1])
    def div(self, args): self.registers[args[0]] //= self.read(args[1])
    def mod(self, args): self.registers[args[0]] %= self.read(args[1])
    
    def cmp(self, args): self.registers["__cmp__"] = (self.read(args[0]), self.read(args[1]))
    def jmp(self, args): self.registers["__cursor__"] = self.registers["__loops__"][args[0]] - 1

    def je(self, args):
        if self.registers["__cmp__"][0] == self.registers["__cmp__"][1]:
            self.registers["__cursor__"] = self.registers["__loops__"][args[0]] - 1

    def jne(self, args):
        if self.registers["__cmp__"][0] != self.registers["__cmp__"][1]:
            self.registers["__cursor__"] = self.registers["__loops__"][args[0]] - 1

    def jge(self, args):
        if self.registers["__cmp__"][0] >= self.registers["__cmp__"][1]:
            self.registers["__cursor__"] = self.registers["__loops__"][args[0]] - 1

    def jg(self, args):
        if self.registers["__cmp__"][0] > self.registers["__cmp__"][1]:
            self.registers["__cursor__"] = self.registers["__loops__"][args[0]] - 1

    def jle(self, args):
        if self.registers["__cmp__"][0] <= self.registers["__cmp__"][1]:
            self.registers["__cursor__"] = self.registers["__loops__"][args[0]] - 1

    def jl(self, args):
        if self.registers["__cmp__"][0] < self.registers["__cmp__"][1]:
            self.registers["__cursor__"] = self.registers["__loops__"][args[0]] - 1

    def call(self, args):
        self.registers["__return_cursor__"].append(self.registers["__cursor__"])
        self.registers["__cursor__"] = self.registers["__loops__"][args[0]] - 1

    def ret(self, args):
        self.registers["__cursor__"] = self.registers["__return_cursor__"].pop()

    def msg(self, args):
        self.registers["__output__"] += "".join([str(self.read(arg)) for arg in args])

    def end(self, args):
        return 1

if __name__ == "__main__":
    with open('assembler.txt', encoding='utf-8') as f:
        program = f.read().replace("{input}", input("> "))
    
    a = Assembler(program)
    print(a.run())