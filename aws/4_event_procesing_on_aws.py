from diagrams import Diagram, Cluster
from diagrams.aws.analytics import Redshift
from diagrams.aws.compute import EKS, ECS, Lambda
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Event Processing", show=True):
    source = EKS("k8s source")
    with Cluster("Event Flows"):
        with Cluster("Event Workers"):
            workers_list = [ECS("worker1"),
                            ECS("worker2"),
                            ECS("worker3")]
        queue = SQS("event queue")
        with Cluster("Processing"):
            handlers_list = [Lambda("lambda proc1"),
                            Lambda("lambda proc2"),
                            Lambda("lambda proc3")]
    object_store = S3("object storage:: event store")
    data_warehouse = Redshift("Analytics:: dw")

    # wire the components
    source >> workers_list >> queue >> handlers_list
    handlers_list >> object_store
    handlers_list >> data_warehouse
