$.get(
    "https://ld-score.herokuapp.com/score",
    {},
    function(data) {
       //alert('page content: ' + data.success);
       console.log(data);
    }
);
