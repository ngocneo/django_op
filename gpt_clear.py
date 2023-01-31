


from pyomo.environ import *

model = ConcreteModel()

# Define the set of stocks
# Define sets
model.item = Set(initialize=[1,2,3,4,5])
model.stock = Set(initialize=[1,2,3,4,5])


# Define the parameter for the width of each stock
model.widths = Param(model.stock, initialize={1:50, 2:75, 3:100, 4:125, 5:150})

# Define the parameter for the height of each stock
model.heights = Param(model.stock, initialize={1:100, 2:100, 3:100, 4:100, 5:100})

# Define the parameter for the width of each item
model.item_widths = Param(model.item, initialize={1:25, 2:25, 3:50, 4:75, 5:100})

# Define the parameter for the height of each item
model.item_heights = Param(model.item, initialize={1:50, 2:50, 3:50, 4:50, 5:50})

model.quantity = Param(model.item, initialize={1:1, 2:5, 3:1, 4:1, 5:1})


# Define the binary decision variables
model.x = Var(model.stock, model.item, within=Binary)

# Define the objective function
def total_cost_rule(model):
    return sum(model.x[s,i]*model.widths[s]*model.heights[s] for s in model.stock for i in model.item)

model.total_cost = Objective(rule=total_cost_rule, sense=minimize)

# Define the constraints
def width_constraint_rule(model, i):
    return sum(model.x[s,i]*model.widths[s] for s in model.stock) >= model.item_widths[i]

def height_constraint_rule(model, i):
    return sum(model.x[s,i]*model.heights[s] for s in model.stock) >= model.item_heights[i]

def quantity_constraint(model, i):
    return sum(model.x[s,i] for s in model.stock) == model.quantity[i]
model.quantity_constraint = Constraint(model.item, rule=quantity_constraint)

model.width_constraints = Constraint(model.item, rule=width_constraint_rule)
model.height_constraints = Constraint(model.item, rule=height_constraint_rule)

# Solve the optimization problem
solver = SolverFactory('glpk')
solver.solve(model, tee=True)

# Print the results
print("\n\nResults:")
for s in model.stock:
    for i in model.item:
        if (value(model.x[s,i]) > 0):
            print(f"Stock {s} cut Item {i}")


# exit()
# # Stock sizes
# stock_sizes = [(20, 30), (30, 40), (40, 50)]

# # Part sizes
# part_sizes = [(10, 20), (15, 15), (20, 25), (30, 30)]

# # Demand for each part
# part_demand = {
#     (10, 20): 10,
#     (15, 15): 20,
#     (20, 25): 30,
#     (30, 30): 5
# }

# # Maximum number of each stock size available
# stock_limit = {
#     (20, 30): 10,
#     (30, 40): 5,
#     (40, 50): 3
# }

# model = ConcreteModel()

# # Define sets
# model.I = Set(initialize=['item1', 'item2', 'item3', 'item4']) # set of items
# model.J = Set(initialize=['stock1', 'stock2','stock3']) # set of stock sizes

# # Define parameters
# model.a = Param(model.I, model.J, initialize={(20, 30), (30, 40), (40, 50)}) # size of each item
# model.b = Param(model.J, initialize={(10, 20), (15, 15), (20, 25), (30, 30)}) # size of each stock size
# model.d = Param(model.I, initialize={10,20,30,5}) # demand for each item

# # Define variables
# model.x = Var(model.I, model.J, within=NonNegativeIntegers) # number of each item cut from each stock
# model.y = Var(model.J, within=Binary) # binary variable indicating if stock j is used

# # Define objective function
# def obj_expression(model):
#     return sum(model.y[j] * model.b[j] for j in model.J)

# model.obj = Objective(rule=obj_expression, sense=minimize)

# # Define constraints
# def constraint1(model, i):
#     return sum(model.x[i, j] for j in model.J) >= model.d[i]

# model.con1 = Constraint(model.I, rule=constraint1)

# def constraint2(model, j):
#     return sum(model.x[i, j] * model.a[i, j] for i in model.I) <= model.b[j] * model.y[j]

# model.con2 = Constraint(model.J, rule=constraint2)

# # Solve the model
# solver = SolverFactory('glpk')
# results = solver.solve(model)