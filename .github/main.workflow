workflow "Update image on Docker Hub" {
  on = "push"
  resolves = ["docker tag"]
}

action "docker build" {
  uses = "actions/docker/cli@8cdf801b322af5f369e00d85e9cf3a7122f49108"
  args = "build -t $GITHUB_REPOSITORY ."
}

action "docker tag" {
  uses = "actions/docker/tag@8cdf801b322af5f369e00d85e9cf3a7122f49108"
  needs = ["docker build"]
}
