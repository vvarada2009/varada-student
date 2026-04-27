---
layout: opencs
title: IP & Ethics Review
description: AP CSP legal and ethical computing review
permalink: /student/ip-ethics-review/
---

# IP & Ethics Review

<style>
  .ip-wrap {
    max-width: 920px;
    margin: 1rem auto 0;
    padding: 0.25rem;
  }

  .ip-intro {
    border: 1px solid #d9e2ec;
    border-left: 5px solid #2f6f9f;
    border-radius: 10px;
    background: #f8fbff;
    padding: 0.8rem 1rem;
    margin-bottom: 0.9rem;
    color: #243b53;
  }

  .ip-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.85rem;
  }

  .ip-panel {
    background: #ffffff;
    border: 1px solid #d9e2ec;
    border-radius: 10px;
    padding: 0.95rem;
  }

  .ip-panel h3 {
    margin: 0 0 0.5rem;
    color: #102a43;
    font-size: 1.03rem;
    line-height: 1.3;
  }

  .ip-panel ul {
    margin: 0;
    padding-left: 1.15rem;
    color: #243b53;
  }

  .ip-panel li {
    margin-bottom: 0.4rem;
  }

  .concerns-bottom {
    margin-top: 0.9rem;
    background: #000000;
    color: #ffffff;
    border: 1px solid #000000;
  }

  .concerns-bottom h3 {
    color: #ffffff;
  }

  .concerns-bottom ul {
    color: #ffffff;
  }

  @media (max-width: 640px) {
    .ip-grid {
      grid-template-columns: 1fr;
    }

    .ip-panel {
      padding: 0.8rem;
    }
  }
</style>

<div class="ip-wrap">
  <div class="ip-grid">
    <section class="ip-panel">
      <h3>Intellectual Property (IP)</h3>
      <ul>
        <li>A work or invention that is the result of creativity to which one has rights.</li>
        <li>Can be saved on the computer, making it faster and easier to access and distribute.</li>
        <li>Raises concerns about ownership and whether someone is allowed to use someone else's creations.</li>
      </ul>
    </section>

    <section class="ip-panel">
      <h3>Copyright</h3>
      <ul>
        <li>Protects IP and prevents anyone from using it unless they have permission.</li>
      </ul>
    </section>

    <section class="ip-panel">
      <h3>Legal Ways to Use Materials Created by Someone Else</h3>
      <ul>
        <li><strong>Creative Commons</strong>: Provides free licenses that allow creators to specify how others may use their creation and clearly tells users what to do and not do with the IP.</li>
        <li><strong>Open Source</strong>: Programs that are freely available for anyone to use and can be redistributed or modified by others.</li>
        <li><strong>Open Access</strong>: Online research output free of restrictions on access and many restrictions on use.</li>
      </ul>
    </section>

    <section class="ip-panel">
      <h3>Plagiarism</h3>
      <ul>
        <li>Using work that is not one's own and presenting it as one's own.</li>
      </ul>
    </section>

  </div>

  <section class="ip-panel concerns-bottom">
    <h3>Legal and Ethical Concerns</h3>
    <ul>
      <li>Broad access to digital information has been made easier through technology.</li>
      <li>Open source programs may be created with good intentions (free, modifiable) but can be used to harm others.</li>
      <li>Software that allows downloads and access, plus devices that collect and analyze data, create concerns about monitoring individual activities.</li>
      <li>Software including algorithms could have built-in bias.</li>
      <li><strong>Digital Divide</strong>: unequal distribution of access to technology. Not everyone has equal access to or understanding of how to use the internet and technologies, and access to free resources does not mean equal access for everyone.</li>
    </ul>
  </section>
</div>

---

## Quick Check: 5-Question MC Progression

<div id="ip-ethics-quiz" style="max-width: 760px; margin: 1.5rem auto; border: 1px solid #d9e2ec; border-radius: 14px; padding: 1rem; background: #f8fbff; box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);">
  <div style="display:flex; justify-content:space-between; align-items:center; gap:0.75rem; margin-bottom:0.75rem;">
    <h3 style="margin:0; color:#102a43;">IP & Ethics Checkpoint</h3>
    <span id="quiz-step" style="font-size:0.92rem; color:#486581;">Question 1 of 5</span>
  </div>

  <div style="height:10px; background:#d9e2ec; border-radius:999px; overflow:hidden; margin-bottom:1rem;">
    <div id="quiz-progress" style="height:100%; width:20%; background:linear-gradient(90deg, #2f855a, #38a169); transition:width 0.25s ease;"></div>
  </div>

  <p id="quiz-question" style="font-weight:600; color:#243b53; margin-bottom:0.8rem;"></p>
  <div id="quiz-options" style="display:grid; gap:0.6rem;"></div>

  <div style="display:flex; justify-content:space-between; align-items:center; gap:0.75rem; margin-top:1rem;">
    <p id="quiz-feedback" style="margin:0; color:#334e68; min-height:1.4rem;"></p>
    <button id="quiz-next" type="button" style="border:none; background:#334e68; color:white; padding:0.55rem 0.9rem; border-radius:8px; cursor:pointer;" disabled>Next</button>
  </div>

  <div id="quiz-result" style="display:none; margin-top:1rem; padding:0.9rem; border-radius:10px; background:#e6fffa; color:#014d40; font-weight:600;"></div>
</div>

<script>
  (function () {
    const questions = [
      {
        q: "What does copyright primarily do?",
        options: [
          "Makes all work free to copy",
          "Protects intellectual property from unauthorized use",
          "Only applies to physical books",
          "Removes the need for attribution"
        ],
        answer: 1
      },
      {
        q: "Which option is a legal way to use someone else's creative work?",
        options: [
          "Copying it without credit",
          "Using a Creative Commons licensed version under its terms",
          "Claiming it as your own",
          "Ignoring license restrictions"
        ],
        answer: 1
      },
      {
        q: "Plagiarism is best described as:",
        options: [
          "Learning from examples",
          "Reusing your own old work",
          "Presenting someone else's work as your own",
          "Asking permission before use"
        ],
        answer: 2
      },
      {
        q: "What is one ethical concern with algorithms?",
        options: [
          "They always remove bias",
          "They can include built-in bias",
          "They cannot make decisions",
          "They only work offline"
        ],
        answer: 1
      },
      {
        q: "The digital divide refers to:",
        options: [
          "A split between hardware brands",
          "Unequal access to technology and internet resources",
          "Different coding languages",
          "A gap between legal and illegal downloads"
        ],
        answer: 1
      }
    ];

    const questionEl = document.getElementById("quiz-question");
    const optionsEl = document.getElementById("quiz-options");
    const feedbackEl = document.getElementById("quiz-feedback");
    const resultEl = document.getElementById("quiz-result");
    const nextBtn = document.getElementById("quiz-next");
    const stepEl = document.getElementById("quiz-step");
    const progressEl = document.getElementById("quiz-progress");

    if (!questionEl || !optionsEl || !feedbackEl || !resultEl || !nextBtn || !stepEl || !progressEl) {
      return;
    }

    let index = 0;
    let score = 0;
    let answered = false;

    function renderQuestion() {
      const item = questions[index];
      answered = false;
      nextBtn.disabled = true;
      feedbackEl.textContent = "";
      resultEl.style.display = "none";

      stepEl.textContent = `Question ${index + 1} of ${questions.length}`;
      progressEl.style.width = `${((index + 1) / questions.length) * 100}%`;
      questionEl.textContent = item.q;

      optionsEl.innerHTML = "";
      item.options.forEach((choice, i) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.textContent = choice;
        btn.style.textAlign = "left";
        btn.style.padding = "0.65rem 0.75rem";
        btn.style.border = "1px solid #bcccdc";
        btn.style.borderRadius = "8px";
        btn.style.background = "white";
        btn.style.cursor = "pointer";

        btn.addEventListener("click", () => {
          if (answered) return;
          answered = true;

          const isCorrect = i === item.answer;
          if (isCorrect) {
            score += 1;
            btn.style.background = "#d3f9d8";
            btn.style.borderColor = "#2f9e44";
            feedbackEl.textContent = "Correct.";
          } else {
            btn.style.background = "#ffe3e3";
            btn.style.borderColor = "#c92a2a";
            feedbackEl.textContent = `Not quite. Correct answer: ${item.options[item.answer]}`;
          }

          Array.from(optionsEl.children).forEach((child, childIndex) => {
            child.disabled = true;
            if (childIndex === item.answer) {
              child.style.background = "#d3f9d8";
              child.style.borderColor = "#2f9e44";
            }
          });

          nextBtn.disabled = false;
          nextBtn.textContent = index === questions.length - 1 ? "Finish" : "Next";
        });

        optionsEl.appendChild(btn);
      });
    }

    nextBtn.addEventListener("click", () => {
      if (index < questions.length - 1) {
        index += 1;
        renderQuestion();
        return;
      }

      questionEl.textContent = "Quiz complete.";
      optionsEl.innerHTML = "";
      feedbackEl.textContent = "";
      nextBtn.style.display = "none";
      stepEl.textContent = "Done";
      progressEl.style.width = "100%";

      const percent = Math.round((score / questions.length) * 100);
      resultEl.style.display = "block";
      resultEl.textContent = `You scored ${score}/${questions.length} (${percent}%).`;
    });

    renderQuestion();
  })();
</script>
