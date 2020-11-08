from pulp import LpVariable, LpProblem, LpInteger, LpStatus, LpMinimize, LpMaximize

prob = LpProblem("Flight_profit", LpMaximize)

rome = LpVariable("Flights_to_Rome", lowBound=0, cat=LpInteger)
seattle = LpVariable("Flights_to_seattle", lowBound=0, cat=LpInteger)


prob += (
    (2500 * rome) +
    (2000 * seattle)

), "Objective Function"

prob += rome + seattle <= 12, "hours_gate_is_open"
prob += 15*rome + 10*seattle <= 150, "hours_crew_can_work_a_day"
prob += rome <= 9, "max_rome_flights"


print("number", prob.solve())
print("Status", LpStatus[prob.status], '\n')

for i in prob.variables():
    print(i.name, "=", i.varValue)
