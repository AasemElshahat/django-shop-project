$(document).on("click", ".img-thumbnail", function () {
  var src = $(this).attr("src");
  var modal = $("#imageModal");
  modal.find(".carousel-item").each(function () {
    if ($(this).find("img").attr("src") == src) {
      $(this).addClass("active");
    } else {
      $(this).removeClass("active");
    }
  });
  modal.modal("show");
});
