from flask import Flask, request, jsonify, Response
from summa import keywords as keywordExtractor
from summa import summarizer
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def summary ():
  messages = json.loads(request.data)['messages']
  concatenatedMessages = '. '.join(messages)
  summarized = summarizer.summarize(concatenatedMessages)
  keywords = keywordExtractor.keywords(concatenatedMessages)
  responseContent = {
    'summarized': summarized,
    'keywords': keywords
  }
  response = jsonify(responseContent)
  response.status_code = 200
  return response
