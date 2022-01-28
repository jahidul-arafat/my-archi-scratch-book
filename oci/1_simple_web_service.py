from diagrams import Diagram
from diagrams.oci.compute import VM
from diagrams.oci.network import LoadBalancer
from diagrams.oci.database import ADB

with Diagram("Simple Web Service @ OCI"):
    lb = LoadBalancer("load balancer")
    web = VM("web instance")
    db = ADB("User Database")

    # wire the components
    lb >> web >> db


