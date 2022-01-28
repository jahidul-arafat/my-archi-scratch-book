from diagrams import Cluster, Diagram
from diagrams.oci.compute import VM
from diagrams.oci.database import ADB
from diagrams.oci.network import LoadBalancer
from diagrams.oci.connectivity import DNS
from diagrams.custom import Custom

with Diagram("Clustered Web Service @OCI", show=True):
    # Creating the custom components not available in the OCI library
    cc_redis = Custom("oci-redis", "./custom_resources/dbs_redis.png")

    # Creating the Clusters: of Compute Instances and Databases
    with Cluster("Services"):
        svc_group = [VM("web1"),
                     VM("web2"),
                     VM("web3")]
    with Cluster("DB Cluster"):
        db_primary = ADB("userdb")
        db_primary - ADB("userdb -ro")

    # Creating independent components: DNS, Load Balancer
    dns = DNS("dns")
    lb = LoadBalancer("load balancer")

    # wiring the components
    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> cc_redis
