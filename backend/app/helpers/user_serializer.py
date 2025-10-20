from bson import ObjectId

def user_serializer(user)-> dict:
    return {
        'id':str(user('_id')),
        'name': user['name'],
        'email': user['email'],
        'password': user['password'],
        'createdAt': user.get('createdAt')
    }