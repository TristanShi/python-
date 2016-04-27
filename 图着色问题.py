#-*- coding: utf-8 -*-

"""图着色问题"""

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']

states = ['A', 'B', 'C', 'D']

neighbors = {}
neighbors['A'] = []
neighbors['B'] = []
neighbors['C'] = []
neighbors['D'] = []

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print colors_of_states


main()