from turing_machine import TuringMachine


machine = TuringMachine(
    {
        ('q0', '#'): ('saw_#', '#', 'R'),
        ('saw_#', '#'): ('saw_##', '#', 'R'),
        ('saw_##', ''): ('qa', '', 'R'),
    }
)

w = "##" #try some strings here to find out what the machine accepts and rejects
print("Input:",w)
print("Accepted?", machine.accepts(w))
machine.debug(w)
