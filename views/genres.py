from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from utils import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/movies/{genre.id}"}


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    @auth_required
    def get(self, uid):
        r = genre_service.get_one(uid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, uid):
        genre_service.delete(uid)
        return "", 204
