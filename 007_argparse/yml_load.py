import yaml

# yaml_document = """
# app:
#   name: "auth-service"
#   environment: "production"
#   replicas: 3
#   ports:
#     - 80
#     - 443
# database:
#   host: "db-primary.internal"
#   port: 5432
#   ssl_enabled: true
# """

# config = yaml.safe_load(yaml_document)

# print(type(config))
# print(f"Application     : {config['app']['name']}")
# print(f"Replicas        : {config['app']['replicas']}")
# print(f"DB Endpont      : {config['database']['host']}")
# print(f"App ports       : {config['app']['ports']}")

# config['app']['replicas'] = 20

# cluster_patch = {
#     "apiVersion": "apps/v1",
#     "kind": "Deployment",
#     "metadata": {"name": "frontend-proxy"},
#     "spec": {
#         "replicas": 5,
#         "strategy": "RollingUpdate"
#     },
#     "ports": [80, 443]
# }

# yaml_output = yaml.dump(cluster_patch, sort_keys=False, default_flow_style=False)
# print("\nYaml Output:")
# print(yaml_output)

