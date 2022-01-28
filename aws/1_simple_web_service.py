# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Lab1_Simple_Web_Service", show=True):
    ELB("Load Balancer") >> EC2("Web") >> RDS("User Database")
