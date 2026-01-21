import unittest
import sysParams
import sysidentitymanager
import inheritance
import exceptionFunction
import myData

import abstractsysidentity

# -------------------------------
# Decorators
# -------------------------------


def points(value):
    """Assign points to a test."""

    def decorator(func):
        func.points = value
        return func

    return decorator


def label(text):
    """Human-readable test label."""

    def decorator(func):
        func.label = text
        return func

    return decorator


# -------------------------------
# Custom TestResult
# -------------------------------


class PointsTestResult(unittest.TextTestResult):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_points = 0.0
        self.earned_points = 0.0

    def startTest(self, test):
        self.total_points += self._get_points(test)
        # IMPORTANT: do NOT call super().startTest(test)
        # It triggers default output
        self.testsRun += 1

    def addSuccess(self, test):
        self.earned_points += self._get_points(test)
        self.stream.writeln(f"{self._get_label(test)} Passed")

    def addFailure(self, test, err):
        self.stream.writeln(f"{self._get_label(test)} Failed")
        self.failures.append((test, err))

    def printErrors(self):
        """Suppress default traceback printing."""
        pass

    def addError(self, test, err):
        self.stream.writeln(f"{self._get_label(test)} Error")
        self.errors.append((test, err))

    def printPointsSummary(self):
        self.stream.writeln(f"\nPoints earned: {self.earned_points}/ 40")

    def _get_points(self, test):
        method = getattr(test, test._testMethodName)
        return float(getattr(method, "points", 0))

    def _get_label(self, test):
        method = getattr(test, test._testMethodName)
        return getattr(method, "label", test._testMethodName)


# -------------------------------
# Custom TestRunner
# -------------------------------


class PointsTestRunner(unittest.TextTestRunner):
    resultclass = PointsTestResult

    def run(self, test):
        result = super().run(test)
        result.printPointsSummary()
        return result


# -------------------------------
# Test Case
# -------------------------------


class MyTestCase(unittest.TestCase):

    def setUp(self):
        color = sysParams.color
        shape = sysParams.shape
        season = sysParams.season

    @label("A Dummy Test --- ")
    def test_dummy(self):
        self.assertEqual(1, 1)

    @points(1.5)
    @label("Test 1: Access student_name, father_name and reg_no in sysParams.py --- ")
    def test_sysParams_import(self):
        self.assertEqual(myData.student_name, sysParams.username)
        self.assertEqual(myData.student_fatherName, sysParams.hostname)
        self.assertEqual(myData.student_registration_number, sysParams.reg_id)

    @points(2)
    @label("Test 2: Abstract Class in abstractsysidentity.py --- ")
    def test_abstract_class(self):
        class IncompleteIdentity(abstractsysidentity.AbstractSystemIdentity):
            pass

        with self.assertRaises(TypeError):
            IncompleteIdentity()

    @points(2)
    @label("Test 3: SystemIdentityManager Initialization --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_class_constructor_Blue(self):
        idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(idManager.username, sysParams.username)
        self.assertEqual(idManager.os_serial, sysParams.os_id)
        self.assertEqual(idManager.bios_serial, sysParams.bios_id)

    @points(2)
    @label("Test 3: SystemIdentityManager Initialization --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_class_constructor_Green(self):
        idManager_cg = sysidentitymanager.SystemIdentityManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(idManager_cg.hostname, sysParams.hostname)
        self.assertEqual(idManager_cg.os_serial, sysParams.os_id)
        self.assertEqual(idManager_cg.bios_serial, sysParams.bios_id)

    @points(2)
    @label("Test 4: Private Attribute --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_private_attribute_Blue(self):
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        self.idManager._SystemIdentityManager__username

    @points(2)
    @label("Test 4: Private Attribute --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_private_attribute_Green(self):
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )
        self.idManager._SystemIdentityManager__hostname

    @points(2)
    @label("Test 5: Getter --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_property_getter_Blue(self):
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(self.idManager.username, sysParams.username)

    @points(2)
    @label("Test 5: Getter --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_property_getter_Green(self):
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(self.idManager.hostname, sysParams.hostname)

    @points(2)
    @label("Test 6: Setter --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_property_setter_Blue(self):
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        self.idManager.username = "new_user"
        self.assertEqual(self.idManager.username, "new_user")

    @points(2)
    @label("Test 6: Setter --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_property_setter_Green(self):
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        self.idManager.hostname = "new_host"
        self.assertEqual(self.idManager.hostname, "new_host")

    @points(2)
    @label("Test 7: ClassMethod --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_classmethod_Blue(self):
        sysidentitymanager.SystemIdentityManager.set_hostname("test_host")
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(self.idManager.hostname, "test_host")

    @points(2)
    @label("Test 7: ClassMethod --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_classmethod_Green(self):
        sysidentitymanager.SystemIdentityManager.set_username("test_user")
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(self.idManager.username, "test_user")

    @points(2)
    @label("Test 8: ClassAttribute --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_class_attribute_Blue(self):
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        another_identity = sysidentitymanager.SystemIdentityManager(
            name="another_user", os_serial="OS999", bios_serial="BIOS999"
        )

        sysidentitymanager.SystemIdentityManager.set_hostname("shared_host")

        self.assertEqual(self.idManager.hostname, "shared_host")
        self.assertEqual(another_identity.hostname, "shared_host")

    @points(2)
    @label("Test 8: ClassAttribute --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_class_attribute_Green(self):
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        another_identity = sysidentitymanager.SystemIdentityManager(
            name="another_host", os_serial="OS999", bios_serial="BIOS999"
        )

        sysidentitymanager.SystemIdentityManager.set_username("shared_user")

        self.assertEqual(self.idManager.username, "shared_user")
        self.assertEqual(another_identity.username, "shared_user")

    @points(2)
    @label("Test 9: Static Method --- ")
    def test_confirm_user_age_above_18(self):
        self.assertTrue(sysidentitymanager.SystemIdentityManager.confirm_user_age(19))

    @points(2.5)
    @label("Test 10: return_identifiers Method --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_return_identifiers_Blue(self):
        sysidentitymanager.SystemIdentityManager.set_hostname("test_host")
        self.idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        identifiers = self.idManager.return_identifiers()

        expected = {
            "HostName": "test_host",
            "UserName": sysParams.username,
            "OS_Serial": sysParams.os_id,
            "BIOS_Serial": sysParams.bios_id,
        }

        self.assertEqual(identifiers, expected)

    @points(2.5)
    @label("Test 10: return_identifiers Method --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_return_identifiers_Green(self):
        sysidentitymanager.SystemIdentityManager.set_username("test_user")
        idManager = sysidentitymanager.SystemIdentityManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        identifiers = idManager.return_identifiers()
        expected = {
            "HostName": sysParams.hostname,
            "UserName": "test_user",
            "OS_Serial": sysParams.os_id,
            "BIOS_Serial": sysParams.bios_id,
        }

        self.assertEqual(identifiers, expected)

    @points(2)
    @label("Test 11: subclasses in inheritance.py --- ")
    @unittest.skipUnless(sysParams.season == "Winter", "Season is not Winter")
    def test_11_validate_inheritance_winter(self):
        self.assertIsSubclass(
            inheritance.OSModule, sysidentitymanager.SystemIdentityManager
        )
        self.assertIsSubclass(
            inheritance.HardwareModule, sysidentitymanager.SystemIdentityManager
        )
        self.assertIsSubclass(
            inheritance.HybridModule, (inheritance.OSModule, inheritance.HardwareModule)
        )

    @points(2)
    @label("Test 11: subclasses in inheritance.py --- ")
    @unittest.skipUnless(sysParams.season == "Summer", "Season is not Summer")
    def test_11_validate_inheritance_summer(self):
        self.assertIsSubclass(
            inheritance.VMModule, sysidentitymanager.SystemIdentityManager
        )
        self.assertIsSubclass(
            inheritance.FirmwareModule, sysidentitymanager.SystemIdentityManager
        )
        self.assertIsSubclass(
            inheritance.HybridModule, (inheritance.VMModule, inheritance.FirmwareModule)
        )

    @points(5)
    @label("Test 12: identify_module method output in inheritance.py--- ")
    @unittest.skipUnless(sysParams.season == "Winter", "Season is not Winter")
    def test_inheritance_method_Winter(self):
        osManager = inheritance.OSModule(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        hardwareManager = inheritance.HardwareModule(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        hybridManager = inheritance.HybridModule(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        self.assertEqual(osManager.identify_module(), "OSModule-" + osManager.os_serial)
        self.assertEqual(
            hardwareManager.identify_module(),
            "Hardware Module-" + hardwareManager.os_serial,
        )
        self.assertEqual(
            hybridManager.identify_module(), "HybridModule-" + hybridManager.os_serial
        )

    @points(5)
    @label("Test 12: identify_module method in inheritance.py--- ")
    @unittest.skipUnless(sysParams.season == "Summer", "Season is not Summer")
    def test_inheritance_method_Summer(self):
        vmManager = inheritance.VMModule(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        firmwareManager = inheritance.FirmwareModule(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        hybridManager = inheritance.HybridModule(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        self.assertEqual(vmManager.identify_module(), "VMModule-" + vmManager.os_serial)
        self.assertEqual(
            firmwareManager.identify_module(),
            "Firmware Module-" + firmwareManager.os_serial,
        )
        self.assertEqual(
            hybridManager.identify_module(), "HybridModule-" + hybridManager.os_serial
        )

    @points(2)
    @label("Test 13: instantiation in inheritance.py --- ")
    def test_task4c_check_instance(self):
        self.assertIsInstance(inheritance.hybrid_obj, inheritance.HybridModule)

    @points(1)
    @label("Task 14: validate mro --- ")
    def test_task4d_validate_mro(self):
        self.assertEqual(inheritance.mro_variable, inheritance.HybridModule.mro())

    # --------------------------------------------------------------------------------
    # Tests No. 15, 16A and 16B are related to exceptionFunction.                   #
    # Test 15 checks invalid input response and 16 checks valid input response.     #
    # Test 16A is for Square and 16B is for trinagle.                               #
    # ---------------------------------------------------------------------------------

    @points(5)
    @label("Test 15: invalid input for exceptionFunction--- ")
    def test_task5a_invalid_string(self):
        result = exceptionFunction.exception_function("15")
        self.assertEqual(result, "Not Possible")

    @points(5)
    @label("Test 16: valid input exceptionFunction  --- ")
    @unittest.skipUnless(sysParams.shape == "Square", "Shape is not Square")
    def test_task16a_square(self):
        result = exceptionFunction.exception_function(15)
        self.assertEqual(result, "Possible")

    @points(5)
    @label("Test 16: valid input exceptionFunction  --- ")
    @unittest.skipUnless(sysParams.shape == "Triangle", "Shape is not Triangle")
    def test_task16b_triangle(self):
        result = exceptionFunction.exception_function("OS_Serial")
        self.assertEqual(result, "Possible")


# -------------------------------
# Entry point
# -------------------------------

if __name__ == "__main__":
    unittest.main(testRunner=PointsTestRunner, verbosity=0, exit=False)
