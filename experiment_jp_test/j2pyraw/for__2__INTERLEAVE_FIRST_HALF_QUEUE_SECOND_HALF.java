class X { static void interLeaveQueue ( Queue < Integer > q ) { if ( q . size ( ) % 2 != 0 ) System . out . println ( " Input ▁ even ▁ number ▁ of ▁ integers . " ) ; Stack < Integer > s = new Stack < > ( ) ; int halfSize = q . size ( ) / 2 ; while ( ! s . empty ( ) ) { q . add ( s . peek ( ) ) ; s . pop ( ) ; } while ( ! s . empty ( ) ) { q . add ( s . peek ( ) ) ; s . pop ( ) ; q . add ( q . peek ( ) ) ; q . poll ( ) ; } }
 }