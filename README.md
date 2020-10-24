# py_process_graph

A simple script to create a graph of Linux processes. This works by 
parsing the /proc filesystem to get pairs of child and parent 
processes.  These are then fed into the NetworkX graph library and 
rendered using matplotlib.

## Example

![Alt text](out.png?raw=true "Linux Process Graph")

 
 <br>

# <span style="color:green">How to Get Started!</span>

### 1. Open your terminal

### 2. Clone the project on your machine.

    git clone https://github.com/smithandrewl/py_process_graph.git


### 3. Go to your project directory
    cd py_process_graph

### 4. Make sure you have all the dependencies installed.

- To install networkx library 

        pip install networkx

- To install matplotlib library
    
        pip install matplotlib

### 5. Now execute the code
    python process_graph.py

### 6. checkout the `process_graph_<timestamp>.png` file in your project directory for output
