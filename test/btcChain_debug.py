inset('../btcrelay.py')  # btcrelay is still the contract under test

# test only method required by some tests
def testingonlySetHeaviest(blockHash):
    self.heaviestBlock = blockHash


#
# macro wrappers (since only functions are testable)
#

def funcSaveAncestors(blockHash, hashPrevBlock):
    m_saveAncestors(blockHash, hashPrevBlock)

#
# end of macro wrappers
#
