from flask_restx import Namespace, Resource

user_ns = Namespace('user')


@user_ns.route('/')
class UserVIew(Resource):
	def post(self):
		pass