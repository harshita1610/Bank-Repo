import yaml
import pprint as pp

with open('John_Acc.yml','r') as f :
     result = yaml.safe_load(f)
pp.pprint(result)