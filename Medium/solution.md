# Solution to Medium Web Exploitation
Flag - CompSoc{C00K13_M0N$TAR}

1. The Riddle's answer is Cookie
2. Analyse your cookies via `Inspect Element>Application>Cookies`
3. The contents of flag-🧠💦 is ```++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>-----.>++++++++.+.++.++++.+.<<++.>+++++++++++++++++++.>------------.---.+++++++++++++.-------------.<<+.-.>---.<++++++++++++++++++.+++++++.>>+++++++++++++++.-----------------.<-----------.++++++++.>+++++++++++++++++++.<+++++++++++.<------.>>--.<<+++++++++++++++++.+++++++++.---------.--.++++++++++.+.>-----.<+.>>--------------.<..<------------.>-----.-----.<++++.>++++++++.<----.>+++.>++++++++.<<------------------.+++++++++++++.
```
4. When "Compiled" using a Brainfuck Compiler, it outputs the string `Almost There! Q29tcFNvY3tDMDBLMTNfTTBOJFRBUn0=`
5. The End bit is base64 encoded. When decoded it returns the flag CompSoc{C00K13_M0N$TAR}