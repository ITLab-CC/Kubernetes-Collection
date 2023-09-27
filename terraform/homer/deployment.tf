resource "kubernetes_deployment" "homer"{
    metadata {
      name = "homer"
      labels = {
        App = "homer"
      }
    }
    spec {
        replicas = 1
        selector {
            match_labels = {
                App = "homer"
            }
        }
      template {
        metadata {
          labels = {
            App = "homer"
          }
        }
        spec {
          container {
            image = "ghcr.io/bastienwirtz/homer:v23.05.1"
            name  = "homer"

            port {
              container_port = 8080
            }
            resources {
                limits = {
                    cpu    = "0.5"
                    memory = "512Mi"
                }
                requests = {
                    cpu    = "250m"
                    memory = "50Mi"
            }
            
          }
          volume_mount {
            name = "homer-config"
            mount_path = "/www/assets/config.yml"
            sub_path = "config.yml"
          }

        }
        volume {
            name = "homer-config"
            config_map {
                name = kubernetes_config_map.homer-config.metadata[0].name
            }
        }
      }
    }
    }
}