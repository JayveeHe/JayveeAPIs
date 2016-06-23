import json

from flask import Flask, request, make_response
from apis.crawlers.cloud_music import get_searchlist
from apis.log_utils import api_logger
from apis.nlp_tools.textrank_utils import text_rank

__author__ = 'jayvee'

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def test_service():
    return 'running'


@app.route('/api/textrank', methods=['POST'])
def api_textrank():
    api_logger.info('[%s][textrank]request = %s' % (request.remote_addr, request.data.strip()))
    json_data = json.loads(request.data.strip())
    sentences = json_data['sentences']
    topk = int(json_data.get('topk', 5))
    res = text_rank(sentences, num=topk)
    return make_response(json.dumps({'results': res}, ensure_ascii=False, encoding='utf8'), 200)


@app.route('/api/music', methods=['POST'])
def api_cloud_music():
    api_logger.info('[%s][music]request = %s' % (request.remote_addr, request.data.strip()))
    json_data = json.loads(request.data)
    song_name = json_data['song_name']
    limit = int(json_data.get('limit', 5))
    res = get_searchlist(song_name, limit=limit)
    return make_response(json.dumps({'results': res}, ensure_ascii=False, encoding='utf8'), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3344, debug=False)
