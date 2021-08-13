
counter_sequence = 0
sequence = [0] * 6

def store_list():
    global counter_sequence

    for i, y in enumerate(sequence):
        if(counter_sequence == i ):
            sequence[i] = sequence[i]+1
    counter_sequence = 0

def find_sequence(list):
    global counter_sequence
    y1 = 0
    y2 = 0

    for x in list:
        y2 = x
        if y2 == y1+1 and x != 1: 
            counter_sequence += 1
        elif list.index(x) != 0: #check array start
            store_list()
        if len(list)-1 == list.index(x): #check array end
            store_list()
        y1 = x

    return sequence


