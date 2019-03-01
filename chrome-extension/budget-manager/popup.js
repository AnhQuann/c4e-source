$(document).ready(function(){
  if (!localStorage.getItem("total")) {
    localStorage.setItem("total", 0);
  }
  updateTotal();
  // $("#total_spending").text("Alo");
  $("#more_spendng").keyup(function(e) {
    if(e.keyCode === 13) {
      var more_spendng = parseInt($("#more_spendng").val());
      $("#more_spendng").val("0");
      var total = parseInt(localStorage.getItem("total")) + more_spendng;
      localStorage.setItem("total", total);
      updateTotal();
    }
  });

  $("#reset").click(function(e){
    localStorage.setItem("total", 0);
    updateTotal();
  });
});


function updateTotal() {
  var total = parseInt(localStorage.getItem("total"));
  $("#total_spending").text(total.toString());
}
