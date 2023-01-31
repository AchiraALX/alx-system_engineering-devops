#!/usr/bin/env ruby
#

def match_cases(string)
  # Regular expression for matching cases
  pattern = /hb(t{1,})n/

  # Match cases in the string
  matches = string.scan(pattern)

  # Return array of matched cases
  return matches.flatten
end

string = ARGV[0]
matches = match_cases(string)
puts matches

