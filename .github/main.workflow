workflow "Update image on Docker Hub" {
  resolves = ["Docker Tag"]
  on = "push"
}

action "Docker Tag" {
  uses = "actions/docker/tag@8cdf801b322af5f369e00d85e9cf3a7122f49108"
}
