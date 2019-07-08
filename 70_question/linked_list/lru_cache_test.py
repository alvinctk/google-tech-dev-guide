import lru_cache as program
import unittest


letterMaps = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
}

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def testLruOfSize(size, testContext):
    # Instantiate cache and insert first key.
    lru = program.LRUCache(size)
    testContext.assertEqual(lru.getValueFromKey("a"), None)
    lru.insertKeyValuePair("a", 99)
    testContext.assertEqual(lru.getMostRecentKey(), "a")
    testContext.assertEqual(lru.getValueFromKey("a"), 99)
    # Add existing key when cache isn't full.
    lru.insertKeyValuePair("a", 0)
    testContext.assertEqual(lru.getMostRecentKey(), "a")
    testContext.assertEqual(lru.getValueFromKey("a"), 0)
    # Add keys until cache reaches maximum capacity.
    for i in range(1, size):
        mostRecentLetter = letters[i - 1]
        testContext.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
        # Test key retrieval when cache isn't full.
        for j in range(0, i):
            letter = letters[j]
            testContext.assertEqual(lru.getValueFromKey(letter), letterMaps[letter])
            testContext.assertEqual(lru.getMostRecentKey(), letter)
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), None)
        lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
        testContext.assertEqual(lru.getMostRecentKey(), currentLetter)
        testContext.assertEqual(lru.getValueFromKey(currentLetter), letterMaps[currentLetter])
    # Add keys now that cache is at maximum capacity.
    for i in range(size, len(letters)):
        mostRecentLetter = letters[i - 1]
        testContext.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
        # Test key retrieval when cache is full.
        for j in range(i - size, i):
            letter = letters[j]
            testContext.assertEqual(lru.getValueFromKey(letter), letterMaps[letter])
            testContext.assertEqual(lru.getMostRecentKey(), letter)
        leastRecentLetter = letters[i - size]
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), None)
        lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
        testContext.assertEqual(lru.getMostRecentKey(), currentLetter)
        testContext.assertEqual(lru.getValueFromKey(currentLetter), letterMaps[currentLetter])
        #lru.display()
        testContext.assertEqual(lru.getValueFromKey(leastRecentLetter), None)
    # Add existing keys when cache is full.
    for i in range(len(letters) - size, len(letters)):
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), letterMaps[currentLetter])
        lru.insertKeyValuePair(currentLetter, (letterMaps[currentLetter] + 1) * 100)
        testContext.assertEqual(lru.getValueFromKey(currentLetter), (letterMaps[currentLetter] + 1) * 100)


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        testLruOfSize(1, self)

    def test_case_2(self):
        testLruOfSize(2, self)

    def test_case_3(self):
        testLruOfSize(3, self)

    def test_case_4(self):
        testLruOfSize(4, self)

    def test_case_5(self):
        testLruOfSize(5, self)

    def test_case_6(self):
        testLruOfSize(6, self)

    def test_case_7(self):
        testLruOfSize(7, self)

    def test_case_8(self):
        testLruOfSize(8, self)

    def test_case_9(self):
        testLruOfSize(9, self)

    def test_case_10(self):
        testLruOfSize(10, self)


if __name__ == "__main__":
	unittest.main()

