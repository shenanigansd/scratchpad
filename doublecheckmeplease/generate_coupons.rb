#!/usr/bin/env ruby

# frozen_string_literal: true

require 'csv'
require 'net/http'
require 'json'
require 'rest_client'
require 'dotenv'

Dotenv.load('../.env')

def create_codes
  codes = []
  2500.times do
    codes.push SecureRandom.alphanumeric 12
  end
  codes.each(&method(:puts))
  send_codes codes
end

def create_codes_for_nathan
  codes = []
  10.times do
    codes.push 'nathan' + codes.length.to_s.next
  end
  send_codes codes
end

def send_codes(codes)
  codes.each(&method(:send_api_post))
end

def send_api_post(code)
  uri = URI('https://api.bigcommerce.com/stores/zzbheyvebw/v2/coupons')
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  req = Net::HTTP::Post.new(uri.path, 'Accept' => 'application/json',
                                      'Content-Type' => 'application/json',
                                      'X-Auth-Token' => 'djvd6j8zgwwfkjrvg1z31cwkupiu7a7',
                                      'X-Auth-Client' => 'fbvcjz05ts800k9o44t7v5nd40wmald')
  req.body = generate_coupon_json code
  res = http.request(req)
  puts "response #{res.body}"
  puts JSON.parse(res.body)
rescue StandardError => e
  puts "failed #{e}"
end

def generate_coupon_json(code)
  { name: code, type: 'per_total_discount', code: code, enabled: true, min_purchase: 1, max_uses: 1, max_uses_per_customer: 1, amount: 23, applies_to: { entity: 'categories', ids: [0] } }.to_json
end

create_codes