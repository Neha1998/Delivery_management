import uuid


class Package(object):
    packages = []
    type_status_map = {
        "forward": ("ordered", "dropped", "delivered"),
        "reverse": ("ordered", "dropped", "delivered")
    }

    def __init__(self, id, user, type="forward"):
        self.id = id
        self.status = "ordered"
        self.type = type
        self.user = user
        self.save()

    def save(self):
        self.packages.append(self)


class Locker(object):
    lockers = []
    status = ("available", "assigned", "occupied")

    def __init__(self, id):
        self.id = id
        self.status = "available"
        self.active = 1
        self.otp = ""
        self.package = ""
        self.save()

    def save(self):
        self.lockers.append(self)


class Customer(object):

    customers = []
    def __init__(self, id, address="abc"):
        self.id = id
        self.address = address
        self.save()

    def save(self):
        self.customers.append(self)


class FE(object):

    FEs = []

    def __init__(self, id, name = 'a',email='b'):
        self.id = id
        self.name =name
        self.email = email
        self.save()

    def save(self):
        self.FEs.append(self)
