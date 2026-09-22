from flask import Flask, request, jsonify
from models import db, Note


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route("/notes", methods=["GET"])
    def list_notes():
        notes = Note.query.all()
        return jsonify([n.to_dict() for n in notes])

    @app.route("/notes", methods=["POST"])
    def create_note():
        data = request.get_json()
        if not data or "title" not in data:
            return jsonify({"error": "title required"}), 400
        note = Note(title=data["title"], body=data.get("body", ""))
        db.session.add(note)
        db.session.commit()
        return jsonify(note.to_dict()), 201

    @app.route("/notes/<int:note_id>", methods=["GET"])
    def get_note(note_id):
        note = Note.query.get(note_id)
        if not note:
            return jsonify({"error": "not found"}), 404
        return jsonify(note.to_dict())

    @app.route("/notes/<int:note_id>", methods=["PUT"])
    def update_note(note_id):
        note = Note.query.get(note_id)
        if not note:
            return jsonify({"error": "not found"}), 404
        data = request.get_json()
        note.title = data.get("title", note.title)
        note.body = data.get("body", note.body)
        db.session.commit()
        return jsonify(note.to_dict())

    @app.route("/notes/<int:note_id>", methods=["DELETE"])
    def delete_note(note_id):
        note = Note.query.get(note_id)
        if not note:
            return jsonify({"error": "not found"}), 404
        db.session.delete(note)
        db.session.commit()
        return "", 204

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    create_app().run(debug=True)