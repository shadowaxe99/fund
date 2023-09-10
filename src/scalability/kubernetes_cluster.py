```python
from kubernetes import client, config

class KubernetesCluster:
    def __init__(self):
        config.load_kube_config()
        self.api_instance = client.CoreV1Api()

    def list_pods(self, namespace='default'):
        return self.api_instance.list_namespaced_pod(namespace)

    def create_deployment(self, deployment_data):
        api_instance = client.AppsV1Api()
        api_response = api_instance.create_namespaced_deployment(
            body=deployment_data,
            namespace="default")
        return api_response

    def update_deployment(self, deployment_name, deployment_data):
        api_instance = client.AppsV1Api()
        api_response = api_instance.patch_namespaced_deployment(
            name=deployment_name,
            namespace="default",
            body=deployment_data)
        return api_response

    def delete_deployment(self, deployment_name):
        api_instance = client.AppsV1Api()
        api_response = api_instance.delete_namespaced_deployment(
            name=deployment_name,
            namespace="default",
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        return api_response

    def scale_deployment(self, deployment_name, replicas):
        api_instance = client.AppsV1Api()
        scale = client.V1Scale()
        scale.spec = client.V1ScaleSpec()
        scale.spec.replicas = replicas
        api_response = api_instance.patch_namespaced_deployment_scale(
            name=deployment_name,
            namespace="default",
            body=scale)
        return api_response
```