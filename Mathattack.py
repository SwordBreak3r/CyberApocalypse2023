import socket
import re

HOST = '$IP'
PORT = $PortNumber

math_regex = r'\[(\d+)\]: (.+?) = \?'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'1\n')
    
    while True:
        data = s.recv(1024).decode()
        print(data.strip())

        if 'HTB{' in data:
            print('Flag:', re.findall('HTB{.+}', data)[0])
            break

        match = re.search(math_regex, data)
        if not match:
            print('Error: could not extract question')
            continue
        problem_id = match.group(1)
        math_problem = match.group(2)

        try:
            math_answer = str(round(eval(math_problem), 2))
            if float(math_answer) < -1337 or float(math_answer) > 1337:
                math_answer = 'MEM_ERR'
        except ZeroDivisionError:
            math_answer = 'DIV0_ERR'
        except (SyntaxError, NameError):
            math_answer = 'SYNTAX_ERR'
        except MemoryError:
            math_answer = 'MEM_ERR'
        print('Answer:', math_answer)
        s.sendall((math_answer + '\n').encode())

    while True:
        data = s.recv(1024).decode()
        if not data:
            break
        print(data.strip())

    s.close()