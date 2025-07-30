package authz

default allow = false

allow if {
  input.username == "admin@mh-cybersolutions.de"
  input.device == "trusted"
}
