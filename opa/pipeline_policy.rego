package ci_cd.policy

default allow = false

allow if {
  input.branch == "main"
  input.approved == true
}
