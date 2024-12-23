import pytest
from fastapi.testclient import TestClient
import uuid
from main import app

client = TestClient(app)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def creatingAStudent(client):
    feedback = client.post("/students", params={"name": "T1", "amountInWallet": 100.00})
    assert feedback.status_code == 200
    return feedback.json()


def testCreatingAStudent(client):
    feedback = client.post("/students", params={"name": "Barry Allen", "amountInWallet": 100.00})
    student_created = feedback.json()

    assert feedback.status_code == 200
    assert student_created['name'] == "Barry Allen"
    assert student_created['wallet'] == 100.00
    assert 'id' in student_created


@pytest.fixture
def creatingAGroupOrder(client):
    feedback = client.post("/group_orders/")
    assert feedback.status_code == 200
    return feedback.json()


def testCreatingAGroupOrder(client):
    feedback = client.post("/group_orders/")
    assert feedback.status_code == 200

    group_order = feedback.json()

    assert 'start_time' in group_order
    assert 'order_id' in group_order
    assert group_order['delivery_fee'] == 5.99


def testJoiningAGroupOrder(client, creatingAGroupOrder, creatingAStudent):
    group_order = creatingAGroupOrder
    student_created = creatingAStudent

    feedback = client.post(f"/group_orders/{group_order['order_id']}/join/", params={"id_student": student_created['id']})

    assert feedback.status_code == 200
    assert feedback.json()['message'] == "Group order has been joined successfully"

def testAddingToTheCart(client, creatingAStudent):
    products_response = client.get("/products/")
    assert products_response.status_code == 200
    inventory_of_the_products = products_response.json()

    if len(inventory_of_the_products) > 0 and inventory_of_the_products != None:
        student_registered = creatingAStudent
        chosen_product_id = inventory_of_the_products[0]['id']

        feedback = client.post(f"/students/{student_registered['id']}/cart/", params={"product_id": chosen_product_id})

        assert feedback.status_code == 200
        updated_cart = feedback.json()
        assert len(updated_cart) > 0
        assert updated_cart[-1]['id'] == chosen_product_id

def testCheckingOutOfOrder(client, creatingAGroupOrder, creatingAStudent):
    student_registered = creatingAStudent
    group_order = creatingAGroupOrder
    try:
        joining = client.post(f"/group_orders/{group_order['order_id']}/join/", params={"id_student": student_registered['id']})
        assert joining.status_code == 200

        get_products = client.get("/products/")
        assert get_products.status_code == 200
        inventory_of_product = get_products.json()

        if len(inventory_of_product) > 0 and inventory_of_product != None:
            product_id_being_used = inventory_of_product[0]['id']
            updated_cart = client.post(f"/students/{student_registered['id']}/cart/", params={"product_id": product_id_being_used})
            assert updated_cart.status_code == 200

            checkout_feedback = client.post(f"/students/{student_registered['id']}/checkout/")
            assert checkout_feedback.status_code == 200
            assert 'wallet' in checkout_feedback.json()

            updated_wallet = checkout_feedback.json()['wallet']
            assert updated_wallet < student_registered['wallet']

    except Exception as e:
        assert False, f"Checkout failed: {str(e)}"
