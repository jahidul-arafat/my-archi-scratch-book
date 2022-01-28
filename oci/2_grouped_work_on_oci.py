from diagrams import Diagram
from diagrams.oci.compute import VM
from diagrams.oci.database import ADB
from diagrams.oci.network import LoadBalancer

with Diagram("Grouped Workers", show=True, direction="TB"):
    LoadBalancer("Load Balancer") >> [
        VM("worker1"),
        VM("worker2"),
        VM("worker3"),
        VM("worker4"),
        VM("worker5")
    ] >> ADB("events")
