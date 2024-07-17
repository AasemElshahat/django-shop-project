// document.addEventListener("DOMContentLoaded", function () {
//   const writeReviewBtn = document.getElementById("write-review-btn");
//   const reviewFormContainer = document.getElementById("review-form-container");

//   function loadReviewForm(productId) {
//     fetch(`/reviews/product/${productId}/get-review-form/`)
//       .then((response) => response.text())
//       .then((html) => {
//         reviewFormContainer.innerHTML = html;
//         initStarRating();
//       });
//   }

//   if (writeReviewBtn) {
//     writeReviewBtn.addEventListener("click", function () {
//       const productId = this.dataset.productId;
//       loadReviewForm(productId);
//     });
//   }

//   // Add event delegation for edit buttons
//   document.addEventListener("click", function (e) {
//     if (e.target && e.target.classList.contains("edit-review-btn")) {
//       const productId = e.target.dataset.productId;
//       loadReviewForm(productId);
//     }
//   });

//   function initStarRating() {
//     const starRatingInput = document.querySelector(".star-rating-input");
//     const ratingField = document.getElementById("id_rating");

//     if (starRatingInput && ratingField) {
//       const stars = starRatingInput.querySelectorAll(".star");

//       stars.forEach((star) => {
//         star.addEventListener("mouseover", function () {
//           const rating = this.dataset.rating;
//           highlightStars(rating);
//         });

//         star.addEventListener("mouseout", function () {
//           const currentRating = ratingField.value;
//           highlightStars(currentRating);
//         });

//         star.addEventListener("click", function () {
//           const rating = this.dataset.rating;
//           ratingField.value = rating;
//           highlightStars(rating);
//         });
//       });

//       function highlightStars(rating) {
//         stars.forEach((star) => {
//           if (star.dataset.rating <= rating) {
//             star.classList.add("filled");
//           } else {
//             star.classList.remove("filled");
//           }
//         });
//       }

//       // Initialize stars based on the current rating
//       highlightStars(ratingField.value);
//     }
//   }
// });
