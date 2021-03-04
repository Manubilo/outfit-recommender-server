from app.data_access import transactional


class MoodsController:

    @transactional
    def create():
        print("create")

    @transactional
    def list():
        print("list")

    @transactional
    def get_one():
        print("list")

    @transactional
    def edit():
        print("list")

    @transactional
    def delete():
        print("list")
