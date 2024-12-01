from flask import request, jsonify
from . import rides_bp




@rides_bp.route('/order', methods=['POST'])
def create_order():
    try:
        data = request.get_json()  # Получаем данные в формате JSON
        print("Received order:", data)  # Для проверки, можно записать в лог

        # Пример обработки данных: вы можете сохранять их в базе данных
        # order = Order(
        #     departure_point=data.get('departurePoint'),
        #     destination_point=data.get('destinationPoint'),
        #     payment_method=data.get('paymentMethod'),
        #     time_type=data.get('timeType'),
        #     departure_time=data.get('departureTime'),
        #     number_of_people=data.get('numberOfPeople'),
        # )
        # db.session.add(order)
        # db.session.commit()

        # Вернем успешный ответ
        return jsonify({"message": "Order created successfully!"}), 200

    except Exception as e:
        print(f"Error processing the order: {e}")
        return jsonify({"error": "Failed to create order"}), 400




@rides_bp.route('/<int:ride_id>/track', methods=['GET'])
def track_ride(ride_id):
    # Отслеживание лодки
    pass
