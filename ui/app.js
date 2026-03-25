const answers = document.querySelectorAll(".answer");
const feedback = document.getElementById("feedback");
const ladderItems = document.querySelectorAll(".ladder li");
const currentPrize = document.getElementById("current-prize");

let currentStep = 1;

if (answers.length > 0 && feedback) {
  answers.forEach(button => {
    button.addEventListener("click", () => {
      answers.forEach(btn => btn.classList.remove("selected"));
      button.classList.add("selected");

      const isCorrect = button.dataset.correct === "true";

      if (isCorrect) {
        feedback.textContent = "Correct answer.";
        feedback.style.color = "green";

        if (currentStep < 5) {
          currentStep++;
        }

        ladderItems.forEach(item => item.classList.remove("active"));

        const nextActive = document.querySelector(`.ladder li[data-step="${currentStep}"]`);
        if (nextActive) {
          nextActive.classList.add("active");
          currentPrize.textContent = nextActive.textContent;
        }
      } else {
        feedback.textContent = "Wrong answer.";
        feedback.style.color = "red";
      }
    });
  });
}