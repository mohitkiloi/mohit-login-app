package pipeline

default allow = false

allow if {
  input.role == "admin"
  input.branch == "main"
}

allow if {
  input.role == "developer"
  input.branch == "dev"
}

deny[msg] if {
  not allow
  msg := sprintf("Access denied for role '%v' on branch '%v'", [input.role, input.branch])
}
