resource "kubernetes_config_map" "homer-config" {
  metadata {
    name = "homer-config"
  }

  data = {
    "config.yml" = "${file("${path.module}/homer-config.yaml")}"
  }
} 