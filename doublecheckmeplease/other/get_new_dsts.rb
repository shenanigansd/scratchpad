#!/usr/bin/env ruby

# frozen_string_literal: true

require 'json'
require 'open-uri'
require 'rest_client'
require 'dotenv'

Dotenv.load('../.env')

def search
  response = RestClient.get "#{ENV['zendesk_url']}/api/v2/search.json?query=need%20dst%20status:open%20status:pending%20status:new%20order_by:updated_at%20sort:desc%20has_attachment:true", Authorization: "Bearer #{ENV['zendesk_oauth']}"
  JSON.parse(response.body)
end

def filter_search(search)
  tickets_with_dsts_available = []
  search['results'].each do |ticket|
    subject = ticket['subject'].downcase.gsub(/,/, '').split(' ')
    subject.each { |s| tickets_with_dsts_available.push ticket['id'] if s.match?(/d...../) }
  end
  tickets_with_dsts_available
end

def download_dsts(ticket_number)
  response = RestClient.get "#{ENV['zendesk_url']}/api/v2/tickets/#{ticket_number}/comments.json", content_type: :json, Authorization: "Bearer #{ENV['zendesk_oauth']}"
  comments = JSON.parse(response.body)
  comments['comments'].each do |comment|
    comment['attachments'].each do |attachment|
      open(attachment['file_name'], 'wb') do |file|
        file << open(attachment['content_url']).read
      end
    end
  end
end

def comment_and_close(ticket_number)
  jdata = '{ "ticket": { "status": "solved", "comment": { "body": "Automatically processed", "author_id": 380031530892, "public": false } } }'
  RestClient.put "#{ENV['zendesk_url']}/api/v2/tickets/#{ticket_number}.json", jdata, content_type: :json, Authorization: "Bearer #{ENV['zendesk_oauth']}"
end

filter_search(search).each do |ticket_number|
  download_dsts ticket_number
  comment_and_close ticket_number
end
