# -*- coding: utf-8 -*-

from flask import Flask, render_template, request #, make_response, jsonify
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

# トップページ
@app.route('/')
def root():
  return render_template('index.html',result = '')

@app.route("/data", methods=["POST"])  #追加
def data():
  res = request.form
  # 解析する 
  #res['log']
  return render_template('index.html',result = '成功')

if __name__ == '__main__':
  app.run(debug=True)
