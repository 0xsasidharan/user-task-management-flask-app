from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.String(required=True)
    user_id = fields.Integer(dump_only=True)


class TaskSchema(Schema):
    title = fields.String(required=True)
    task_id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)

class TaskUpdateSchema(Schema):
    title = fields.String(required=True)
    user_id = fields.Integer(dump_only=True)

