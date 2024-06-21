class RegexParser:
    def __init__(self, pattern):
        self.pattern = pattern
        self.index = 0

    def parse(self):
        return self.expression()

    def expression(self):
        nodes = []
        while self.index < len(self.pattern) and self.pattern[self.index] not in ")":
            term = self.term()
            if self.index < len(self.pattern) and self.pattern[self.index] == "*":
                self.index += 1
                term = StarNode(term)
            nodes.append(term)
        return nodes

    def term(self):
        if self.index >= len(self.pattern):
            raise ValueError("Unexpected end of pattern")
        char = self.pattern[self.index]
        self.index += 1
        if char == ".":
            return AnyNode()
        else:
            return CharNode(char)


class CharNode:
    def __init__(self, char):
        self.char = char


class AnyNode:
    pass


class StarNode:
    def __init__(self, node):
        self.node = node


class State:
    def __init__(self):
        self.transitions = {}
        self.is_final = False


def add_transition(state, char, next_state):
    if char not in state.transitions:
        state.transitions[char] = []
    state.transitions[char].append(next_state)


def build_nfa(nodes):
    start_state = State()
    current_state = start_state

    for node in nodes:
        if isinstance(node, CharNode):
            next_state = State()
            add_transition(current_state, node.char, next_state)
            current_state = next_state
        elif isinstance(node, AnyNode):
            next_state = State()
            for char in "abcdefghijklmnopqrstuvwxyz":
                add_transition(current_state, char, next_state)
            current_state = next_state
        elif isinstance(node, StarNode):
            star_state = State()
            add_transition(current_state, None, star_state)
            add_transition(star_state, None, current_state)
            current_state = star_state

    current_state.is_final = True
    return start_state


def match_nfa(state, s, index):
    if index == len(s):
        return state.is_final

    char = s[index]
    if char in state.transitions:
        for next_state in state.transitions[char]:
            if match_nfa(next_state, s, index + 1):
                return True

    if None in state.transitions:
        for next_state in state.transitions[None]:
            if match_nfa(next_state, s, index):
                return True

    return False


def match(pattern, s):
    parser = RegexParser(pattern)
    nodes = parser.parse()
    nfa_start = build_nfa(nodes)
    return match_nfa(nfa_start, s, 0)


# Примеры использования
print(match("a*", "aaa"))  # True
print(match("a*", ""))  # True
print(match("a.", "ab"))  # True
print(match("a.", "a"))  # False
