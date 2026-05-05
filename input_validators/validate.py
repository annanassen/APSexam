
import sys
import re
line = sys.stdin.readline()
patient0, b = line.split()

n = sys.stdin.readline()
if line[0] == '0':
    print(f"regex failing", file=sys.stderr)
    sys.exit(43)

if not re.match(r"^[A-Za-z][A-Za-z0-9]*$", patient0):
    print(f"regex failing", file=sys.stderr)
    sys.exit(43)
if not re.match(r"^[0-9]*$", b):
    print(f"regex failing", file=sys.stderr)
    sys.exit(43)

if not re.match(r"^[0-9]*$", n):
    print(f"regex failing", file=sys.stderr)
    sys.exit(43)


for _ in range(int(n)):
    line = sys.stdin.readline().split()
    node1 = line[0]
    
    if not re.match(r"^[A-Za-z][A-Za-z0-9]*$", node1):
        print(f"regex failing", file=sys.stderr)
        sys.exit(43)

    for interation in range(1,len(line), 2):
        node2 = line[interation]
        
        if not re.match(r"^[A-Za-z][A-Za-z0-9]*$", node2):
            print(f"regex failing", file=sys.stderr)
            sys.exit(43)


        time = int(line[interation+1])
        if not re.match(r"^[0-9]*$", n):
            print(f"regex failing", file=sys.stderr)
            sys.exit(43)
  
if sys.stdin.readline() != "":
    sys.exit(43)


sys.exit(42)
