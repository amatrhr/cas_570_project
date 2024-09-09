# School Closing Network model
- This is a model of a network O(100) nodes, each representing a school
- Schools are treated as being designed to have a minimum viable enrollment, a maximum enrollment capacity, and an maximum absolute rate of change of enrollment (MARCE)
    + If, due to demographic factors, a school is planned to lose sufficient students that it would end up under its minimum viable enrollment, then all remaining students will need to be sent to other schools on the network, and similarly for schools that would be over capacity
    + However, a neighboring school can only transfer a limited number of students, and will pass through any students that, if accepted, would exceed the MARCE
- A dirichlet-multinomial model of school attachment is planned, with the intent that over repeated iterations, schools learn the 'MARCE's of all other schools  this network and attach to them preferentially 
