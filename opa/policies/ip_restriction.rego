package ip_restriction

default allow = false

trusted_ips = {
  "192.168.1.100": true,
  "192.168.1.101": true,
  "127.0.0.1": true
}

allow if {
  input.ip != ""
  trusted_ips[input.ip]
}
