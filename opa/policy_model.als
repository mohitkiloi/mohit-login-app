module ci_cd_policy

// 1. Define types
sig Branch {}
one sig Main extends Branch {}

sig Approval {
  approved: Bool
}

abstract sig Bool {}
one sig True extends Bool {}
one sig False extends Bool {}

// 2. Define a commit event
sig Commit {
  branch: Branch,
  approval: Approval
}

// 3. The Policy: Only allow commit if on main AND approved
pred allow(c: Commit) {
  c.branch = Main and c.approval.approved = True
}

// 4. Check: is there any commit that violates the policy?
assert NoPolicyViolation {
  all c: Commit |
    allow[c] or not (c.branch = Main and c.approval.approved = True)
}

check NoPolicyViolation for 3
