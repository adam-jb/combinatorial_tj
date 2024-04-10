
import pandas as pd
import numpy as np
import copy

df = pd.read_csv('2024-04-10 - Coloured graph edges problem (to be shared) - Coloured edges.csv')

df.head()

unique_nodes = [c for c in set(df.iloc[:,1:5].values.reshape(-1)) if isinstance(c, str)]
unique_colours = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Pink']

# each unique node can have 2 different colours

# No individual node should be part of 2 or more groups that have the same colour.
'''
Each node can be part of lots of groups, but it cant have 


'''


def get_colours(df, unique_nodes, unique_colours):

    nodes_to_colours = {}
    colour_col_values = []
    
    for node in unique_nodes:
        nodes_to_colours[node] = {c:0 for c in unique_colours}
    
    for _, row in df.iterrows():
                        
        group_nodes = [node for node in row[1:4] if pd.notna(node)]

        colours_allowed = copy.deepcopy(set(unique_colours))
        #print(colours_allowed)
        
        for node in group_nodes:
            node_colours_to_counts = nodes_to_colours[node]
            #print(node_colours_to_counts)
            for colour in unique_colours:
                if colour in colours_allowed:
                    #print(node_colours_to_counts)
                    if node_colours_to_counts[colour] > 1:
                        colours_allowed.remove(colour)
                        #print(colour)

        #print(colours_allowed)
        if len(colours_allowed) == 0:
            return f'fail on iter {_}'
        else:
            colour_this_row = list(colours_allowed)[0]

            for node in group_nodes:
                node_colours_to_counts = nodes_to_colours[node]
                node_colours_to_counts[colour_this_row] = node_colours_to_counts[colour_this_row] + 1
                nodes_to_colours[node] = node_colours_to_counts

            colour_col_values.append(colour_this_row)
            
            
        #print(unique_colours)
        
    return colour_col_values, nodes_to_colours

import traceback
try:
    res, nodes_to_colours = get_colours(df, unique_nodes, unique_colours)
except:
    print(traceback.print_exc())
    

df['Colour (no more than 7)'] = res
colour_counts_each_node = pd.DataFrame(nodes_to_colours).T

df.to_csv('combinatorial_result.csv', index = False)
colour_counts_each_node.to_csv('combinatorial_result_by_node.csv', index = False)
