import unittest
import sysParams
import inheritance


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
        pass


    @label("A Dummy Test --- ")
    def test_dummy(self):
        self.assertEqual(1, 1)

    
    @points(2)
    @label("Test 1: Abstract Class in abstractClass.py --- ")
    def test_abstract_class(self):
        from abstractClass import AbstractSystem
        class IncompleteIdentity(AbstractSystem):
            pass

        with self.assertRaises(TypeError):
            IncompleteIdentity()

    @points(2)
    @label("Test 2: SystemManager Initialization --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_class_constructor_Blue(self):
        import sysidentitymanager
        idManager = sysidentitymanager.SystemManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(idManager.hostID, sysParams.username)
        self.assertEqual(idManager.osID, sysParams.os_id)
        self.assertEqual(idManager._biosID, sysParams.bios_id)

    @points(2)
    @label("Test 2: SystemManager Initialization --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_class_constructor_Green(self):
        import sysidentitymanager
        idManager_cg = sysidentitymanager.SystemManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(idManager_cg.userID, sysParams.hostname)
        self.assertEqual(idManager_cg.osID, sysParams.os_id)
        self.assertEqual(idManager_cg._biosID, sysParams.bios_id)

    @points(2)
    @label("Test 3: Private Attribute --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_private_attribute_Blue(self):
        import sysidentitymanager
        self.idManager = sysidentitymanager.SystemManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        self.idManager._SystemManager__hostID

    @points(2)
    @label("Test 3: Private Attribute --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_private_attribute_Green(self):
        import sysidentitymanager
        self.idManager = sysidentitymanager.SystemManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )
        self.idManager._SystemManager__userID

    @points(2)
    @label("Test 4: Getter --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_property_getter_Blue(self):
        import sysidentitymanager
        self.idManager = sysidentitymanager.SystemManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(self.idManager.hostID, sysParams.username)

    @points(2)
    @label("Test 4: Getter --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_property_getter_Green(self):
        import sysidentitymanager
        self.idManager = sysidentitymanager.SystemManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        self.assertEqual(self.idManager.userID, sysParams.hostname)

    @points(2)
    @label("Test 5: Setter --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_property_setter_Blue(self):
        import sysidentitymanager
        idManager = sysidentitymanager.SystemManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        idManager.hostID = "new_host"
        self.assertEqual(idManager.hostID, "new_host")

    @points(2)
    @label("Test 5: Setter --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_property_setter_Green(self):
        import sysidentitymanager
        self.idManager = sysidentitymanager.SystemManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        self.idManager.userID = "new_user"
        self.assertEqual(self.idManager.userID, "new_user")

    @points(3)
    @label("Test 6: ClassMethod --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_classmethod_Blue(self):
        import sysidentitymanager
        sysidentitymanager.SystemManager.decrement_userID(5)
        self.assertEqual(sysidentitymanager.SystemManager.userID, 95)
        sysidentitymanager.SystemManager.decrement_userID(-5)


    @points(3)
    @label("Test 6: ClassMethod --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_classmethod_Green(self):
        import sysidentitymanager
        sysidentitymanager.SystemManager.increment_hostID(5)
        self.assertEqual(sysidentitymanager.SystemManager.hostID, 5)
        sysidentitymanager.SystemManager.increment_hostID(-5)

    @points(2)
    @label("Test 7: ClassAttribute --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_class_attribute_Blue(self):
        import sysidentitymanager
        idManager = sysidentitymanager.SystemManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        another_identity = sysidentitymanager.SystemManager(
            "another_user", "OS999", "BIOS999"
        )


        sysidentitymanager.SystemManager.userID = 1000
        self.assertEqual(idManager.userID, 1000)
        self.assertEqual(another_identity.userID, 1000)
        sysidentitymanager.SystemManager.userID = 100


    @points(2)
    @label("Test 7: ClassAttribute --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_class_attribute_Green(self):
        import sysidentitymanager
        idManager = sysidentitymanager.SystemManager(
            sysParams.hostname, sysParams.os_id, sysParams.bios_id
        )

        another_identity = sysidentitymanager.SystemManager(
            "another_host", "OS999", "BIOS999"
        )

        sysidentitymanager.SystemManager.hostID = 1000

        self.assertEqual(idManager.hostID, 1000)
        self.assertEqual(another_identity.hostID, 1000)
        sysidentitymanager.SystemManager.hostID = 0

    @points(8)
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    @label("Test 8: Static Method --- ")
    def test_verify_string(self):
        import sysidentitymanager
        self.assertEqual(sysidentitymanager.SystemManager.verify_string("abc"), "Input is a string")
        self.assertEqual(sysidentitymanager.SystemManager.verify_string(10), "Input is not a string")

    
    @points(8)
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    @label("Test 8: Static Method --- ")
    def test_verify_int(self):
        import sysidentitymanager
        self.assertEqual(sysidentitymanager.SystemManager.verify_int("abc"), "Input is not an integer")
        self.assertEqual(sysidentitymanager.SystemManager.verify_int(10), "Input is an integer")

    @points(4)
    @label("Test 9: get_identifiers Method --- ")
    @unittest.skipUnless(sysParams.color == "Blue", "Color is not Blue")
    def test_get_identifiers_Blue(self):
        import sysidentitymanager
        sysidentitymanager.SystemManager.userID = 100
        idManager = sysidentitymanager.SystemManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        identifiers = idManager.get_identifiers()

        expected = {
            "hostID": sysParams.username,
            "userID": 100,
            "osID": sysParams.os_id,
            "biosID": sysParams.bios_id,
        }

        self.assertEqual(identifiers, expected)

    @points(4)
    @label("Test 9: get_identifiers Method --- ")
    @unittest.skipUnless(sysParams.color == "Green", "Color is not Green")
    def test_get_identifiers_Green(self):
        import sysidentitymanager
        sysidentitymanager.SystemManager.hostID = 100
        idManager = sysidentitymanager.SystemManager(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )

        identifiers = idManager.get_identifiers()

        expected = {
            "hostID": 100,
            "userID": sysParams.username,
            "osID": sysParams.os_id,
            "biosID": sysParams.bios_id,
        }

        self.assertEqual(identifiers, expected)

    @points(3)
    @label("Test 10: subclasses in inheritance.py --- ")
    @unittest.skipUnless(sysParams.season == "Winter", "Season is not Winter")
    def test_validate_inheritance_winter(self):
        import sysidentitymanager
        self.assertIsSubclass(
            inheritance.VMClass, sysidentitymanager.SystemManager
        )
        self.assertIsSubclass(
            inheritance.ConClass, sysidentitymanager.SystemManager
        )
        self.assertIsSubclass(
            inheritance.MixClass, (inheritance.VMClass, inheritance.ConClass)
        )

    @points(3)
    @label("Test 10: subclasses in inheritance.py --- ")
    @unittest.skipUnless(sysParams.season == "Summer", "Season is not Summer")
    def test_validate_inheritance_summer(self):
        import sysidentitymanager
        self.assertIsSubclass(
            inheritance.OSClass, sysidentitymanager.SystemManager
        )
        self.assertIsSubclass(
            inheritance.FirmClass, sysidentitymanager.SystemManager
        )
        self.assertIsSubclass(
            inheritance.MixClass, (inheritance.OSClass, inheritance.FirmClass)
        )

    @points(8)
    @label("Test 11: identify_module method output in inheritance.py--- ")
    @unittest.skipUnless(sysParams.season == "Winter" and sysParams.color == "Blue", "Season is not Winter")
    def test_inheritance_method_Winter_Blue(self):
        vmManager = inheritance.VMClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        conManager = inheritance.ConClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        mixManager = inheritance.MixClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        self.assertEqual(vmManager.identify_module(), "VMClass-" + vmManager.hostID)
        self.assertEqual(
            conManager.identify_module(),
            "ConClass-" + conManager.hostID,
        )
        self.assertEqual(
            mixManager.identify_module(), "MixClass-" + mixManager.hostID
        )
    @points(8)
    @label("Test 11: identify_module method output in inheritance.py--- ")
    @unittest.skipUnless(sysParams.season == "Winter" and sysParams.color == "Green", "Season is not Winter")
    def test_inheritance_method_Winter_Green(self):
        vmManager = inheritance.VMClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        conManager = inheritance.ConClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        mixManager = inheritance.MixClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        self.assertEqual(vmManager.identify_module(), "VMClass-" + vmManager.userID)
        self.assertEqual(
            conManager.identify_module(),
            "ConClass-" + conManager.userID,
        )
        self.assertEqual(
            mixManager.identify_module(), "MixClass-" + mixManager.userID
        )
    @points(8)
    @label("Test 11: identify_module method output in inheritance.py--- ")
    @unittest.skipUnless(sysParams.season == "Summer" and sysParams.color == "Blue", "Season is not Summer")
    def test_inheritance_method_Summer_Blue(self):
        osManager = inheritance.OSClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        firmManager = inheritance.FirmClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        mixManager = inheritance.MixClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        self.assertEqual(osManager.identify_module(), "OSClass-" + osManager.hostID)
        self.assertEqual(
            firmManager.identify_module(),
            "FirmClass-" + firmManager.hostID,
        )
        self.assertEqual(
            mixManager.identify_module(), "MixClass-" + mixManager.hostID
        )
    @points(8)
    @label("Test 11: identify_module method output in inheritance.py--- ")
    @unittest.skipUnless(sysParams.season == "Summer" and sysParams.color == "Green", "Season is not Winter")
    def test_inheritance_method_Summer_Green(self):
        osManager = inheritance.OSClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        firmManager = inheritance.FirmClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        mixManager = inheritance.MixClass(
            sysParams.username, sysParams.os_id, sysParams.bios_id
        )
        self.assertEqual(osManager.identify_module(), "OSClass-" + osManager.userID)
        self.assertEqual(
            firmManager.identify_module(),
            "FirmClass-" + firmManager.userID,
        )
        self.assertEqual(
            mixManager.identify_module(), "MixClass-" + mixManager.userID
        )

    @points(2)
    @label("Test 12: instantiation in inheritance.py --- ")
    def test_check_inheritance_instantiation(self):
        self.assertIsInstance(inheritance.hybrid_obj, inheritance.MixClass)

# -------------------------------
# Entry point
# -------------------------------

if __name__ == "__main__":
    unittest.main(testRunner=PointsTestRunner, verbosity=0, exit=False)
