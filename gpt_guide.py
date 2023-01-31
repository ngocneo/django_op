from pyomo.environ import *

# Create a Concrete Model
model = ConcreteModel()

# Define the sets
model.I = Set(initialize=[1, 2, 3, 4, 5])
model.J = Set(initialize=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define the parameters
model.w = Param(model.I, initialize={1: 5, 2: 6, 3: 5, 4: 4, 5: 3})
model.h = Param(model.J, initialize={1: 5, 2: 4, 3: 3, 4: 6, 5: 5, 6: 4, 7: 6, 8: 4, 9: 5, 10: 4})

# Define the variables
model.x = Var(model.I, model.J, within=Binary)

# Define the objective function
def total_area_rule(model):
    return sum(model.w[i] * model.h[j] * model.x[i, j] for i in model.I for j in model.J)

model.total_area = Objective(rule=total_area_rule, sense=maximize)

# Define the constraints
def limit_width_rule(model, j):
    return sum(model.w[i] * model.x[i, j] for i in model.I) <= 10
model.limit_width = Constraint(model.J, rule=limit_width_rule)

def limit_height_rule(model, i):
    return sum(model.h[j] * model.x[i, j] for j in model.J) <= 8
model.limit_height = Constraint(model.I, rule=limit_height_rule)

# Solve the problem
solver = SolverFactory('glpk')
solver.solve(model)

# Print the results
print("The maximum total area is: ", model.total_area())
for i in model.I:
    for j in model.J:
        if model.x[i, j].value == 1:
            print(f"Item {i} with width {model.w[i]} and height {model.h[j]} is selected.")
