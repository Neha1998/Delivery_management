from models import Package, Customer, FE, Locker
from services import LockerService, NotificationService

if __name__ == '__main__':
    c1, c2 = Customer("cust1"), Customer("cust2")
    FE1, FE2 = FE("FE1"), FE("FE2")
    package = Package("package1", c1)
    l1, l2 = Locker("locker1"), Locker("locker2")

    assigned_locker, otp = LockerService.assign(FE1, c1, package)

    # FE has arrived and dropped the package
    status = LockerService.drop(assigned_locker, package, otp)

    if status:
        NotificationService.notify(c1, assigned_locker)

    # when package has been picked up
    status = LockerService.unassign(assigned_locker, otp)







