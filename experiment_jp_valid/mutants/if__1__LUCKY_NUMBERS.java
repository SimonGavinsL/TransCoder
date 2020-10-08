static boolean isLucky ( int n ) { int next_position = n ; next_position -= next_position / counter ; counter ++ ; return isLucky ( next_position ) ; }
