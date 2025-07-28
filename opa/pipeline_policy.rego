package ci_cd.policy

default allow = false

# Allow only if on main branch, approved, and role is admin
allow {
  input.branch == "main"
  input.approved == true
  input.role == "admin"
}
