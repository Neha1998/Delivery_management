import math
from random import random

from models import Locker


class LockerAssignmentStrategy1(object):

    def assign(self, requester, end_user, package, **kwargs):
        """
         assign a otp to that locker
        return locker id, otp
        :return:
        """

        assigned_locker = None
        for locker in Locker.lockers:
            if locker.active and locker.status == "available":
                assigned_locker = locker
                break
        if not assigned_locker:
            print("no locker available. ")
            return

        otp = OTPService().generate()

        assigned_locker.otp = otp

        print(f"{requester.id} is assigned a locker {assigned_locker.id}, use otp = {otp} "
              f"to drop the package {package.id}.")


class LockerService(object):

    def assign(self, assignment_strategy=LockerAssignmentStrategy1, **kwargs):
        """
         assign a otp to that locker
        return locker id, otp
        :return:
        """
        assignment_strategy.assign(**kwargs)

    def drop(self, locker, package, otp):
        """
        make the locker occupied,
         change the package status to dropped,

        :return:
        """
        is_valid = OTPService().validate(locker, otp)
        if not is_valid:
            print(" Invalid OTP ")
            return False

        locker.package = package
        package.status = "dropped"
        locker.status = "occupied"
        print(f"{package.id} have been dropped")

    def unassign(self, locker, otp):
        """
        make the locker status available
        change the package status to delivered
        set otp field ""
        :return:
        """
        is_valid = OTPService().validate(locker, otp)
        if not is_valid:
            print("Invalid OTP")
            return False

        locker.package.status = "delivered"
        locker.status = "available"
        locker.otp = ""

        return True


class OTPService(object):

    def generate(self, len=6):
        """
        random(len)
        assign otp to that locker.
        :return:
        """
        otp = "829898"
        return otp


    def validate(self, locker, otp):
        """
        chceck if otp matches the locker's otp
        :param locker_id:
        :param otp:
        :return: Bool
        """
        return otp == locker.otp


class NotificationService(object):

    def notify(self, user, locker):
        print(f"Hey {user.id}, Please pick up the package from Locker - {locker.id}, "
              f"using otp- {locker.otp}")

