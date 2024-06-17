# Run using python test_file.py

import sys
sys.path.insert(0, "..")
import citylearn
from citylearn.agents.rbc import BasicRBC as Agent
# RandomAgent, RLAgent
from citylearn.citylearn import CityLearnEnv
from citylearn.electric_vehicle import ElectricVehicle

dataset_name = 'citylearn_2022_phase_all_plus_evs'

# dataset_name = 'citylearn_challenge_2023_phase_2_local_evaluation'
env = CityLearnEnv(dataset_name, central_agent=True)
model = Agent(env)
model.learn(episodes=1)

# print cost functions at the end of episode
kpis = model.env.evaluate()
kpis = kpis.pivot(index='cost_function', columns='name', values='value').round(3)
kpis = kpis.dropna(how='all')
print(kpis)

print(citylearn.data.DataSet.get_names())