#def command(result, cmd):
#    print(result, cmd[0])
#    if cmd[0] == 'insert':
#        result.insert(int(cmd[1]), int(cmd[2]))
#        return result
#    elif cmd[0] == 'remove':
#        result.remove(int(cmd[1]))
#        return result
#    elif cmd[0] == 'append':
#        result.append(int(cmd[1]))
#        return result
#    elif cmd[0] == 'pop':
#        result.pop()
#        return result
#    elif cmd[0] == 'reverse':
#        result.reverse()
#        return result
#    elif cmd[0] == 'print':
#        print(result)
#        return result
#    elif cmd[0] == 'sort':
#        return sorted(result)
#    else:
#        print('Invalid command')


#def main():
#    N = int(input())
#    ans = []

#    while N:
#        ans = command(ans, input().split())
#       print(ans)
#        N -= 1


#if __name__ == '__main__':
#    main()



### Elegant one ###

def lines_from_stdin(n):
    n = int(n)
    for i in range(n):
        yield input().rstrip('\n').split()

def matching_lines(lines, patterns):
    for line in lines:
        for pattern in patterns:
            if pattern in line:
                yield line

def matching_lines_from_stdin(pattern, n):
    lines = lines_from_stdin(n)
    matching = matching_lines(lines, pattern)
    yield from matching

def map_list_commands(n):
    answer = list()
    funcs = dir(list) + ['print']
    matching = matching_lines_from_stdin(funcs, n)
    for vals in matching:
        func = vals[0]
        if func in dir(list):
            try:
                val1, val2 = int(vals[1]), int(vals[2])
                method = getattr(answer, func)(val1, val2)
            except IndexError:
                try:
                    val1 = int(vals[1])
                    method = getattr(answer, func)(val1)
                except IndexError:
                    method = getattr(answer, func)()
        elif func == 'print':
            print(answer)

if __name__ == '__main__':
    N = int(input())
    map_list_commands(N)
