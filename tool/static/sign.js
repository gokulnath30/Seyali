$( "form" ).on( "submit", function( event ) {
    event.preventDefault();
    console.log( $( this ).serialize() );
    $.post('/add_user',$( this ).serialize(),function(res){
      console.log(res)
    })
  });