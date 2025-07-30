package time_based

default allow = false

allow if {
  input.time != ""
  hour := to_number(split(input.time, ":")[0])
  hour >= 9
  hour <= 18
}
