#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\w*[^\]])/).join
puts ","
puts ARGV[0].scan(/\[to:(\w*[^\]])/).join
puts ","
puts ARGV[0].scan(/\[flags:(\w*[^\]])/).join
