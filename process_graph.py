import networkx as nx
import matplotlib.pyplot as plt
import os.path
import glob
from datetime import datetime
import argparse

def parseArguments():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument("-o", "--output", help="output file name", default=None)
    parser.add_argument("-t", "--timestamp", help="add or remove timestamp from output file name. optional argument value [True | False | No]", default=True)

    # Print version
    parser.add_argument("-V", "--version", action="version", version='%(prog)s - Version 1.0')

    # Parse arguments
    args = parser.parse_args()

    return args

args = parseArguments()

# Get a list of the process identifiers of the current running processes
pids = [int(os.path.basename(os.path.normpath(path))) for path in glob.glob('/proc/[0-9]*')]

def getProcessInfo(pid):

    if pid == "0":
        return {'PPid' : 0, 'Name' : "init" }
    
    else:
    
        f = open('/proc/' + str(pid) + '/status','r')
    
        lines = [line.strip() for line in f.readlines()]
        info = dict([ [l.strip() for l in line.split(':')] for line in lines if len(line.split(':')) == 2])
        
        if 'Name' not in info:
            info['Name'] = "Unknown"

        f.close()
    
    return info   

# Make a dictionary/map taking a process id and returning all of the key value information for the process
p_info = dict([(pid, getProcessInfo(pid)) for pid in pids])

# Make a dictionary/map from process id to process name
process_names = dict([(int(pid), p_info[pid]['Name']) for pid in pids])

# Add an entry for the init process which is not in /proc
process_names[0] = "init" 

# Create a mathematical graph
G = nx.Graph()

fig=plt.figure(figsize=(80,40))

# Add a node for init since it is a parent not in /proc
G.add_node('0 - init')


for pid in pids:

    name = process_names[pid]
    
    try:
        parent_id = int(p_info[pid]['PPid'])
    except:
        parent_id = 0

    # Add the process to the graph
    G.add_node(str(pid) + " - " +name)

    # Add a connection from this process to its parent process in the graph 
    G.add_edge(str(pid) + " - " + name, str(parent_id) + " - " + process_names[parent_id])
        
# Draw the mathematical graph onto the screen
nx.draw(G, with_labels=True, node_color='#5D080D', node_size=1500, edge_color='white',font_color='white', width=1)

# Set the background color to black and save.
fig.set_facecolor("#000000")

# generate name for output file having ISO 8601 date format
date = datetime.now()
file_name = (args.output if args.output else 'process_graph') + ( '' if (args.timestamp == 'False' or args.timestamp == 'No') else '_' +date.strftime('%Y-%m-%dT%H-%M-%S') + '.png')


plt.savefig(file_name, facecolor=fig.get_facecolor())