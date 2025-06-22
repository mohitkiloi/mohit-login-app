package ci_cd.policy

default allow = false

allow {
  input.branch == "main"
  input.approved == true
}
