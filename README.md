# py_process_graph

A simple script to create a graph of Linux processes. This works by 
parsing the /proc filesystem to get pairs of child and parent 
processes.  These are then fed into the NetworkX graph library and 
rendered using matplotlib.

## Example

![Alt text](out.png?raw=true "Linux Process Graph")

