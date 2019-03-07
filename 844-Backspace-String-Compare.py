def backspaceCompare(S, T):
    def process(my_str):
        result = []
        for i in range(len(my_str)):
            if my_str[i] == "#":
                if len(result) == 0:
                    continue
                else:
                    result.pop()
            else:
                result.append(my_str[i])
        return ''.join(result)

    return process(S) == process(T)



S = "a##c"
T = "c#d#"
print backspaceCompare(S, T)
