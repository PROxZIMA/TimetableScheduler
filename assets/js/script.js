$(function () {
  $("#genButton").on('click', function () {
    setInterval(function () {
      $.ajax({
        method: "GET",
        url: "/api/genNum/",
        success: function (data) {
          console.log(data);
          $('.loaderClassValue').contents()[0].textContent = data.genNum;
        },
        error: function (data) {
          console.log("error")
        }
      });
    }, 1000);
  });
});