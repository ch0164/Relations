import numpy as np  # Used for the Boolean matrix.


# Calculate the relation's properties and display them to the screen.
def relation_check(filename):
    try:  # Parse the file for the set and relation.
        set_elements, boolean_matrix = create_boolean_matrix(filename)
    except TypeError:  # File could not be found.
        print("[ERROR] File does not exist.")
        return None
    n = len(boolean_matrix)  # Get cardinality of set.
    # Calculate the relation's properties,
    # as well as the closure sets for reflexivity/symmetry/transitivity.
    reflexive, reflexive_closure = is_reflexive(set_elements, boolean_matrix, n)
    irreflexive = is_irreflexive(boolean_matrix, n)
    symmetric, symmetric_closure = is_symmetric(set_elements, boolean_matrix, n)
    asymmetric = is_asymmetric(boolean_matrix, n)
    antisymmetric = is_antisymmetric(boolean_matrix, n)
    transitive, transitive_closure = is_transitive(set_elements, boolean_matrix, n)
    equivalence_relation = is_equivalence_relation(reflexive, symmetric, transitive)
    partial_ordering = is_partial_ordering(reflexive, antisymmetric, transitive)
    # Print the relation's properties to the screen.
    print("\nThe properties of the relation:")
    print("%-30s\t%-r" % ("Reflexive", reflexive))
    print("%-30s\t%-r" % ("Irreflexive", irreflexive))
    print("%-30s\t%-r" % ("Symmetric", symmetric))
    print("%-30s\t%-r" % ("Asymmetric", asymmetric))
    print("%-30s\t%-r" % ("Antisymmetric", antisymmetric))
    print("%-30s\t%-r" % ("Transitive", transitive))
    print("%-30s\t%-r" % ("Equivalence Relation", equivalence_relation))
    print("%-30s\t%-r" % ("Partial Ordering", partial_ordering))
    # Print the closure sets of the relation.
    print("\nReflexive Closure: ", end='')
    print_closure(reflexive_closure)
    print("Symmetric Closure: ", end='')
    print_closure(symmetric_closure)
    print("Transitive Closure: ", end='')
    print_closure(transitive_closure)
    return


# Utility function used for formatting and printing the closure set string.
def print_closure(closure_set):
    s = "{"  # All sets begin with opening curly brace.
    # Format the string as a set of ordered pairs.
    for pair in closure_set:
        s += "(" + pair[0] + ", " + pair[1] + "), "
    if s == "{":          # Is the string unmodified?
        s += "}"          # Then it is the empty set.
    else:                 # Otherwise, remove the excess parenthesis and comma,
        s = s[:-2] + "}"  # then append closing curly brace.
    print(s)


# Tests if the relation is reflexive; calculates the closure set.
def is_reflexive(set_elements, boolean_matrix, n):
    if n == 0:            # The empty set
        return False, []  # is not reflexive.
    reflexive_closure = []
    ret_val = True
    # Test along the main diagonal -- if there is a 0, it is not reflexive.
    for i in range(n):
        if boolean_matrix[i][i] == 0:
            ret_val = False
            # Union the missing pair with the closure set.
            reflexive_closure.append((set_elements[i], set_elements[i]))
    return ret_val, reflexive_closure


# Tests if the relation is irreflexive.
def is_irreflexive(boolean_matrix, n):
    # Test along the main diagonal -- if there is a 1, it is not irreflexive.
    for i in range(n):
        if boolean_matrix[i][i] == 1:
            return False
    return True


# Tests if the relation is symmetric; calculates the closure set.
def is_symmetric(set_elements, boolean_matrix, n):
    ret_val = True
    symmetric_closure = []
    # If (x, y) is in R, then (y, x) is also in R.
    for i in range(n):
        for j in range(n):
            if boolean_matrix[i][j] != boolean_matrix[j][i]:
                ret_val = False
                if boolean_matrix[i][j] == 0:  # Union {(i, j)}?
                    symmetric_closure.append((set_elements[i], set_elements[j]))
                else:  # If not, union {(j, i)}.
                    symmetric_closure.append((set_elements[j], set_elements[i]))
    return ret_val, symmetric_closure


# Tests if the relation is asymmetric.
def is_asymmetric(boolean_matrix, n):
    # If (x, y) is in R, then (y, x) is not in R.
    for i in range(n):
        for j in range(n):
            if boolean_matrix[i][j] == boolean_matrix[j][i]:
                return False
    return True


# Tests if the relation is antisymmetric.
def is_antisymmetric(boolean_matrix, n):
    # If (x, y) is in R and x = y, then (y, x) is not in R.
    for i in range(n):
        for j in range(n):
            if boolean_matrix[i][j] == boolean_matrix[j][i] and i != j:
                return False
    return True


# Tests if the relation is transitive; calculates the closure set.
def is_transitive(set_elements, boolean_matrix, n):
    ret_val = True
    transitive_closure = []
    reach_matrix = boolean_matrix.copy()
    # Use Warshall's algorithm to compute the reachability matrix.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach_matrix[i][j] = reach_matrix[i][j] or (reach_matrix[i][k] and reach_matrix[k][j])
    # Compare the original Boolean matrix with the new reachability matrix.
    # If the two are not the same, then the relation is not transitive.
    for i in range(n):
        for j in range(n):
            if boolean_matrix[i][j] != reach_matrix[i][j]:
                ret_val = False
                # Union the missing pair with the closure set.
                transitive_closure.append((set_elements[i], set_elements[j]))
    return ret_val, transitive_closure


# An equivalence relation (E.R.) is a relation that is reflexive, symmetric, and transitive.
def is_equivalence_relation(reflexive, symmetric, transitive):
    return reflexive and symmetric and transitive


# An partial ordering (poset) is a relation that is reflexive, antisymmetric, and transitive.
def is_partial_ordering(reflexive, antisymmetric, transitive):
    return reflexive and antisymmetric and transitive


# Construct the set and Boolean matrix using the file provided.
def create_boolean_matrix(filename):
    try:
        f = open(filename, "r")  # Open the file containing the relation.
    except FileNotFoundError:    # If it does not exist, exit the function.
        return None
    print(filename + " Information")
    # Read the set and relation, then close the file.
    set_line = f.readline()
    rel_line = f.readline()
    f.close()
    # Parse the set.
    print("S = " + set_line, end='')      # Print the set to the screen.
    set_line = set_line[1:-2]             # Remove curly braces from the set.
    set_elements = set_line.split(", ")   # Tokenize the set into a list.
    # Parse the relation.
    print("R: S→S = " + rel_line)         # Print the relation to the screen.
    rel_line = rel_line[1:-1]             # Remove curly braces from the relation.
    rel_line = rel_line.replace('(', '')  # Clear line of opening parentheses.
    rel_line = rel_line.replace(')', '')  # Clear line of closing parentheses.
    rel_line = rel_line.replace(',', '')  # Clear line of commas.
    rel_line = rel_line.split()           # Tokenize the elements into a list.
    # Construct the nxn Boolean matrix, where n = |S|.
    boolean_matrix = np.zeros((len(set_elements), len(set_elements)), dtype=bool)
    # Read the 1D list of ordered pairs two values per iteration.
    for x in range(0, len(rel_line), 2):
        row = 0  # First element of ordered pair.
        col = 0  # Second element of ordered pair.
        # Find the first element's index on the Boolean matrix using exhaustive search.
        for i in range(len(set_elements)):
            if rel_line[x] == set_elements[i]:
                row = i
                break
        # Find the second element's index on the Boolean matrix using exhaustive search.
        for i in range(len(set_elements)):
            if rel_line[x + 1] == set_elements[i]:
                col = i
                break
        # The ordered pair is an element of the relation.
        boolean_matrix[row][col] = True
    # Print the Boolean matrix.
    print("   |", end='')
    for x in set_elements:
        print("%3s" % x, end='')
    print("\n---+" + "-" * len(set_elements) * 3, end='')
    for i in range(len(set_elements)):
        print("\n%3s|" % set_elements[i], end='')
        for j in range(len(set_elements)):
            print("%3d" % boolean_matrix[i][j], end='')
    # Return the set and relation (as a Boolean matrix) as a tuple.
    return set_elements, boolean_matrix


# Driver main function to test relations.py.
if __name__ == '__main__':
    choice = 0  # Valid choice is 1-6.
    # Print welcome + info message.
    print("Welcome to the Relations program!")
    print("Select a relation .txt file listed below.")
    print("The set and relation will be displayed;"
          " the relation will also be presented in a Boolean matrix.")
    print("Afterwards, the relation's properties will be calculated.")
    print("Finally, if the relation is not reflexive/symmetric/transitive, "
          "then the closure set will be calculated to make the respective property hold true.")
    # Enter menu.
    while True:
        # Display the menu.
        print("\n" + "-" * 34)
        print("1. Relation 1\n2. Relation 2\n3. Relation 3\n4. Relation 4")
        print("5. Custom Relation\n6. Quit")
        print("-" * 34)
        # Confirm the user's choice.
        try:
            choice = int(input("Please enter an option: "))
        except ValueError:  # Bad input -- likely a string.
            print("Please enter an integer value.")
        # Evaluate the user's choice.
        if choice == 1:
            relation_check("Relation1.txt")
        elif choice == 2:
            relation_check("Relation2.txt")
        elif choice == 3:
            relation_check("Relation3.txt")
        elif choice == 4:
            relation_check("Relation4.txt")
        elif choice == 5:  # Choice 5 is a custom relation.
            relation_check(input("Please enter the filename of the custom relation: "))
        elif choice == 6:  # Choice 6 quits the program.
            print("Goodbye!")
            break
        else:              # User did not enter a valid number.
            print("Invalid input. Try again.")
