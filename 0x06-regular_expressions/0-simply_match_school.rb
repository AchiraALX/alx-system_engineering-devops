#!/usr/bin/env ruby
# Accepts one argument and passes it to a regular expression
regex = /School/

if ARGV[0] = ~ regex
  puts ARGV[0]
else
  puts "No match"
end

