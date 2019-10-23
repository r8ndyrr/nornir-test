from nornir.core import InitNornir
from nornir.plugins.tasks.data import load_yaml
from nornir.plugins.tasks.text import template_file
from nornir.plugins.tasks.networking import napalm_configure
from nornir.plugins.functions.text import print_result

def load_data(taks):
       data = task.run(
           task=load_yaml,
           file=f'{task.host["site"]}.yaml
       )

       task.host["asn"] = data.result["asn"]
       task.host["networks"] = data.result["networks"]

