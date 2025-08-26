from marshmallow import Schema, fields, ValidationError

class ProductSchema(Schema):
    getbest = fields.Boolean(
        required=False,
        truthy={"true", "1", "yes", "on"},
        falsy={"false", "0", "no", "off"}
    )
    
class SearchSchema(Schema):
    search = fields.Str(
        required=False
    )

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class SubmitSchema(Schema):
    message = fields.Str(required=False)
    url = fields.URL(required=True)
    name = fields.Str(required=False)

submit_scheme = SubmitSchema()
login_scheme = LoginSchema()
product_scheme = ProductSchema()
search_scheme = SearchSchema()