class X { static void tower ( int n , char sourcePole , char destinationPole , char auxiliaryPole ) { tower ( n - 1 , sourcePole , auxiliaryPole , destinationPole ) ; System . out . printf ( " Move ▁ the ▁ disk ▁ % d ▁ from ▁ % c ▁ to ▁ % c \n " , n , sourcePole , destinationPole ) ; tower ( n - 1 , auxiliaryPole , destinationPole , sourcePole ) ; }
 }