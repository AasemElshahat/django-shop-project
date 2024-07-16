// // Reviews
// document.addEventListener("DOMContentLoaded", function () {
//   console.log("DOM fully loaded and parsed");

//   const addReviewButton = document.getElementById("add-review");
//   if (addReviewButton) {
//     console.log("Add review button found");
//     addReviewButton.addEventListener("click", function (event) {
//       console.log("Add review button clicked");
//       event.preventDefault();
//       fetchReviewForm("{% url 'review-create-or-edit' product.id %}");
//     });
//   } else {
//     console.error("Add review button not found");
//   }

//   document.querySelectorAll(".edit-review").forEach(function (button) {
//     console.log("Edit review button found");
//     button.addEventListener("click", function (event) {
//       console.log("Edit review button clicked");
//       event.preventDefault();
//       const reviewId = this.getAttribute("data-review-id");
//       fetchReviewForm(
//         "{% url 'review-create-or-edit' product.id %}".replace("0", reviewId)
//       );
//     });
//   });

//   function fetchReviewForm(url) {
//     console.log("Fetching review form from:", url);
//     fetch(url, {
//       headers: {
//         "X-Requested-With": "XMLHttpRequest",
//       },
//     })
//       .then((response) => {
//         console.log("Response status:", response.status);
//         return response.json();
//       })
//       .then((data) => {
//         console.log("Received data:", data);
//         document.getElementById("review-form-container").innerHTML = data.form;
//         attachFormSubmit();
//         attachStarRating();
//       })
//       .catch((error) => console.error("Error fetching form:", error));
//   }

//   function attachFormSubmit() {
//     const form = document.querySelector("#review-form-container form");
//     form.addEventListener("submit", function (event) {
//       event.preventDefault();
//       fetch(form.action, {
//         method: form.method,
//         body: new FormData(form),
//         headers: {
//           "X-Requested-With": "XMLHttpRequest",
//         },
//       })
//         .then((response) => response.json())
//         .then((data) => {
//           if (data.success) {
//             location.reload();
//           } else {
//             document.getElementById("review-form-container").innerHTML =
//               data.form;
//             attachFormSubmit();
//             attachStarRating();
//           }
//         })
//         .catch((error) => console.error("Error submitting form:", error));
//     });
//   }

//   function attachStarRating() {
//     const starContainer = document.querySelector(
//       "#review-form-container .star-rating"
//     );
//     const ratingInput = document.querySelector(
//       "#review-form-container input[name='rating']"
//     );

//     starContainer.addEventListener("mouseover", function (e) {
//       if (e.target.classList.contains("star")) {
//         const rating = e.target.getAttribute("data-rating");
//         highlightStars(rating);
//       }
//     });

//     starContainer.addEventListener("mouseout", function () {
//       highlightStars(ratingInput.value);
//     });

//     starContainer.addEventListener("click", function (e) {
//       if (e.target.classList.contains("star")) {
//         const rating = e.target.getAttribute("data-rating");
//         ratingInput.value = rating;
//         highlightStars(rating);
//       }
//     });

//     function highlightStars(rating) {
//       starContainer.querySelectorAll(".star").forEach((star, index) => {
//         star.classList.toggle("filled", index < rating);
//       });
//     }
//   }
// });
