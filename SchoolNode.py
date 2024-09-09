from uuid import uuid4

class SchoolNode:
    # represents a school, expected to be at steady 
    #  state in terms of accepting and graduating    
    #  students drawn from its catchment area
    
    def __init__(self):
        #TODO remember the syntactic sugar for this!
        # Attributes:
        #   - ID -- UUID 
        #   - enrollment: int (special numpy int)
        #   - pvs enrollment: int 
        #   - forecasted enrollment: int
        #   - growth rate: float
        #   - carrying capacity: int 
        #   - change capacity: float 
        #   - TODO: include maxcapacity
        #   - isSpecial: bool
        #   - districtID:
        pass
    
    def transfer_students(self):
        # look up self.inNeighbors 
        pass
    
    def recieve_students(self):
        pass