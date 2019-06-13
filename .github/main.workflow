workflow "Update image on Docker Hub" {
  on = "push"
  resolves = ["docker publish"]
}

action "docker build" {
  uses = "actions/docker/cli@8cdf801b322af5f369e00d85e9cf3a7122f49108"
  args = "build -t $GITHUB_REPOSITORY ."
}

action "Docker Login" {
  uses = "actions/docker/login@8cdf801b322af5f369e00d85e9cf3a7122f49108"
  needs = ["docker build"]
  secrets = ["DOCKER_USERNAME", "DOCKER_PASSWORD"]
}

action "docker publish" {
  uses = "actions/docker/cli@8cdf801b322af5f369e00d85e9cf3a7122f49108"
  needs = ["Docker Login"]
  args = "push $GITHUB_REPOSITORY"
}
