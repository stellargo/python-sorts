import unittest
import selectionSort
import bubbleSort
import bubbleSortR
import insertionSort
import insertionSortR
import mergeSort

class Test( unittest.TestCase ):
	def testSelectionSort( self ):
		A = [5,1,3,0,10]
		selectionSort.selectionSort( A )
		B = [0,1,3,5,10]
		if (A!=B):
			self.fail( "selectionSort method fails." )

	def testBubbleSort( self ):
		A = [5,1,3,0,10]
		bubbleSort.bubbleSort( A )
		B = [0,1,3,5,10]
		if (A!=B):
			self.fail( "bubbleSort method fails." )

	def testBubbleSortR( self ):
		A = [5,1,3,0,10]
		bubbleSortR.bubbleSortR( A , len(A))
		B = [0,1,3,5,10]
		if (A!=B):
			self.fail( "bubbleSortR method fails." )

	def testInsertionSort(self):
		A = [5,1,3,0,10]
		insertionSort.insertionSort( A )
		B = [0,1,3,5,10]
		if (A!=B):
			self.fail("insertionSort method fails.")

	def testInsertionSortR(self):
		A = [5,1,3,0,10]
		insertionSortR.insertionSortR( A , 0 )
		B = [0,1,3,5,10]
		if (A!=B):
			self.fail("insertionSortR method fails.")

	def testMergeSort( self ):
		A = [5,1,3,0,10]
		new = mergeSort.mergeSort( A )
		B = [0,1,3,5,10]
		if (new!=B):
			self.fail( "mergeSort method fails." )

	def testQuickSort( self ):
		A = [5,1,3,0,10]
		new = quickSort.quickSort( A )
		B = [0,1,3,5,10]
		if (new!=B):
			self.fail( "quickSort method fails." )

		