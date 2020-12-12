# Relations
A Python script which reads a .txt file, then determines a relation's properties, its Boolean matrix representation, and its closure sets.

Example Input
{1, 2, 3, 4, 5, 6, 7}
{(1, 1), (1, 3), (1, 4), (2, 2), (2, 7), (3, 1), (3, 3), (3, 4), (4, 1), (4, 3), (4, 4), (5, 5), (5, 6), (6, 5), (6, 6), (7, 2), (7, 7)}

Example Output
Relation1.txt Information
S = {1, 2, 3, 4, 5, 6, 7}
R: S→S = {(1, 1), (1, 3), (1, 4), (2, 2), (2, 7), (3, 1), (3, 3), (3, 4), (4, 1), (4, 3), (4, 4), (5, 5), (5, 6), (6, 5), (6, 6), (7, 2), (7, 7)}
   |  1  2  3  4  5  6  7
---+---------------------
  1|  1  0  1  1  0  0  0
  2|  0  1  0  0  0  0  1
  3|  1  0  1  1  0  0  0
  4|  1  0  1  1  0  0  0
  5|  0  0  0  0  1  1  0
  6|  0  0  0  0  1  1  0
  7|  0  1  0  0  0  0  1
The properties of the relation:
Reflexive                     	True
Irreflexive                   	False
Symmetric                     	True
Asymmetric                    	False
Antisymmetric                 	False
Transitive                    	True
Equivalence Relation          	True
Partial Ordering              	False

Reflexive Closure: {}
Symmetric Closure: {}
Transitive Closure: {}
