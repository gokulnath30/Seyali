$( "form" ).on( "submit", function( event ) {
    event.preventDefault();
    console.log( $( this ).serialize() );
    $.post('/add_user',$( this ).serialize(),function(res){
      if(res['res'] == 'success'){
        window.location.href = '/';

      }
    })
  });