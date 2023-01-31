from pyomo.environ import *

from pyomo.environ import *


# def solve_cutting_stock(cut_lengths, stock_lengths, num_pieces):
#     model = ConcreteModel()
#     model.x = Var(cut_lengths, within=Binary)
#     model.y = Var(stock_lengths, within=NonNegativeIntegers)
    
#     def total_length_rule(model):
#         return sum(model.y[i] * i for i in stock_lengths) >= sum(model.x[i] * i for i in cut_lengths)
    
#     model.total_length_constraint = Constraint(rule=total_length_rule)
    
#     def num_pieces_rule(model, i):
#         return model.x[i] <= num_pieces[i]
    
#     model.num_pieces_constraint = Constraint(cut_lengths, rule=num_pieces_rule)
    
#     def objective_rule(model):
#         return sum(model.y[i] for i in stock_lengths)
    
#     model.objective = Objective(rule=objective_rule, sense=minimize)
    
#     solver = SolverFactory('glpk')
#     solver.solve(model, tee=True)
    
#     return model.display()

# cut_lengths = [10, 20, 30, 40]
# stock_lengths = [50, 100, 150, 200]
# num_pieces = {10: 8, 20: 15, 30: 10, 40: 5}

# results = solve_cutting_stock(cut_lengths, stock_lengths, num_pieces)
# print("Stock lengths used:", results)




from pyomo.environ import *

model = ConcreteModel()

# Define the set of items to be cut
model.I = Set(initialize=[1,2,3,4,5])

# Define the set of available stock sizes
model.J = Set(initialize=[1,2,3])

# Define the parameters for the length of each item and each stock size
model.a = Param(model.I, initialize={1:10, 2:12, 3:8, 4:9, 5:15})
model.b = Param(model.J, initialize={1:100, 2:120, 3:150})

# Define the decision variables to represent the number of cuts made from each stock size
model.x = Var(model.J, within=NonNegativeIntegers)

# Define the objective function as the total number of stock sizes used
def objective_rule(model):
    return sum(model.x[j] for j in model.J)
model.objective = Objective(rule=objective_rule,sense=minimize)

# Define the constraints to ensure that the length of the items cut from each stock size is less than or equal to the available length of that stock size
def constraint_rule(model, i):
    return sum(model.x[j]*model.b[j] for j in model.J) >= model.a[i]
model.constraints = Constraint(model.I, rule=constraint_rule)

# Solve the optimization problem
solver = SolverFactory('glpk')
solver.solve(model)

# Print the results
print("Total Number of Stock Sizes Used: ", model.objective())
print("Number of Cuts Made from Each Stock Size:")
for j in model.J:
    print("Stock Size ", j, ": ", model.x[j]())