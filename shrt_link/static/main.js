$( document ).ready(function() {
    console.log( "ready!" );

    $(".counter").click(function( ){
      count =  parseInt($("#clickCount"+this.id).text()) + 1;
      $("#clickCount"+this.id).text(count);
    })
});
