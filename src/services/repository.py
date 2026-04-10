import boto3
from src.models.user import UserResponse
from uuid import UUID


class UserRepository:

    # En el constructor, especificamos la región para evitar el NoRegionError cuando se utiliza boto3 sin una configuración de región global.
    # Constructor para inicializar la conexión a DynamoDB y especificar la tabla a utilizar.
    def __init__(self, table_name: str, region_name: str = "us-east-1"):
        self.dynamodb = boto3.resource("dynamodb", region_name=region_name)
        self.table_name = table_name
        self.table = self.dynamodb.Table(table_name)

    def save_user(self, user: UserResponse):
        # Convertimos el modelo de Pydantic a un diccionario para DynamoDB 
        self.table.put_item(Item=user.model_dump(mode='json'))
        print(f"Usuario {user.user_id} guardado con éxito.")

    def create(self, user_data: dict):
        self.table.put_item(Item=user_data)
        return user_data

    def get(self, user_id: str):
        response = self.table.get_item(Key={'user_id': user_id})
        return response.get('Item')

    def update(self, user_id: str, update_data: dict):
        # Generamos una expresión de actualización dinámica (Senior Tip)
        # Usamos '#' para nombres y ':' para valores para evitar conflictos con palabras reservadas de DynamoDB.
        update_expr = "set " + ", ".join(f"#{k}=:{k}" for k in update_data.keys())
        # ExpressionAttributeNames: {"#email": "email", "#edad": "edad"}
        attr_names = {f"#{k}": k for k in update_data.keys()}
        # ExpressionAttributeValues: {":email": "nuevo@test.com", ":edad": 30}
        attr_values = {f":{k}": v for k, v in update_data.items()}

        response = self.table.update_item(
            Key={'user_id': user_id},
            UpdateExpression=update_expr,
            ExpressionAttributeNames=attr_names,
            ExpressionAttributeValues=attr_values,
            ReturnValues="UPDATED_NEW"
        )
        return response.get('Attributes')

    def delete(self, user_id: str):
        self.table.delete_item(Key={'user_id': user_id})
        return True