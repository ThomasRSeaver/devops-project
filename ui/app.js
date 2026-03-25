const answers = document.querySelectorAll(".answer");
const feedback = document.getElementById("feedback");

if (answers.length > 0 && feedback) {
  answers.forEach(button => {
    button.addEventListener("click", () => {
      answers.forEach(btn => btn.classList.remove("selected"));

      button.classList.add("selected");

      const isCorrect = button.dataset.correct === "true";

      if (isCorrect) {
        feedback.textContent = "Correct answer.";
        feedback.style.color = "green";
      } else {
        feedback.textContent = "Wrong answer.";
        feedback.style.color = "red";
      }
    });
  });
}