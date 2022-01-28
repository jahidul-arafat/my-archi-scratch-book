from diagrams import Diagram, Cluster
from diagrams.oci.compute import OKE, Container, Functions
from diagrams.oci.storage import ObjectStorage
from diagrams.custom import Custom

with Diagram("Event Processing", show=True):
    # Creating Custom Components
    # cc_adw = Custom("oci-adw", "./custom_resources/dbs_adw.png")
    # cc_sqs = Custom("OCI RabbitMQ Service", "./custom_resources/integration_rabbitmq.png")

    # Creating individual components: OKE
    source = OKE("k8s source")

    with Cluster("Event Flows"):
        with Cluster("Event Workers"):
            workers_list = [Container("worker1"),
                            Container("worker2"),
                            Container("worker3")]
        cc_queue = Custom("OCI RabbitMQ Service", "./custom_resources/integration_rabbitmq.png")
        with Cluster("Processing"):
            handlers_list = [Functions("lambda proc1"),
                             Functions("lambda proc2"),
                             Functions("lambda proc3")]
    object_store = ObjectStorage("object storage:: event store")
    cc_adw = Custom("oci-adw", "./custom_resources/dbs_adw.png")

    # wire the components
    source >> workers_list >> cc_queue >> handlers_list
    handlers_list >> object_store
    handlers_list >> cc_adw
