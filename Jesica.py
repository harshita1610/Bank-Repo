import yaml
import pprint as pp

with open('Jesica.yml','r') as f :
     result = yaml.safe_load(f)
pp.pprint(result)