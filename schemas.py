from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.String(required=True)
    user_id = fields.String(dump_only=True)


class TaskSchema(Schema):
    title = fields.String(required=True)
    task_id = fields.String(dump_only=True)
    user_id = fields.String(required=True)

class TaskUpdateSchema(Schema):
    title = fields.String(required=True)
    user_id = fields.String(dump_only=True)

