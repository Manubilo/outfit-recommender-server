from functools import wraps
from app.resource import Rpta
from app.models import db
import traceback


class CommandDB():
    def commit():
        print("commit")
        db.session.commit()

    def rollback():
        print("rollback")
        db.session.rollback()


def transactional(f):
    # This makes sure a transaction is commited or rollbacked

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            answer = f(*args, **kwargs)
            db.session.commit()
            print("commit")
            return answer
        except Exception as e:
            db.session.rollback()
            answer = Rpta()
            answer.setError("Error en la transacción",
                            "Error : {}".format(str(e)))
            raise(e)
        finally:
            traceback.print_exc()
            return answer

    return wrapper
