from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import Elasticache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("Clustered Web Service", show=True):
    with Cluster("Services"):
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]
    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - RDS("userdb -ro")

    memcached = Elasticache("memcached")
    dns = Route53("dns")
    lb = ELB("load balancer")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
