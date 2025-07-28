module ci_cd_policy

sig Branch {}
one sig Main extends Branch {}

sig Approval {
  approved: Bool
}

abstract sig Bool {}
one sig True extends Bool {}
one sig False extends Bool {}

sig Commit {
  branch: Branch,
  approval: Approval,
  role: Role
}

abstract sig Role {}
one sig Admin extends Role {}
one sig Developer extends Role {}
one sig Intern extends Role {}

pred allow(c: Commit) {
  c.branch = Main and c.approval.approved = True and c.role = Admin
}

assert NoPolicyViolation {
  all c: Commit |
    allow[c] or not (c.branch = Main and c.approval.approved = True and c.role = Admin)
}

check NoPolicyViolation for 5
