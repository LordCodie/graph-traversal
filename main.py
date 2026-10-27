"""
    - problem: 
        I need to find the quickest pathway from my starting point
        to my final ending point, every specific endpoint has a
        number assigned to it.
        
    - Input/Output: 
        Function None -> ["node", "node", "node"]
    
    - Short Story:
        I need the code to calculate and collect and record 
        the value of the last stop until it it reaches the final
        stop. The record of the last stops should accumilate to 
        a final number and the smallest number returned is the shortest
        route.
        
    - Tools:
        - dictionary: data structure
        - for loop
        - lists
"""

def find_shortest_pathway():
    graph_layout = {
        ("A", "C"): 70,
        ("C", "E"): 15,
        ("E", "F"): 15,
        ("A", "B"): 50,
        ("B", "D"): 25,
        ("D", "F"): 5,
        ("B", "E"): 45
    }
    
    pin_point = ["A", 0]
    curr="A"
    last_stops = []
    
    for x, y in graph_layout.items():
        current_stop_point = x # tuple
        current_distance = y # number between the two points
        
        if pin_point[0] in current_stop_point:
            print("Potential pathways:", current_stop_point)
            pin_point[0] = x[1]
            curr=x[1]
            pin_point[1] = y
            if pin[]
            
    
find_shortest_pathway()
