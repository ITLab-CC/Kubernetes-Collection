

resource "kubernetes_service" "homer" {
  metadata {
    name = "homer"
  }
  spec {
    selector = {
      App = kubernetes_deployment.homer.spec.0.template.0.metadata[0].labels.App
    }
    port {
      node_port   = 30201
      port        = 8080
      target_port = 8080
    }

    type = "NodePort"
  }
  
}

resource "kubernetes_service" "homer2" {
    metadata {
        name = "homer2"
    }
    spec {
        selector = {
        App = kubernetes_deployment.homer.spec.0.template.0.metadata[0].labels.App
        }
        port {
        node_port   = 30202
        port        = 8080
        target_port = 8080
        }
    
        type = "NodePort"
    }
    
}