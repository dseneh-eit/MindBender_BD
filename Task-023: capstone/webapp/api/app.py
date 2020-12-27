from flask import Flask, jsonify, Response
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from . import jsonOverride
import collections
from flask_cors import CORS

mysql = MySQL()

app = Flask(__name__, static_folder='../build', static_url_path='/')
api = Api(app)
# CORS(app)
app.json_encoder = jsonOverride.MyJSONEncoder

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'bigdata'

mysql.init_app(app)


class Home(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        query = "select sum(view_count) as total_views, \
            sum(like_count) as likes, \
                sum(dislike_count) as dislikes, \
                    sum(comment_count) as comments, \
                        sum(favorite_count) as favorites \
                            from youtube order by total_views desc;"

        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        dataList = []

        for row in data:
            d = collections.OrderedDict()
            d['views'] = row[0]
            d['likes'] = row[1]
            d['dislikes'] = row[2]
            d['comments'] = row[3]
            d['favorites'] = row[4]

            dataList.append(d)
        return jsonify(dataList)
        # return jsonify({"message": "No resource available at the home location."})


class GetAll(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM youtube order by view_count desc limit 15")
        data = cur.fetchall()
        cur.close()
        rows = cur.fetchall()
        dataList = []

        for row in data:
            d = collections.OrderedDict()
            d['id'] = row[0]
            d['publish_at'] = row[1]
            d['channel_id'] = row[2]
            d['video_title'] = row[3]
            d['channel_title'] = row[4]
            d['cagegory_id'] = row[5]
            d['view_count'] = row[6]
            d['like_count'] = row[7]
            d['dislike_count'] = row[8]
            d['favorite_count'] = row[9]
            d['comment_count'] = row[10]
            d['code'] = row[11]
            d['category'] = row[12]
            d['pub_date'] = row[13]
            d['pub_month'] = row[14]
            d['pub_day'] = row[15]
            d['pub_year'] = row[16]
            d['pub_time'] = row[17]
            d['country'] = row[18]

            dataList.append(d)
        return jsonify(dataList)

        # return jsonify(data)


class ByRegion(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        query = "select country, sum(view_count) as total_views, \
            sum(like_count) as total_likes, \
                sum(dislike_count) as total_dislikes, \
                    sum(comment_count) as total_comment, \
                        sum(favorite_count) as total_favorites \
                            from youtube group by country \
                                order by total_views desc;"

        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        dataList = []

        for row in data:
            d = collections.OrderedDict()
            d['country'] = row[0]
            d['views'] = row[1]
            d['likes'] = row[2]
            d['dislikes'] = row[3]
            d['comments'] = row[4]
            d['favorites'] = row[5]

            dataList.append(d)
        return jsonify(dataList)


class ByCategory(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        query = "select category, sum(view_count) as total_views, \
            sum(like_count) as likes, \
                sum(dislike_count) as dislikes, \
                    sum(comment_count) as comments, \
                        sum(favorite_count) as favorites \
                            from youtube group by category \
                                order by likes desc;"

        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        dataList = []

        for row in data:
            d = collections.OrderedDict()
            d['category'] = row[0]
            d['views'] = row[1]
            d['likes'] = row[2]
            d['dislikes'] = row[3]
            d['comments'] = row[4]
            d['favorites'] = row[5]

            dataList.append(d)
        return jsonify(dataList)


class RegionCategory(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        query = "select country, category, sum(view_count) as total_views, \
            sum(like_count) as likes, \
                sum(dislike_count) as dislikes, \
                    sum(comment_count) as comments, \
                        sum(favorite_count) as favorites \
                            from youtube group by country, category \
                                order by total_views"

        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        dataList = []

        for row in data:
            d = collections.OrderedDict()
            d['country'] = row[0]
            d['category'] = row[1]
            d['views'] = row[2]
            d['likes'] = row[3]
            d['dislikes'] = row[4]
            d['comments'] = row[5]
            d['favorites'] = row[6]

            dataList.append(d)
        return jsonify(dataList)


api.add_resource(Home, '/api')
api.add_resource(GetAll, '/api/list')
api.add_resource(ByRegion, '/api/region')
api.add_resource(ByCategory, '/api/category')
api.add_resource(RegionCategory, '/api/region-category')


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()

# FLASK_APP=app.py FLASK_ENV=development flask run
# Kill processes running on 5000
## -> sudo kill -9 $(sudo lsof -t -i:5000)

# Use ngrok to forward localhost to public url:
## -> ngrok http 5000
