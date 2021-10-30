#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2019
# ## Day 9: Sensor Boost
# https://adventofcode.com/2019/day/9

# ----
# ## Part 1
# ----

# In[1]:


import copy


# In[2]:


def run_intcode_computer(program, int_input):
    """
    Generator function version of the intcode computer
    """
    position = 0
    output = []
    opcode = ''
    program = copy.deepcopy(program) + 1000 * [0]
    
    num_params = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1] # each element maps to an opcode

    relative_base = 0
    
    while True:

        opcode_str = (5 - len(str(program[position]))) * '0' + str(program[position])
        opcode = int(opcode_str[-2:])

        # opcode 99 is terminate, takes 0 parameters    
        if opcode == 99:
            break
        
        modes = [0, int(opcode_str[-3]), int(opcode_str[-4]), int(opcode_str[-5])]
        
        arg_pos = [0] # Argument position, start list with a 0 pad
        for i in range(1, num_params[opcode] + 1):
            if i <= num_params[opcode]:
                # position mode
                if modes[i] == 0:  
                    arg_pos.append(program[position + i])
                # immediate mode
                elif modes[i] == 1: 
                    arg_pos.append(position + i)
                # relative mode
                elif modes[i] == 2:
                    arg_pos.append(relative_base + program[position + i])

        # Set next opcode position
        position += num_params[opcode] + 1
        
        # opcode 1 is addition, takes 3 parameters
        if opcode == 1:
            program[arg_pos[3]] = program[arg_pos[1]] + program[arg_pos[2]]

        # opcode 2 is multiplication, takes 3 parameters
        elif opcode == 2:
            program[arg_pos[3]] = program[arg_pos[1]] * program[arg_pos[2]]

        # opcode 3 is input, takes 1 parameter
        elif opcode == 3:  
            program[arg_pos[1]] = int_input.pop(0)
            
        # opcode 4 is output, takes 1 parameter
        elif opcode == 4:
            # yield program[arg_pos[1]]
            output.append(program[arg_pos[1]])
            
        # opcode 5, jump if true, takes 2 parameters
        elif opcode == 5:
            if program[arg_pos[1]] == True:
                position = program[arg_pos[2]]
        
        # opcode 6, jump if false, takes 2 parameters
        elif opcode == 6:
            if program[arg_pos[1]] == False:
                position = program[arg_pos[2]]
        
        # opcode 7, less than, takes 3 parameters
        elif opcode == 7:
            if program[arg_pos[1]] < program[arg_pos[2]]:
                program[arg_pos[3]] = 1
            else:
                program[arg_pos[3]] = 0

        # opcode 8, equals, takes 3 parameters
        elif opcode == 8:
            if program[arg_pos[1]] == program[arg_pos[2]]:
                program[arg_pos[3]] = 1
            else:
                program[arg_pos[3]] = 0
                
        # opcode 9, adjust relative base, takes 1 parameter
        elif opcode == 9:
            relative_base += program[arg_pos[1]]     
    
    return output


# ## Test Data

# In[3]:


test_pgms = [[109,1,204,-1,1001,10,1,100,1008,100,16,101,1006,101,0,99],
             [1102,34915192,34915192,7,4,7,99,0],
             [104,1125899906842624,99]]


# In[4]:


# Should write out the input program (Quine - https://en.wikipedia.org/wiki/Quine_(computing))
run_intcode_computer(test_pgms[0], [1])


# In[5]:


# Should write out a 16 digit number
len(str(run_intcode_computer(test_pgms[1] + 1000 * [0], [1])[0]))


# In[6]:


# Should write out 1125899906842624
run_intcode_computer(test_pgms[2] + 1000 * [0], [1])[0]


# ## Read in the Boost program

# In[7]:


with open("inputs\\boost.txt") as file:
    for line in file:
        program = [int(x) for x in line.split(',')] 


# In[8]:


run_intcode_computer(program, [1])[0]


# ----
# ## Part 2
# ----
# Run with 2 as input

# In[9]:


get_ipython().run_cell_magic('time', '', 'run_intcode_computer(program, [2])[0]')

