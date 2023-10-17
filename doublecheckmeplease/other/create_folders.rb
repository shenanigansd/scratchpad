#!/usr/bin/env ruby

# frozen_string_literal: true

require 'fileutils'

thousand = File.basename(Dir.getwd).split(' ')[0].to_i

1000.times do |x|
  FileUtils.mkdir_p((thousand + 999 - x).to_s)
end
