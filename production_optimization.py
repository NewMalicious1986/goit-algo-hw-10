import pulp

# Create the Linear Programming model (default is maximization)
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Define decision variables:
# x represents the number of units of "Lemonade"
# y represents the number of units of "Fruit Juice"
# Here we use integer variables as the products are counted in whole units.
x = pulp.LpVariable("Lemonade", lowBound=0, cat=pulp.LpInteger)
y = pulp.LpVariable("Fruit_Juice", lowBound=0, cat=pulp.LpInteger)

# Objective Function: maximize the total production of products
model += x + y, "Total_Production"

# Resource Constraints:

# 1. Water constraint:
# "Lemonade" requires 2 units of water and "Fruit Juice" requires 1 unit per product.
model += 2 * x + 1 * y <= 100, "Water_Constraint"

# 2. Sugar constraint:
# Only "Lemonade" uses sugar, and it requires 1 unit per product.
model += x <= 50, "Sugar_Constraint"

# 3. Lemon Juice constraint:
# Only "Lemonade" uses lemon juice, and it requires 1 unit per product.
model += x <= 30, "Lemon_Juice_Constraint"

# 4. Fruit Puree constraint:
# Only "Fruit Juice" uses fruit puree, and it requires 2 units per product.
model += 2 * y <= 40, "Fruit_Puree_Constraint"

# Solve the problem
model.solve()

# Print the status of the solution
print("Solution Status:", pulp.LpStatus[model.status])

# Print the optimal values of the decision variables
print("Optimal number of 'Lemonade':", pulp.value(x))
print("Optimal number of 'Fruit Juice':", pulp.value(y))

# Print the maximum total production of products
print("Maximum total production:", pulp.value(model.objective))
